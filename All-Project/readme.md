## －建置虛擬環境：
> ###  PowerShell ISE
>> 1. get-executionpolicy (會回傳 Restricted
>> 2. set-executionpolicy remotesigned
>> 3. set-executionpolicy -Scope CurrentUser remotesigned
>> 4. get-executionpolicy (會回傳 RemoteSigned
> ### PowerShell Complete 
---
> ### pip install
>> 1. 安裝虛擬環境軟體 pip3 install virtualenv  
>> 2. 建立虛擬環境 virtualenv venv-All-Project
>> 3. 開啟虛擬環境 .\venv-All-Project\Scripts\activate
>> 4. 在虛擬環境下安裝專案所需套件 pip3 install "套件名稱"
> ### pip install Complete
---

## －Install Package
> Download mp4 & mp3
>> ###  pip install pytube
---
> Download image
>> ### pip install beautifulsoup4
>> ### pip install requests
---
> Subtitle grab
>> ### pip install youtube-transcript-api

> Convert mp4 to mp3
>> ### pip install moviepy
---
## [Download youtube mp4](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/All-Project/Download%20Youtube%20mp4.md)
## [Download youtube mp3](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/All-Project/Download%20Youtube%20mp3.md)
## [Youtube Subtitle grab](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/All-Project/Youtube%20Subtitle%20grab.md)
## [Convert mp4 to mp3](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/All-Project/Convert%20mp4%20to%20mp3.py)
## [Short URL](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/All-Project/Short%20URL.md)

---

### Error
[Python pip錯誤：無法辨識 ‘pip’ 詞彙是否為 Cmdlet、函數、指令檔或可執行程式的名稱。請檢查名稱拼字是否正確，如果包含路徑的話，請確認路徑是否正確，然後再試一次。]([https://dragongo.co/%E8%A7%A3%E6%B1%BA%EF%BC%9A%E7%84%A1%E6%B3%95%E8%BE%A8%E8%AD%98-pip-%E8%A9%9E%E5%BD%99%E6%98%AF%E5%90%A6%E7%82%BA-cmdlet%E3%80%81%E5%87%BD%E6%95%B8%E3%80%81%E6%8C%87%E4%BB%A4%E6%AA%94%E6%88%96/](https://dragongo.co/%E8%A7%A3%E6%B1%BA%EF%BC%9A%E7%84%A1%E6%B3%95%E8%BE%A8%E8%AD%98-pip-%E8%A9%9E%E5%BD%99%E6%98%AF%E5%90%A6%E7%82%BA-cmdlet%E3%80%81%E5%87%BD%E6%95%B8%E3%80%81%E6%8C%87%E4%BB%A4%E6%AA%94%E6%88%96/))

第一步：開啟檢視進階系統設定
第二步：選擇環進變數
第三步：從系統變數中選擇PATH變數，並按下編輯，若不小心按到刪除或新增，先將整個視窗取消，重新從第一部操作，避免影響windows系統。
第四步：按下新增
第五步：在新的一欄複製上
C:\Users\”你的使用者名稱”\AppData\Local\Programs\Python\Python38-32\Scripts
第六步：按下確認
第七步：重新開啟命令提示自元(cmd)、Visual Studio Code等軟體，重新輸入指令，即可解決此問題。
