from pytube import Playlist
from pytube import YouTube
'''playlist = Playlist('https://www.youtube.com/watch?v=GZu-L31SKTs')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

for video in playlist.videos:
    video.streams.get_highest_resolution().download()'''

link = 'https://www.youtube.com/watch?v=GZu-L31SKTs'  
YouTube(link).streams.get_highest_resolution().download()

print("全部下載成功！！！")