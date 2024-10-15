import yt_dlp
import os

def download_video(youtube_url, video_format):
    download_path = os.path.expanduser('~/Downloads')  # Path to download directory

    # Options for downloading video
    ydl_opts = {
        'format': f'bestvideo[ext={video_format}]+bestaudio/best',  # Downloads best video of selected format
        'merge_output_format': video_format,  # Specify the video output format
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Output file naming
        'noplaylist': True,  # Prevent downloading playlists
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([youtube_url])
        except Exception as e:
            print(f"An error occurred: {e}")

def download_audio(youtube_url, audio_format):
    download_path = os.path.expanduser('~/Downloads')  # Path to download directory

    # Options for downloading audio
    ydl_opts = {
        'format': 'bestaudio/best',  # Select best audio available
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Post-processor to convert to audio
            'preferredcodec': audio_format,  # Selected audio format
            'preferredquality': '320',  # For MP3 or others; adjust accordingly
        }],
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Output file naming
        'noplaylist': True,  # Prevent downloading playlists
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([youtube_url])
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    url = input("Enter the YouTube video URL: ")
    choice = input("Do you want to download video (v) or audio (a)? ").strip().lower()

    if choice == 'v':
        video_format = input("Enter the video format (mp4, webm, mkv): ").strip().lower()
        if video_format in ['mp4', 'webm', 'mkv']:
            download_video(url, video_format)
        else:
            print("Invalid video format. Please enter 'mp4', 'webm', or 'mkv'.")
    elif choice == 'a':
        audio_format = input("Enter the audio format (mp3, wav, ogg): ").strip().lower()
        if audio_format in ['mp3', 'wav', 'ogg']:
            # Map 'ogg' and others to formats supported by FFmpeg
            if audio_format == 'ogg':
                audio_format = 'vorbis'  # 'vorbis' is the codec used for 'ogg'
            download_audio(url, audio_format)
        else:
            print("Invalid audio format. Please enter 'mp3', 'wav', or 'ogg'.")
    else:
        print("Invalid choice. Please enter 'v' for video or 'a' for audio.")
