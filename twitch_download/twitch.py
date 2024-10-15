import streamlink
import subprocess
import re
import requests
from bs4 import BeautifulSoup
import time

def get_video_info(video_url):
    """
    Extract the video ID and title from a given Twitch video URL.

    Args:
        video_url (str): The URL of the Twitch video.

    Returns:
        tuple: A tuple containing the video ID and title.

    Raises:
        ValueError: If the URL is invalid or if the title cannot be found.
        ConnectionError: If the video page cannot be fetched.
    """
    # Extract video ID from the URL
    match = re.search(r"twitch\.tv/videos/(\d+)", video_url)
    if not match:
        raise ValueError("Invalid Twitch video URL. Please enter a valid URL.")
    
    video_id = match.group(1)

    # Fetch the HTML of the video page
    response = requests.get(video_url)
    if response.status_code != 200:
        raise ConnectionError("Failed to retrieve the video page.")
    
    # Parse the HTML to find the video title using meta tags
    soup = BeautifulSoup(response.text, 'html.parser')

    # Try to find the title in the <title> tag first
    title_tag = soup.find('title')
    if title_tag:
        video_title = title_tag.text.replace(" - Twitch", "").strip()
        if video_title:
            return video_id, video_title
    
    # Fallback to looking for meta tags that might have a better title
    meta_title_tag = soup.find("meta", property="og:title")
    if meta_title_tag and 'content' in meta_title_tag.attrs:
        video_title = meta_title_tag['content']
        return video_id, video_title.strip()

    # Raise an error if no title could be found
    raise ValueError("Could not find the video title.")

def download_video(video_url, quality, output_filename):
    """
    Download the video using Streamlink.

    Args:
        video_url (str): The URL of the Twitch video.
        quality (str): The desired quality for download (e.g., 'best', '720p').
        output_filename (str): The filename for the downloaded video.

    Returns:
        bool: True if the download was successful, False otherwise.
    """
    command = f"streamlink {video_url} {quality} -o \"{output_filename}\""
    print(f"Starting download: {output_filename} at quality: {quality}.")
    
    # Execute the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully downloaded: {output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while downloading: {e}")
        return False
    
    return True

def main():
    video_url = input("Enter the Twitch video URL: ")  # User Input

    # Get video ID and title
    try:
        video_id, video_title = get_video_info(video_url)
    except Exception as e:
        print(f"Error: {e}")
        return

    # Set the output filename using the video title
    output_filename = f"{video_title.replace('/', '_')}_{video_id}.mp4"

    # Set the quality options
    quality_options = ["best", "720p", "480p", "360p"]

    print("Available quality options:")
    for i, option in enumerate(quality_options):
        print(f"{i}: {option}")

    # User selects quality
    quality_choice = input("Select quality (0 for best, or enter desired quality): ")
    selected_quality = quality_options[int(quality_choice)] if quality_choice.isdigit() and int(quality_choice) < len(quality_options) else "best"

    # Retry downloading in case of failure
    max_retries = 3
    for attempt in range(max_retries):
        if download_video(video_url, selected_quality, output_filename):
            break
        else:
            print(f"Retrying download... ({attempt + 1}/{max_retries})")
            time.sleep(5)  # Wait before retrying
    else:
        print("Failed to download the video after several attempts.")

if __name__ == "__main__":
    main()