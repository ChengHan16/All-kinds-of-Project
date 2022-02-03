from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=UbbOCalEfRY&list=OLAK5uy_lPcjle_Prc5nmHUpG5QGePsNX9I4LhFEI')
print(yt.streams.filter(file_extension='mp4'))
#stream = yt.streams.get_by_itag(140)
#stream = yt.streams.get_audio_only()
#stream.download()