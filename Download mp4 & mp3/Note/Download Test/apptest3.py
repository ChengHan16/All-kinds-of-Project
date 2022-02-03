from pytube import Playlist

playlist = Playlist('https://www.youtube.com/playlist?list=PLOVg1anWBCbw3pxnrUBpJ4M4TYZmd7amC')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

for video in playlist.videos:
    stream = video.streams.get_by_itag(140)
    #stream = video.streams.order_by('resolution').desc()[0]
    stream.download()