## Only outside Chinese can Subtitle grab
```py
from youtube_transcript_api import YouTubeTranscriptApi
import os

srt = YouTubeTranscriptApi.get_transcript("QN7BKarpltI")
text = ""
with open("file.txt","w", encoding='UTF-8') as file:
    for i in srt:
        text += i["text"] + "\n"
    file.write(text)

os.startfile("file.txt")
```
![image](https://user-images.githubusercontent.com/55220866/153379284-05b3869a-d192-466c-9cfa-0bf92d0d18a6.png)
