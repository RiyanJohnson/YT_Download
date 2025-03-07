# YouTube Video Downloader

A simple Python script to download YouTube videos with separate audio and video streams, then combine them into a single MP4 file.

## Features

- Download YouTube videos in your preferred resolution
- Automatically extracts audio stream separately
- Combines video and audio into a single high-quality MP4 file
- Handles special characters in video titles

## Requirements

This script requires the following Python packages:
- pytubefix
- moviepy

## Installation

```bash
pip install pytubefix moviepy
```

## Usage

1. Run the script:
```python
python youtube_downloader.py
```

2. Enter the YouTube video URL when prompted
3. Choose your desired resolution (e.g., 720p, 1080p)
4. The script will download the video and audio separately, then combine them

## How It Works

The script works in two main steps:

1. **Download Phase**: Uses pytubefix to download the highest quality video stream in your chosen resolution and the audio stream separately.

2. **Combine Phase**: Uses moviepy to merge the video and audio files into a single MP4 file with the original video title.

## Limitations

- Some resolutions may not be available for certain videos
- The script downloads files to the same directory where it's located
- Special characters in video titles are handled but may affect filename consistency



