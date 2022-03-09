## Tkinter 基本架構
##  - Ⅰ 
### 匯入 Tkinter 函式庫
> import tkinter as tk
### 定義一個視窗 名叫 window
> window = tk.Tk() 
### 設定標題
> window.title('Tkinter_Test')
### 設定像素大小
> window.geometry('1280x720')
|補充解析度||
|--|--|
|  |1280x720|
|HD|1920*1080|
|SD|2560*1440|
|UHD|3840*2160|
### 設定主視窗寬、高皆不可縮放
> window.resizable(False,False)
### 主視窗迴圈顯示
> window.mainloop()
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
## Ⅱ
### Hello Word 
使用 標籤 ( Label )
> 宣告標籤的時候，需要先宣告一個標籤，再給予位置，如果沒有給予位置資訊的話將不會被放在視窗上面，這邊我們使用grid來告訴視窗標籤要放在該容器中的 (0, 0) 這個位置，此外沒有給定視窗寬、高大小的話，視窗會依照Widget大小而自動去調整：
```py
import tkinter as tk #匯入 Tkinter 函式庫

window = tk.Tk() #定義一個視窗 名叫 window
window.title('Tkinter_Test') #設定標題
window.geometry('1280x720') #設定像素大小
window.resizable(False,False) #設定主視窗寬、高皆不可縮放

lbl_1 = tk.Label(window, text='Hello World', background='light grey', foreground='black', font=('Arial', 20))
lbl_1.grid(column=0, row=0)

window.mainloop() #主視窗迴圈顯示
```
![image](https://user-images.githubusercontent.com/55220866/157254509-b912a1be-dc70-4435-b10d-99fc81fcb38d.png)
## Ⅲ
### 視窗元件使用
### 1. 文字輸入框 [tkinter Entry]
> tkinter Entry 基本用法，tk.Entry() 初始化完以後，用 grid() 來設定排版，Label 在左邊(0,0)，Entry 在右邊(0,1) ，之後就進入 mainloop()
>> Enter1 = tk.Entry(window) <br>
>> Enter1.grid(row=0, column=0)
### 範例
```py
import tkinter as tk
from turtle import bk #匯入 Tkinter 函式庫

window = tk.Tk() #定義一個視窗 名叫 window
window.title('Tkinter_Test') #設定標題
window.geometry('1280x720') #設定像素大小
window.resizable(False,False) #設定主視窗寬、高皆不可縮放
`
mylabel = tk.Label(window, text='Please enter URL：', font = ('微軟正黑體',15), background = '#BEBEBE')
mylabel.grid(row=0, column=0)

Enter1 = tk.Entry(window, width = 50)
Enter1.grid(row=0, column=1)

window.mainloop() #主視窗迴圈顯示
```
![image](https://user-images.githubusercontent.com/55220866/157454023-89029e72-7f0a-46de-9964-b527c236baa5.png)
### 2. 按鈕 ( Button )
> tkinter Button 的用法如下，一開始先用 tk.Button 建立一個按鈕，給這個按鈕一個顯示的文字 button，再用一個變數 mybutton 來儲存回傳的 tk.Button
>> mybutton = tk.Button(root, text='button') <br>
>> mybutton.pack()
```py
import tkinter as tk

window = tk.Tk() #定義一個視窗 名叫 window
window.title('Tkinter_Test') #設定標題
window.geometry('1280x720') #設定像素大小
window.resizable(False,False) #設定主視窗寬、高皆不可縮放

mylabel = tk.Label(window, text='Please enter URL：', font = ('微軟正黑體',15), background = '#BEBEBE')
mylabel.grid(row=0, column=0)

Enter1 = tk.Entry(window, width = 50)
Enter1.grid(row=0, column=1)

mybutton = tk.Button(window, text='button', font = ('微軟正黑體',12), background = '#BEBEBE')
mybutton.grid(row=0, column=2)

window.mainloop() #主視窗迴圈顯示
```
![image](https://user-images.githubusercontent.com/55220866/157456340-6fa7fc78-9082-4063-8c49-bbb1d89dc4fb.png)
### 3. 顯示圖片
> 要注意的是需要將圖片轉成Tkinter 可以讀的格式：
### 讀取圖片
> def create_label_image(): <br>
&emsp; img = Image.open('./images/cat_1.jpg')
### 縮小圖片
> img = img.resize( (img.width // 10, img.height // 10) )   
### 轉換成Tkinter可以用的圖片
> imgTk =  ImageTk.PhotoImage(img)
### 宣告標籤並且設定圖片
> lbl_2 = tk.Label(window, image=imgTk)
### 排版位置
> lbl_2.image = imgTk <br>
  lbl_2.grid(column=0, row=0)
### Result
```py
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk() #定義一個視窗 名叫 window
window.title('Tkinter_Test') #設定標題
window.geometry('720x320') #設定像素大小
window.resizable(False,False) #設定主視窗寬、高皆不可縮放

def create_label_image():
    img = Image.open('./images/youtube.png')      
    img = img.resize( (img.width // 6, img.height // 6) )   
    imgTk =  ImageTk.PhotoImage(img)
    lbl_2 = tk.Label(window, image=imgTk)
    lbl_2.image = imgTk
    lbl_2.place(x=315, y=50)

mylabel = tk.Label(window, text='Please enter URL：', font = ('微軟正黑體',12), background = '#BEBEBE')
mylabel.pack(side='left', ipadx=10, padx=10)

Enter1 = tk.Entry(window, width = 40)
Enter1.pack(side='left', ipadx=10, padx=10)

mybutton = tk.Button(window, text='Download', font = ('微軟正黑體',10), background = '#BEBEBE', width = 20)
mybutton.pack(side='left')

create_label_image()
window.mainloop() #主視窗迴圈顯示
```
![image](https://user-images.githubusercontent.com/55220866/157462426-91f80528-4491-4bf1-b68e-97d9ea79afe0.png)



## Error
### ◆ _tkinter.TclError: cannot use geometry manager pack inside . which already has slaves managed by grid
|method|describe|
|---|---|
|pack()|包装|
|grid()|網格|
|place()|位置|

解決方法：把 pack 都改成 grid <br>
> Step 1: Uninstall the PIL package.
>> pip uninstall PIL
>> python3 -m pip install --upgrade pip
>> python3 -m pip install --upgrade Pillow
>> pip install --upgrade --force-reinstall Pillow

參考資料：https://blog.csdn.net/cool99781/article/details/106200985

### ◆ Python ImportError: No module named PIL Solution
參考資料： https://itsmycode.com/python-importerror-no-module-named-pil-solution/

## 參考資料
> https://www.rs-online.com/designspark/python-tkinter-cn#_Toc61529918
