from moviepy.editor import *
import fnmatch
from os import listdir
from os.path import isfile
from pytube import YouTube
import os, sys

link = 'https://www.youtube.com/watch?v=I8-hAvTJ-BE'  
YouTube(link).streams.get_highest_resolution().download()

path = "E:\Program\Python Project\Download mp3 Project"
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