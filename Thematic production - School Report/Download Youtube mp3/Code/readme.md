### download_highvideo.py <br> ● 最高 720p
```py
from pytube import Playlist
playlist = Playlist('https://www.youtube.com/watch?v=3hSKNGcjFaA&list=PL12UaAf_xzfrBnvNaqS8tOniZddE4o9Q-')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

for video in playlist.videos:
    video.streams.get_highest_resolution().download()

print("全部下載成功！！！")
```
### 下載單一 1080p 的影片
```py
from pytube import YouTube
import os
import subprocess

fileobj = {}
download_count = 1

# 檢查影片檔是否包含聲音
def check_media(filename):
    r = subprocess.Popen([".\\bin\\ffprobe", filename],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = r.communicate()

    if (out.decode('ANSI').find('Audio') == -1):
        return -1  # 沒有聲音
    else:
        return 1

# 合併影片檔
def merge_media():
    temp_video = os.path.join(fileobj['dir'], 'temp_video.mp4')
    temp_audio = os.path.join(fileobj['dir'], 'temp_audio.mp4')
    temp_output = os.path.join(fileobj['dir'], 'output.mp4')

    cmd = f'".\\ffmpeg" -i "{temp_video}" -i "{temp_audio}" \
        -map 0:v -map 1:a -c copy -y "{temp_output}"'
    try:
        subprocess.call(cmd, shell=True)
        # 視訊檔重新命名
        os.rename(temp_output, os.path.join(fileobj['dir'], fileobj['name']))
        os.remove(temp_audio)
        os.remove(temp_video)
        print('視訊和聲音合併完成')
    except:
        print('視訊和聲音合併失敗')

def onProgress(stream, chunk, remains):
    total = stream.filesize
    percent = (total-remains) / total * 100
    print('下載中… {:05.2f}%'.format(percent), end='\r')

def download_sound():
    try:
        yt.streams.filter(type="audio").first().download()
    except:
        print('下載影片時發生錯誤，請確認網路連線和YouTube網址無誤。')
        return

# 檔案下載的回呼函式
def onComplete(stream, file_path):
    global download_count, fileobj
    fileobj['name'] = os.path.basename(file_path)
    fileobj['dir'] = os.path.dirname(file_path)
    print('\r')

    if download_count == 1:
        if check_media(file_path) == -1:
            print('此影片沒有聲音')
            download_count += 1
            try:
                # 視訊檔重新命名
                os.rename(file_path, os.path.join(
                    fileobj['dir'], 'temp_video.mp4'))
            except:
                print('視訊檔重新命名失敗')
                return

            print('準備下載聲音檔')
            download_sound()          # 下載聲音
        else:
            print('此影片有聲音，下載完畢！')
    else:
        try:
            # 聲音檔重新命名
            os.rename(file_path, os.path.join(
                fileobj['dir'], 'temp_audio.mp4'))
        except:
            print("聲音檔重新命名失敗")
        # 合併聲音檔
        merge_media()

yt = YouTube('https://www.youtube.com/watch?v=qhCMjYjVyEg', on_progress_callback=onProgress,
                     on_complete_callback=onComplete)
yt.streams.filter(subtype='mp4',resolution="1080p")[0].download()
```

### 下載單一 mp3 (download_mp4_and_mp3.py)
```py
from moviepy.editor import *
import fnmatch
from os import listdir
from os.path import isfile
from pytube import YouTube
import os, sys

link = 'https://www.youtube.com/watch?v=M1srS8BKvF4'  
YouTube(link).streams.get_highest_resolution().download()

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

### 下載清單 mp3 (download_mp4_and_mp3.py)
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
