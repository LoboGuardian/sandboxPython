import os
import streamlink
import subprocess
import re
import requests
from bs4 import BeautifulSoup
import time
from typing import Tuple, Optional

# Constants
MAX_RETRIES = 3
RETRY_DELAY = 5
QUALITY_OPTIONS = ["best", "720p", "480p", "360p", "audio_only"]
DEFAULT_QUALITY = "best"

# Function to get video ID and title
def get_video_info(video_url: str) -> Optional[tuple[str, str]]:
    """
    Extracts video ID and title from Twitch URL.

    Args:
        video_url (str): The URL of the Twitch video.

    Returns:
        Optional[tuple[str, str]]: A tuple containing video ID and title, or None on error.
    """
    match = re.search(r"twitch\.tv/videos/(\d+)", video_url)
    if not match:
        return None

    video_id = match.group(1)
    downloads_folder = os.path.expanduser("~/Downloads")
    output_filename = os.path.join(downloads_folder, f"video_{video_id}.mp4")

    return video_id, output_filename

def download_video(video_url: str, quality: str, output_filename: str) -> bool:
    """
    Downloads video using streamlink.

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
        print(f"Error occurred during download: {e}")
        return False

def attempt_download(video_url: str, quality: str, output_filename: str) -> bool:
    """
    Attempts download with retries.

    Args:
        video_url (str): The URL of the Twitch video.
        quality (str): The desired video quality.
        output_filename (str): The filename to save the downloaded video.

    Returns:
        bool: True if download is successful, False otherwise.
    """
    for attempt in range(MAX_RETRIES):
        if download_video(video_url, quality, output_filename):
            return True
        print(f"Retrying download... ({attempt + 1}/{MAX_RETRIES})")
        time.sleep(RETRY_DELAY)
    print("Failed to download the video after several attempts.")
    return False

def main():
    video_url = input("Enter the Twitch video URL: ")

    info = get_video_info(video_url)
    if not info:
        print("Invalid Twitch video URL.")
        return

    video_id, output_filename = info

    selected_quality = input(f"Select quality ({', '.join(QUALITY_OPTIONS)}) [default: {DEFAULT_QUALITY}]: ") or DEFAULT_QUALITY

    if not attempt_download(video_url, selected_quality, output_filename):
        print("Download failed.")

if __name__ == "__main__":
    main()