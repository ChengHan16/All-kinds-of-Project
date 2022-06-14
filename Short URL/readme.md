## － 使用套件：
### &emsp;&emsp; - bitly_api

## － 建置虛擬環境：
> ###  PowerShell ISE
>> 1. get-executionpolicy (會回傳 Restricted
>> 2. set-executionpolicy remotesigned
>> 3. set-executionpolicy -Scope CurrentUser remotesigned
>> 4. get-executionpolicy (會回傳 RemoteSigned
> ### PowerShell Complete 
---
> ### pip install
>> 1. 安裝虛擬環境軟體 pip3 install virtualenv  
>> 2. 建立虛擬環境 virtualenv venv-short-url
>> 3. 開啟虛擬環境 .\venv-short-url\Scripts\activate
>>> 關閉虛擬環境 deactivate <br>
>>> 刪除虛擬環境 env remove --name myenv
>> 4. 在虛擬環境下安裝專案所需套件 pip3 install "套件名稱"
> ### pip install Complete
---
### &emsp;&emsp; - pip install bitly-api
---
## Code
編譯前需要先到 [bitly](https://bitly.com/) 註冊帳號，然後在個人設定中選取 Developer settings 裡的 `API`<br> 然後輸入密碼獲取你的 `Access token`
```py
import bitly_api

BITLY_ACCESS_TOKEN ="YOUR_ACCESS_TOKEN"

x = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
url_input = input("Enter the url: ")

response = x.shorten(url_input)
print(response)
```
---
## - Error
### ● 'from bitly_api import Connection, BitlyError, Error' in pycharm?
> 1.若以安裝 bitly_api 套件，就請先解除安裝 `pip uninstall bitly_api` <br><br>
> 2.從旁邊連結下載 Bitly API 模組 [bitly-api-python](https://github.com/bitly/bitly-api-python)，點擊綠色 Code 按 Dowanload <br><br>
> 3.將下載的文件解壓縮到目錄底下或是虛擬環境中的site-packages資料夾內，再來輸入 cd 切換進到 bitly-api-python-master資料夾<br> `cd bitly-api-python-master`<br><br>
> 4.在終端機中入指令來安裝 bitly_api 模組：`python setup.py install`<br><br>
> 5.在終端機中，通過輸入指令進入 Python shell python，然後輸入import bitly_api，如果沒有錯誤，則模組已成功安裝（忽略語法警告）。

參考資料：https://stackoverflow.com/questions/54977488/how-can-i-resolve-from-bitly-api-import-connection-bitlyerror-error-in-pycha

---
## 參考資料：
使用 Python 和 Bitly 缩短您的 URL
> https://news.sangniao.com/p/2237394596

How To Generate Bitly Shortener URLs with the Bitly API in Python 3
> https://pythonhowtoprogram.com/how-to-generate-bitly-shortener-urls-with-the-bitly-api-in-python-3/

