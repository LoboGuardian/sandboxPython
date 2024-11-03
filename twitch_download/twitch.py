import os
import streamlink
import subprocess
import re
import requests
from bs4 import BeautifulSoup
import time
from typing import Tuple, Optional
from tqdm import tqdm

# Constants for configuration
MAX_RETRIES = 3 # Maximum number of download retries
RETRY_DELAY = 5  # Delay between retries in seconds
QUALITY_OPTIONS = ["best", "720p", "480p", "360p", "audio_only"] # Available video quality options
DEFAULT_QUALITY = "best" # Default video quality

# Function to extract video ID and title from URL
def get_video_info(video_url: str) -> Tuple[str, str]:
    """
    This function extracts the video ID and title from the provided Twitch video URL.

    Args:
        video_url (str): The URL of the Twitch video.

    Returns:
        Tuple[str, str]: A tuple containing the video ID and title.

    Raises:
        ValueError: If the URL is invalid.
        ConnectionError: If there's an issue retrieving the video page.
    """
    match = re.search(r"twitch\.tv/videos/(\d+)", video_url)
    if not match:
        raise ValueError("Invalid Twitch video URL.")
    video_id = match.group(1)

    response = requests.get(video_url)
    if response.status_code != 200:
        raise ConnectionError("Failed to retrieve the video page.")

    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title')
    if title: 
        return video_id,  title.text.replace(" - Twitch", "").strip()

    meta_title = soup.find("meta", property="og:title")
    if meta_title and 'content' in meta_title.attrs:
        return video_id, meta_title['content'].strip()

    raise ValueError("Could not find the video title.")

def get_stream_url_size(url: str) -> Optional[int]:
    """
    This function attempts to estimate the size of the stream using a HEAD request.

    Args:
      url (str): The URL of the stream.
    
    Returns:
      Optional[int]: The estimated size of the stream in bytes, or None if unavailable.
    """
    try:
        response = requests.head(url, allow_redirects=True)
        return int(response.headers.get('Content-Length', 0))
    except requests.RequestException as e:
        print(f"Error fetching size for {url}: {e}")
    return None


# Function to list available video qualities with estimated sizes
def list_quality_with_sizes(video_url: str):
    """
    This function retrieves available video qualities and attempts to estimate their sizes using streamlink.

    Args:
        video_url (str): The URL of the Twitch video.

    Raises:
        ValueError: If no streams are found for the URL.
    """
    streams = streamlink.streams(video_url)
    if not streams:
        raise ValueError("No streams found for the given URL.")

    for quality, stream in streams.items():
        size = get_stream_url_size(stream.url)
        size_mb = f"{size / (1024 * 1024):.2f} MB" if size else "Unknown"
        print(f"Quality: {quality}, Estimated Size: {size_mb}")

# Function to download the video using streamlink
def download_video(video_url: str, quality: str, output_filename: str) -> bool:
    """
    This function downloads the video using the specified quality and saves it to the provided output filename.

    Args:
      video_url (str): The URL of the Twitch video.
      quality (str): The desired video quality.
      output_filename (str): The filename to save the downloaded video.

    Returns:
      bool: True if download is successful, False otherwise.
    """
    command = f"streamlink {video_url} {quality} -o \"{output_filename}\""
    print(f"Starting download: {output_filename} at quality: {quality}.")
    try:
        subprocess.run(command.split(), check=True)
        print(f"Successfully downloaded: {output_filename}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during download: {e}")
        return False

# Function to attempt download with retries
def attempt_download(video_url: str, quality: str, output_filename: str, max_retries: int = MAX_RETRIES) -> bool:
    """
    This function attempts to download the video with retries in case of failure.

    Args:
      video_url (str): The URL of the Twitch video.
      quality (str): The desired video quality.
      output_filename (str): The filename to save the downloaded video.
      max_retries (int, optional): The maximum number of retries. Defaults to MAX_RETRIES.

    Returns:
      bool: True if download is successful, False otherwise.
    """
    for attempt in range(max_retries):
        if download_video(video_url, quality, output_filename):
            return True
        print(f"Retrying download... ({attempt + 1}/{max_retries})")
        time.sleep(RETRY_DELAY)
    print("Failed to download the video after several attempts.")
    return False

def get_downloads_folder():
    """
    This function checks for the user's Downloads folder and returns its path.
    If Downloads doesn't exist, it creates it.
    """
    # Get the user's home directory
    home = os.path.expanduser("~")
    
    # Check if the Downloads folder exists
    downloads = os.path.join(home, "Downloads")
    if os.path.exists(downloads) and os.path.isdir(downloads):
        return downloads
    
    # If Downloads doesn't exist, use the home directory
    return home

# Main function - program entry point
def main():
    try:
        video_url = input("Enter the Twitch video URL: ")

        try:
            video_id, video_title = get_video_info(video_url)
        except (ValueError, ConnectionError) as e:
            print(f"Error: {e}")
            return

        filename = f"{video_title.replace('/', '_')}_{video_id}.mp4"
        downloads_folder = get_downloads_folder()
        output_filename = os.path.join(downloads_folder, filename)

        print(f"File will be saved to: {output_filename}")

        print("Available quality options:")
        for i, option in enumerate(QUALITY_OPTIONS):
            print(f"{i}: {option}")
        choice = input("Select quality (0 for best, or enter desired quality): ")
        selected_quality = QUALITY_OPTIONS[int(choice)] if choice.isdigit() and int(choice) < len(QUALITY_OPTIONS) else DEFAULT_QUALITY

        if attempt_download(video_url, selected_quality, output_filename):
            print("Download successful!")
        else:
            print("Download failed.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        return

if __name__ == "__main__":
    main()
