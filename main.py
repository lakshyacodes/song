from pytube import YouTube
import os
import urllib.request
import re
print("Enter artist name!(without white space)")
artist_name=input(">> ")
print("Enter song/track name!")
song_name=input(">> ")
url="https://www.youtube.com/results?search_query="+artist_name+song_name
url="".join(url.split())

html = urllib.request.urlopen(url)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
video=video_ids[0]
video_url="https://www.youtube.com/watch?v="+video
# url input from user
yt = YouTube(video_url)
video = yt.streams.filter(only_audio=True).first()
destination = ""
out_file = video.download(output_path=destination)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
print(yt.title + " has been successfully downloaded.")