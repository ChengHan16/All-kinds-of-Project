# youtube-dl usage
## 抓取影片各項資訊,不下載影片 download 為 Flase
```py
from pprint import pprint
import youtube_dl

def get_video_info(youtube_url):
    video_info = {}

    with youtube_dl.YoutubeDL() as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        # pprint(info)
        video_info['ID'] = info.get('id')
        video_info['標題'] = info.get('title')
        video_info['影片縮圖'] = info.get('thumbnail')
        video_info['上傳者'] = info.get('uploader')
        video_info['上傳者網址'] = info.get('uploader_url')
        video_info['影片長度(秒)'] = info.get('duration')
        video_info['觀看次數'] = info.get('view_count')
        video_info['留言數'] = info.get('comment_count') # -
        video_info['喜歡數'] = info.get('like_count')
        video_info['不喜歡數'] = info.get('dislike_count')
        video_info['平均評分'] = info.get('average_rating')
        video_info['描述'] = info.get('description')
        video_info['標籤'] = info.get('tags')
        video_info['網頁網址'] = info.get('webpage_url')
        video_info['上傳日期'] = info.get('upload_date')
    return video_info

if __name__ == '__main__':
    video_info = get_video_info('https://www.youtube.com/watch?v=Vn3ocg9Fnc8&t=262s')
    pprint(video_info)
```
![image](https://user-images.githubusercontent.com/55220866/156368861-1e77242d-65ef-40b7-8d54-7e9fdb4e59a9.png)
