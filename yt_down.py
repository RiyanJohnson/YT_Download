from pytubefix import YouTube
from moviepy import VideoFileClip,AudioFileClip
import re

def yt_download():
    link = input("Enter the link: ")
    yt = YouTube('{}'.format(link))

    global title
    title = yt.title
    print("Title: ",title)
    print("Views: ",yt.views)

    c = True
    while c == True:
        resolution = input("Resolution (Syntax: 720p,480p,1080p,...): ")
        yt_res = yt.streams.filter(res="{}".format(resolution))
        if len(yt_res)==0:
            resolution = input("Enter a resolution which exists: ")
            yt_res = yt.streams.filter(res="{}".format(resolution))
            c = False
            continue
        c = False
    try:
        y_aud = yt.streams.get_audio_only()
        y_aud.download('<same directory as the python file>')

        y_vid = yt_res.get_highest_resolution(progressive=False)
        y_vid.download('<same directory as the python file>')

        print("Downloaded")

    except:
        print("Error has occured")

def combine():  
    title1 = re.sub(r'[\|/?"]','',title)
    try:
        vid_clip = VideoFileClip("{}".format(title1+".webm"))
    except:
        vid_clip = VideoFileClip("{}".format(title1+".mp4"))
    
    aud_clip = AudioFileClip("{}".format(title1+".m4a"))

    final_clip = vid_clip.with_audio(aud_clip)
    final_clip.write_videofile("{}".format(title)+"_downloaded"+".mp4",threads = 16)

yt_download()
combine()