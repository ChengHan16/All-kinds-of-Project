## Subtitle grab
## 使用套件
### pip install youtube_transcript_api

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
>> 2. 建立虛擬環境 virtualenv venv-Subtitle-grab
>> 3. 開啟虛擬環境 .\venv-Subtitle-grab\Scripts\activate
>> 4. 在虛擬環境下安裝專案所需套件 pip3 install "套件名稱"
> ### pip install Complete
---
## －參考資料
> https://zhuanlan.zhihu.com/p/371123139
## －Error 
#### ● ERROR: Could not install packages due to an OSError: [WinError 5] 存取被拒。
&emsp;
`解決辦法：python -m pip install --upgrade pip`
&emsp;
> https://www.crifan.com/windows_python_install_error_could_not_install_/
#### ● 'cp950' codec can't encode ?
&emsp;
`解決辦法：修改 Python 程式，在 open 檔案時多一個輸入參數，讓讀寫檔案的編碼方式為 UTF-8` <br> `open('text.txt', 'w', encoding='UTF-8')`
&emsp;
> https://weirenxue.github.io/2021/06/12/python_cp950_codec_cant_encode/
