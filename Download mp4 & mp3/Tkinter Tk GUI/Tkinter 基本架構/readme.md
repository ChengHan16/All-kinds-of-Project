## Tkinter 基本架構
##  - Ⅰ 
### 匯入 Tkinter 函式庫
`import tkinter as tk`
### 定義一個視窗 名叫 window
`window = tk.Tk() `
### 設定標題
`window.title('Tkinter_Test')`
### 設定像素大小
`window.geometry('1280x720')`
|補充解析度||
|--|--|
|  |1280x720|
|HD|1920*1080|
|SD|2560*1440|
|UHD|3840*2160|
### 設定主視窗寬、高皆不可縮放
`window.resizable(False,False)`
### 主視窗迴圈顯示
`window.mainloop()`
### 完整 CODE
```py
import tkinter as tk #匯入 Tkinter 函式庫

window = tk.Tk() #定義一個視窗 名叫 window
window.title('Tkinter_Test') #設定標題
window.geometry('1280x720') #設定像素大小
window.resizable(False,False) #設定主視窗寬、高皆不可縮放
window.mainloop() #主視窗迴圈顯示
```
![image](https://user-images.githubusercontent.com/55220866/157248672-2a03f16a-a633-4f45-a0c1-f2c807655bd4.png)




