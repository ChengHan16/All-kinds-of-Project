## 使用套件：
### &emsp;&emsp; - Pytube <br> &emsp;&emsp; - you-get

## 建置虛擬環境：
###  ⚠ 安裝 Python 3.9.6 (記得勾選安裝的首頁最下面的 Add Python 3.9 to PATH)
> ###  PowerShell ISE
>> 1. get-executionpolicy (會回傳 Restricted
>> 2. set-executionpolicy remotesigned
>> 3. set-executionpolicy -Scope CurrentUser remotesigned
>> 4. get-executionpolicy (會回傳 RemoteSigned
> ### PowerShell Complete 
---
> ### pip install
>> 1. 安裝虛擬環境軟體 pip3 install virtualenv  
>> 2. 建立虛擬環境 virtualenv venv-download-mp3
>> 3. 開啟虛擬環境 .\venv-download-mp3\Scripts\activate
>> 4. 在虛擬環境下安裝專案所需套件 pip3 install "套件名稱"
> ### pip install Complete
---
## 參考資料：

### Pytube 用法 (官方)
> https://pytube.io/en/latest/user/streams.html#filtering-streams

### pytube模塊，下載YouTube視頻
> https://www.twblogs.net/a/5db31e1abd9eee310ee66ae4

### module contains a lookup table of YouTube's itag values
> https://github.com/pytube/pytube/blob/master/pytube/itags.py

### 視窗圖形介面的Youtube影片下載程式
> https://zh-tw.coderbridge.com/@Eterna-E

### YouTube影片下載（一）：合併視訊和音軌的Python程式
> https://swf.com.tw/?p=1357

### YouTube影片下載（五）：PyTube3程式庫更新說明
> https://swf.com.tw/?p=1402

### Python tkinter 視窗程式設計教學：Hello World
> https://officeguide.cc/python-tkinter-gui-tcl-tk-interface-tutorial-examples/

### 使用Python Tkinter 模組
> https://www.rs-online.com/designspark/python-tkinter-cn

### tkinter 模組字體（font）的使用
> https://www.pynote.net/archives/1220

### 從零開始學Python - 圖形化使用者介面Tkinter
> https://ithelp.ithome.com.tw/articles/10247294

### [Python] 使用 tqdm 套件展示進度條
> https://clay-atlas.com/blog/2019/11/11/python-chinese-tutorial-tqdm-progress-and-ourself/

### 使用pytube下載Youtube list
> https://liaozihzrong.github.io/2020/08/14/allinone19/

### ffmpeg 將音頻轉換為不同的格式/採樣率
> https://gist.github.com/protrolium/e0dbd4bb0f1a396fcb55

### 特定目錄中下載 How to download whole playlist videos from YouTube using Python 
> https://freshlybuilt.com/how-to-download-whole-playlist-videos-from-youtube-using-python/

## Other：
### FFmpeg 批量 AV 轉換器
> https://ffmpeg-batch.sourceforge.io/

### python+ffmpeg視訊轉碼轉格式
> https://iter01.com/595405.html

### ffmpeg 轉換代碼
> https://www.codegrepper.com/code-examples/whatever/ffmpeg+batch+convert+wav+to+mp3

### Python竟可以輕鬆實現音訊格式無損轉換
> https://www.gushiciku.cn/pl/gIZv/zh-tw

### python實現指定資料夾下的指定檔案移動到指定位置
> https://www.itread01.com/article/1537165863.html
