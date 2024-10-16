import streamlink
import subprocess
import re
import requests
from bs4 import BeautifulSoup
import time
from typing import Tuple, Optional

# Constants for configuration
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds
QUALITY_OPTIONS = ["best", "720p", "480p", "360p", "audio_only"]
DEFAULT_QUALITY = "best"

def get_video_info(video_url: str) -> Tuple[str, str]:
    """Extract the video ID and title from the given Twitch video URL."""
    match = re.search(r"twitch\.tv/videos/(\d+)", video_url)
    if not match:
        raise ValueError("Invalid Twitch video URL.")
    video_id = match.group(1)

    response = requests.get(video_url)
    if response.status_code != 200:
        raise ConnectionError("Failed to retrieve the video page.")

    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.find('title')
    if title_tag:
        video_title = title_tag.text.replace(" - Twitch", "").strip()
        return video_id, video_title

    meta_title_tag = soup.find("meta", property="og:title")
    if meta_title_tag and 'content' in meta_title_tag.attrs:
        return video_id, meta_title_tag['content'].strip()

    raise ValueError("Could not find the video title.")

def get_stream_url_size(url: str) -> Optional[int]:
    """Get the size of the stream from the URL using a HEAD request."""
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code == 200 and 'Content-Length' in response.headers:
            return int(response.headers['Content-Length'])
    except requests.RequestException as e:
        print(f"Error fetching size for {url}: {e}")
    return None

def list_quality_with_sizes(video_url: str):
    """List all available qualities with their estimated file sizes."""
    streams = streamlink.streams(video_url)
    if not streams:
        raise ValueError("No streams found for the given URL.")

    for quality, stream in streams.items():
        stream_url = stream.to_url()
        size = get_stream_url_size(stream_url)
        size_mb = f"{size / (1024 * 1024):.2f} MB" if size else "Unknown"
        print(f"Quality: {quality}, Estimated Size: {size_mb}")

def download_video(video_url: str, quality: str, output_filename: str) -> bool:
    """Download the video using Streamlink."""
    command = f"streamlink {video_url} {quality} -o \"{output_filename}\""
    print(f"Starting download: {output_filename} at quality: {quality}.")
    try:
        subprocess.run(command.split(), check=True)
        print(f"Successfully downloaded: {output_filename}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during download: {e}")
        return False

def attempt_download(video_url: str, quality: str, output_filename: str, max_retries: int = MAX_RETRIES) -> bool:
    """Attempt to download the video with retries on failure."""
    for attempt in range(max_retries):
        if download_video(video_url, quality, output_filename):
            return True
        print(f"Retrying download... ({attempt + 1}/{max_retries})")
        time.sleep(RETRY_DELAY)
    print("Failed to download the video after several attempts.")
    return False

def prompt_video_url() -> str:
    """Prompt the user to enter the Twitch video URL."""
    return input("Enter the Twitch video URL: ")

def prompt_quality_selection(quality_options: list[str]) -> str:
    """Prompt the user to select a video quality."""
    print("Available quality options:")
    for i, option in enumerate(quality_options):
        print(f"{i}: {option}")
    choice = input("Select quality (0 for best, or enter desired quality): ")
    return quality_options[int(choice)] if choice.isdigit() and int(choice) < len(quality_options) else DEFAULT_QUALITY

def handle_error(error: Exception):
    """Print the error message."""
    print(f"Error: {error}")

def main():
    video_url = prompt_video_url()

    try:
        video_id, video_title = get_video_info(video_url)
    except (ValueError, ConnectionError) as e:
        handle_error(e)
        return

    # print("\nFetching available qualities and their sizes...")
    # try:
    #     list_quality_with_sizes(video_url)
    # except ValueError as e:
    #     handle_error(e)
    #     return

    output_filename = f"{video_title.replace('/', '_')}_{video_id}.mp4"
    selected_quality = prompt_quality_selection(QUALITY_OPTIONS)

    if not attempt_download(video_url, selected_quality, output_filename):
        print("Download failed.")

if __name__ == "__main__":
    main()
