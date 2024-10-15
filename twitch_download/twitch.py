import streamlink
import subprocess
import re
import requests
from bs4 import BeautifulSoup

# Twitch video URL
video_url = input("Enter the Twitch video URL: ")

# Extract the video ID from the URL using regular expressions
match = re.search(r"twitch\.tv/videos/(\d+)", video_url)
if match:
    video_id = match.group(1)
else:
    print("Invalid Twitch video URL. Prease enter a valid URL.")
    exit()

# Fetch the HTML of the video page
response = requests.get(video_url)
if response.status_code != 200:
    print("Failed to retrieve the video page.")
    exit()

# Parse the HTML to find the video title
soup = BeautifulSoup(response.text, 'html.parser')
title_tag = soup.find('title')
if title_tag:
    video_title = title_tag.text.replace(" - Twitch", "").strip()  # Clean up the title
else:
    print("Could not find the video title.")
    exit()

# Set the output filename using the video title
output_filename = f"{video_title.replace('/', '_')}_{video_id}.mp4"

# Set the quality options
quality_options = ["best", "720p", "480p", "360p"]
print("Available quality options:")
for i, option in enumerate(quality_options):
    print(f"{i}: {option}")
# Prompt the user to select quality or use default
quality_choice = input("Select quality (0 for best, or enter desired quality): ")
if quality_choice.isdigit() and int(quality_choice) < len(quality_options):
    selected_quality = quality_options[int(quality_choice)]
else:
    selected_quality = "best"

# Command to download the video using streamlink
command = f"streamlink {video_url} {selected_quality} -o \"{output_filename}\""

# Execute the command using subprocess
subprocess.call(command, shell=True)

print(f"Downloaded the video as {output_filename} in {selected_quality} quality.")