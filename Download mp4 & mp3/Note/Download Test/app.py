from pytube import Playlist

playlist = Playlist('https://www.youtube.com/watch?v=UbbOCalEfRY&list=OLAK5uy_lPcjle_Prc5nmHUpG5QGePsNX9I4LhFEI')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video in playlist.videos:
    video.streams.get_audio_only().download()