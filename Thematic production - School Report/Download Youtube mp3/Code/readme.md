### download_highvideo.py <br> ● 最高 720p
```py
from pytube import Playlist
playlist = Playlist('https://www.youtube.com/watch?v=3hSKNGcjFaA&list=PL12UaAf_xzfrBnvNaqS8tOniZddE4o9Q-')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

for video in playlist.videos:
    video.streams.get_highest_resolution().download()

print("全部下載成功！！！")
```


### 下載清單影片 & mp3 (download_mp4_and_mp3.py)
```py
from moviepy.editor import *
import fnmatch
from os import listdir
from os.path import isfile
from pytube import Playlist
import os, sys

from pytube import YouTube
playlist = Playlist('https://www.youtube.com/watch?v=VZ13Ui8TjUk&list=OLAK5uy_kYAjVeVWGqZ7UjKer0O8j4_vMybyHR604')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

for video in playlist.videos:
    video.streams.get_highest_resolution().download()


path = "E:\Python Project\Download mp3 Project"
dirs = os.listdir( path )

for fullpath in dirs :
    if isfile(fullpath) and fnmatch.fnmatch(fullpath,"*.mp4"):
        #print(fullpath)
        
        mp4_file = fullpath
        mp3_file = fullpath.split(".")[0] + '.mp3'

        print(mp3_file)

        videoClip = VideoFileClip(mp4_file)
        audioclip = videoClip.audio
        audioclip.write_audiofile(mp3_file)

        audioclip.close()
        videoClip.close()
```
