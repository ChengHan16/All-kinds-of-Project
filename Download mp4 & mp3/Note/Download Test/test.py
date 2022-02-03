import tkinter as tk
from PIL import Image, ImageTk
from pytube.__main__ import YouTube    # 匯入tkinter模組
import tkinter.font as tkFont
#--------------------函式區域----------------------------------------------

from moviepy.editor import *
import fnmatch
from os import listdir
from os.path import isfile
from pytube import Playlist
import os, sys
from bs4 import BeautifulSoup
import requests as req
from tkinter import messagebox
from pytube import YouTube


def links_get(url):  # 取得播放清單所有影片網址的自訂函式
    urls = []   # 播放清單網址
    if '&list=' not in url :
        return urls    # 單一影片
    response = req.get(url)    # 發送 GET 請求
    if response.status_code != 200:
        print('請求失敗')
        return
    #請求成功, 解析網頁
    soup = BeautifulSoup(response.text, 'lxml')
    a_list = soup.find_all('a')
    base = 'https://www.youtube.com/'    # Youtube 網址
    for a in a_list:
        href = a.get('href')
        url = base + href  # 主網址結合 href 才是完整的影片網址
        if ('&index=' in url) and (url not in urls):
            urls.append(url)
    return urls

def video_download(url, listbox):
    print(url) #印出影片網址
    global yt
    yt = YouTube(url)
    name = yt.title
    no = listbox.size()     # 以目前列表框筆數為下載編號
    listbox.insert(tk.END, f'{no:02d}:{name}.....下載中')
    print('插入:', no, name)
    try:
        os.system('you-get ' +"\""+ url + "\"")
    except:
        try:
            print(yt.streams.get_highest_resolution().download())[0].download()
        except:
            print(yt.streams.get_highest_resolution().download())[1].download()
    print('更新:', no, name)
    listbox.delete(no)
    listbox.insert(no, f'{no:02d}:●{name}.....下載完成')
    # print(fileobj)
    return

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

#------------主視窗------------#
win = tk.Tk()                          # 建立主視窗物件
win.geometry('700x550')                # 設定主視窗預設尺寸為700x550
win.resizable(False,False)             # 設定主視窗的寬跟高皆不可縮放
win.title('YouTube Video Downloader')  # 設定主視窗標題
win.iconphoto(True, tk.PhotoImage(file='E:/Program/Python Project/Download mp3 Project/pytube-11.0.2/youtube.png')) # Title icon圖片設定 & 存放位置

# 設定圖片
img=Image.open('E:/Program/Python Project/Download mp3 Project/pytube-11.0.2/youtube.png')  # 開啟圖片位置
img = img.resize( (img.width // 4, img.height // 4) ) # 縮小圖片
img=ImageTk.PhotoImage(img)
imLabel=tk.Label(win,image=img)
imLabel.pack()

f1 = tkFont.Font(family='microsoft yahei', size=16, weight='bold')
f2 = tkFont.Font(family='microsoft yahei', size=10, weight='bold')

#設定網址輸入區域
input_frm = tk.Frame(win, width=640, height=50)
input_frm.pack()
#設定提示文字
lb = tk.Label(input_frm,text='請輸入影片連結或播放列表連結',fg='black',font=f1)
lb.place(rely=0.2, relx=0.5, anchor='center')
#設定輸入框
input_url = tk.StringVar()     # 取得輸入的網址
input_et = tk.Entry(input_frm, textvariable=input_url, width=60)
input_et.place(rely=0.75, relx=0.5, anchor='center')
#設定按鈕

#-----------------------------------------------------------------

def btn_click():   # 按鈕的函式
    url = input_url.get()          # 取得文字輸入框的網址
    try:    #  測試 pytube 是否支援此網址或者網址是否正確
        YouTube(url)
    except:
        messagebox.showerror('錯誤','pytube 不支援此影片或者網址錯誤')
        return
    # pytube 支援此網址, 進行網路爬蟲
    urls = links_get(url)
    #輸入網址中有影片清單
    if urls and messagebox.askyesno('確認方塊',
            '是否下載清單內所有影片？(選擇 否(N) 會下載單一影片)') :
    #下載清單中所有影片
        print('開始下載清單')
        urls.sort(key = lambda s:int(req.search("index=\d+",s).group()[6:]))
        #對所有影片網址做排序

        for url in urls:     # 建立與啟動執行緒
            video_download(url, listbox)
    #下載單一影片
    else:
        yt = YouTube(url)
        if messagebox.askyesno('確認方塊',
                               f'是否下載{yt.title}影片？') :
            video_download(url, listbox)
        else:
            print('取消下載')

#-----------------------------------------------------------------
def btn_click():   # 按鈕的函式
    print('後面再實作')

btn = tk.Button(input_frm, text='Download', command = btn_click,
                bg='orange', fg='Black',font=f2)
btn.place(rely=0.75, relx=0.9, anchor='center')

#下載清單區域
dl_frm = tk.Frame(win, width=640, height=280)
dl_frm.pack()

#設定提示文字
lb = tk.Label(dl_frm, text='Download list',fg='black',font=f1)
lb.place(rely=0.1, relx=0.5, anchor='center')

#設定顯示清單
listbox = tk.Listbox(dl_frm, width=65, height=15)
listbox.place(rely=0.6, relx=0.5, anchor='center')

#設定捲軸
sbar = tk.Scrollbar(dl_frm)
sbar.place(rely=0.6, relx=0.87, anchor='center', relheight=0.75)

#連結清單和捲軸
listbox.config(yscrollcommand = sbar.set)
sbar.config(command = listbox.yview)
win.mainloop()





