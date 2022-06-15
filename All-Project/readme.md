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
>> pip install beautifulsoup4
>> ### pip install requests
---
> Subtitle grab
>> ### pip install youtube-transcript-api
