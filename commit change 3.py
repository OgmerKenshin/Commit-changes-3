import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def download_youtube_audio(youtube_url, output_dir="downloads"):
    """
    Downloads the audio from the YouTube video at the specified URL and converts it to MP3 format.
    """

    # Print the URL to verify what’s being passed
    print(f"Downloading from URL: {youtube_url}")
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

  