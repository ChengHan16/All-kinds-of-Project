## － 使用套件：
### &emsp;&emsp; - Pytube <br> &emsp;&emsp; - you-get

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
>> 2. 建立虛擬環境 virtualenv venv-download-mp3
>> 3. 開啟虛擬環境 .\venv-download-mp3\Scripts\activate
>>> 關閉虛擬環境 deactivate <br>
>>> 刪除虛擬環境 env remove --name myenv
>> 4. 在虛擬環境下安裝專案所需套件 pip3 install "套件名稱"
> ### pip install Complete
---
## － Error：
### ERROR: Could not install packages due to an OSError: [WinError 5] 存取被拒。<br> : 'C:\\Users\\Harry\\AppData\\Local\\Temp\\pip-uninstall-aaiyrmoc\\pip.exe' <br> Consider using the `--user` option or check the permissions.
> 加上–user
>> ` python -m pip install --upgrade pip --user `
### in _execute_child hp, ht, pid, tid = _winapi.CreateProcess(executable, args, FileNotFoundError: <br> [WinError 2] 系统找不到指定的文件。
```
File "I:\Users\Administrator\AppData\Local\Programs\Python\Python38\lib\subprocess.py",
根据提示找到lib中的subprocess.py文件，CTRL+f查找class Popen模块，再将这个模块中的
init函数中的shell = False 改成shell = True

作者：302室
链接：https://www.jianshu.com/p/fbc31e1cc32a
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

### UTF-8 decode 0xa4
> 解決辦法：將 UTF-8 編碼改為 ANSI 

> Error: __init__: could not find match for ^\w+\W <br>
https://stackoverflow.com/questions/70776558/pytube-exceptions-regexmatcherror-init-could-not-find-match-for-w-w

### AttributeError: 'NoneType' object has no attribute 'span' <br>
> 解決辦法：<br>
Make sure you in pytube/cipher.py on line 293: <br>
You change <br>
`name = re.escape(get_throttling_function_name(js))` <br>
to <br>
`name = "iha"` <br>
https://stackoverflow.com/questions/70060263/pytube-attributeerror-nonetype-object-has-no-attribute-span
### AttributeError: 'NoneType' object has no attribute 'span' 方法 2<br>
```
改變：
  ● 文件 cipher.py，第 268 行到
   r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'r'\([a-z]\s*=\s*([a-zA-Z0-9$]{3})(\[\d+\])?\([a-z]\)',
  ● 文件 cipher.py，第 275 -> 277 行到
            logger.debug("finished regex search, matched: %s", pattern)
            if len(function_match.groups()) == 1:
                return function_match.group(1)
            idx = function_match.group(2)
            if idx:
                idx = idx.strip("[]")
                array = re.search(
                    r'var {nfunc}\s*=\s*(\[.+?\]);'.format(
                        nfunc=function_match.group(1)),
                    js
                )
                if array:
                    array = array.group(1).strip("[]").split(",")
                    array = [x.strip() for x in array]
                    return array[int(idx)]
```

### pytube.exceptions.RegexMatchError: get_throttling_function_name: could not find match for multiple
> https://stackoverflow.com/questions/68945080/pytube-exceptions-regexmatcherror-get-throttling-function-name-could-not-find
> 
把 cipher.py 內的
```
function_patterns = [

    r'a\.C&&\(b=a\.get\("n"\)\)&&\(b=([^(]+)\(b\),a\.set\("n",b\)\)}};',
]
```
改為：
```
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
r'\([a-z]\s*=\s*([a-zA-Z0-9$]{2,3})(\[\d+\])?\([a-z]\)'
```
還須將第288行改為：
```
nfunc=re.escape(function_match.group(1))),
```
### pytube.exceptions.RegexMatchError: __init__: could not find match for ^\w+\W
```
var_regex = re.compile(r"^\w+\W") 
```
改為 
```
var_regex = re.compile(r"^\$*\w+\W")
```
> 參考資料：https://stackoverflow.com/questions/70776558/pytube-exceptions-regexmatcherror-init-could-not-find-match-for-w-w

> https://github.com/pytube/pytube/issues/1218


## － 參考資料：

### Pytube 用法 (官方)
> https://pytube.io/en/latest/user/streams.html#filtering-streams

### Pytube 3
> https://pytube3.readthedocs.io/en/latest/api.html

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

## 待參考
### Python Script to Download YouTube Videos
> https://www.journaldev.com/40720/python-script-to-download-youtube-videos

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


