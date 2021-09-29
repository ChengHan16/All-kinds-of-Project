# OpenCv & Python 影像辨識
> ## 範例教學影片：https://www.youtube.com/watch?v=wWG8qjKUmbk
> ### 虛擬環境：conda create --name ImgRecognition python=3.8
> ### 啟動：conda activate ImgRecognition
> ### 關閉：conda deacivate
## 安裝套件： <br> - pip install opencv-python
---
### ●【Code 照片顯示測試】
```py
import cv2 //import OpenCv 模組
import  numpy as np //import 數學運算模組

if __name__ == "__main__":

    img = cv2.imread("image1.jpg") //取讀照片

    cv2.namedWindow("image1", cv2.WINDOW_NORMAL) //使用Show將照片寫出來，讓照片調成視窗適當大小
    cv2.imshow("image1", img) //用CV2 Show 出來
    cv2.waitKey(0) //給等待時間
    cv2.destroyALLWindows() //有成功啟動後將視窗關掉
```
> #### 說明：正規寫法使用 main 來執行
### 執行結果：
![1](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/Thematic%20production%20-%20School%20Report/Img%20Placement%20area/OpenCv%20%26%20Python%20%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98/1%20%E5%9C%96%E7%89%87%E9%A1%AF%E7%A4%BA%E6%B8%AC%E8%A9%A6.JPG)
### ●【開始尋找輪廓】(使用閥值方法) 單獨做函式專門做處理
```py
import cv2
import  numpy as np

def findcontour(img: np.ndarray): //設檢查器 typing
    cv2.threshold(img, dst=img, *(89, 255, 0)) //輸入原況照片
    return img //回傳 cv2.threshold 所輸出的 img

if __name__ == "__main__":

    img = cv2.imread("image1.jpg")
    img = findcontour(img)

    cv2.namedWindow("image1", cv2.WINDOW_NORMAL)
    cv2.imshow("image1", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
> #### 設檢查器 typing：給他檢查今天未來輸入的型態都是對的
### 執行結果：
![2](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/Thematic%20production%20-%20School%20Report/Img%20Placement%20area/OpenCv%20%26%20Python%20%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98/2%20%E6%89%BE%E5%87%BA%E8%BC%AA%E5%BB%93.JPG)

> #### 透過 Opcv 的 threshold 功能將原始照片輸入進去 <br> cv2.threshold(img(輸入), dst=img, *(89, 255, 0)(輸出) <br> * (米字號) 是用來將所有東西拆開，把3個物件原本的一個 tuple 物件拆成 3 個物件變 89, 255, 0

## tuple！？
> ### 元組（tuple） 是 Python 的資料儲存容器之一，最大的特點就是，它是「不可變」（Immutable）的資料型態。 <br> Tuple 說明：https://selflearningsuccess.com/python-tuple/
 
### ●【變成灰階原況照片】 <br> 由於照片是彩色的，閥值設定會使顏色變得奇怪，所以此打算將照片變原況灰階狀態 <br> 透過 Convert(轉換) 的方式把照片變灰階 img gray
```py
import cv2
import numpy as np

def findcontour(img: np.ndarray):
    cv2.threshold(img, dst=img, *(89, 255, 0))
    return img

if __name__ == "__main__":

    img = cv2.imread("image1.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) //透過 Convert(轉換) 的方式把照片變灰階
    img = findcontour(img_gray) //輸出記得換成 Convert 過的 img_gray

    cv2.namedWindow("image1", cv2.WINDOW_NORMAL)
    cv2.imshow("image1", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
### 執行結果：
![3](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/Thematic%20production%20-%20School%20Report/Img%20Placement%20area/OpenCv%20%26%20Python%20%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98/3%20%E7%81%B0%E9%9A%8E%E5%8E%9F%E5%A7%8B%E5%9C%96%E7%89%87.JPG)
### ●【使用 morphology去除空洞】 <br> 若照片上有黑點點 & 圈圈的部分可以使用膨脹或侵蝕方式來去除
```py
import cv2
import numpy as np
from numpy import array, uint8

def findcontour(img: np.ndarray):
    cv2.threshold(img, dst=img, *(89, 255, 0))
    cv2.morphologyEx(img, dst=img,  *(2, array([[0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [1, 1, 1, 1, 1, 1, 1],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0]], dtype=uint8)), iterations=6) //可自定義想要的遮罩形狀, 需要加上 from numpy import array, uint8
    return img

if __name__ == "__main__":

    img = cv2.imread("image1.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = findcontour(img_gray)

    cv2.namedWindow("image1", cv2.WINDOW_NORMAL)
    cv2.imshow("image1", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
### 執行結果：
![4](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/Thematic%20production%20-%20School%20Report/Img%20Placement%20area/OpenCv%20%26%20Python%20%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98/4%20%E5%B0%87%E9%BB%91%E9%BB%9E%E7%A9%BA%E6%B4%9E%E5%8E%BB%E6%8E%89.JPG)
### ●【使用侵蝕將黑點拿掉】
```py
import cv2
import numpy as np
from numpy import array, uint8

def findcontour(img: np.ndarray):
    cv2.threshold(img, dst=img, *(89, 255, 0))
    cv2.morphologyEx(img, dst=img,  *(2, array([[0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [1, 1, 1, 1, 1, 1, 1],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0]], dtype=uint8)), iterations=6)
    cv2.erode(img, dst=img, *(array([[0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0],
                                     [1, 1, 1, 1, 1],
                                     [0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0]], dtype=uint8),), iterations=1) //使用erode(侵蝕)，並用類似遮罩做辨識
    cv2.dilate(img, dst=img, *(array([[0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [1, 1, 1, 1, 1, 1, 1],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0]], dtype=uint8),), **{'iterations': 8}) //使用dilate(膨脹)將黑點去掉
    return img

if __name__ == "__main__":

    img = cv2.imread("image1.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_copy = img_gray.copy()
    img = findcontour(img_gray)

    cv2.namedWindow("image1", cv2.WINDOW_NORMAL)
    cv2.namedWindow("compare", cv2.WINDOW_NORMAL)
    cv2.imshow("image1", img_gray)
    cv2.imshow("compare", img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
### 執行結果：
![5](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/Thematic%20production%20-%20School%20Report/Img%20Placement%20area/OpenCv%20%26%20Python%20%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98/5%20%E8%86%A8%E8%84%B9%E5%8F%8A%E4%BE%B5%E8%9D%95%E5%B0%87%E9%BB%91%E9%BB%9E%E5%8E%BB%E9%99%A4.JPG)
### ●【尋找輪廓】13:30 ~ 15:30
```py
import cv2
import numpy as np
from numpy import array, uint8

def findcontour(img: np.ndarray):
    cv2.threshold(img, dst=img, *(89, 255, 0))
    cv2.morphologyEx(img, dst=img,  *(2, array([[0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [1, 1, 1, 1, 1, 1, 1],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0]], dtype=uint8)), iterations=6)
    cv2.erode(img, dst=img, *(array([[0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0],
                                     [1, 1, 1, 1, 1],
                                     [0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0]], dtype=uint8),), iterations=1)
    cv2.dilate(img, dst=img, *(array([[0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [1, 1, 1, 1, 1, 1, 1],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0]], dtype=uint8),), **{'iterations': 8})
    return img

if __name__ == "__main__":

    img = cv2.imread("image1.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_copy = img_gray.copy()
    process = findcontour(img_gray) //此為處理中的圖所以更改名稱為 process
    process = cv2.Canny(process, 200, 255, apertureSize=5) //使用 Canny 的方式把邊找出來
    cnts, _ =  cv2.findContours(process, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) //照片存進來後會有一個輪廓，cnts
    print(len(cnts)) //列印出看有無找到輪廓
    exit()

    cv2.namedWindow("image1", cv2.WINDOW_NORMAL)
    cv2.namedWindow("compare", cv2.WINDOW_NORMAL)
    cv2.imshow("image1", img_gray)
    cv2.imshow("compare", img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
![6-1](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/Thematic%20production%20-%20School%20Report/Img%20Placement%20area/OpenCv%20%26%20Python%20%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98/6-1%20%E6%89%BE%E5%87%BA%E8%BC%AA%E5%BB%93.JPG)
### ●【檢查 OpenCV 版本】15:55

### ●【畫圖片將輪廓範圍顯示】(使用 drawcontours) ~17:30
```py
import cv2
import numpy as np
from numpy import array, uint8

def findcontour(img: np.ndarray):
    cv2.threshold(img, dst=img, *(89, 255, 0))
    cv2.morphologyEx(img, dst=img,  *(2, array([[0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [1, 1, 1, 1, 1, 1, 1],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0]], dtype=uint8)), iterations=6)
    cv2.erode(img, dst=img, *(array([[0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0],
                                     [1, 1, 1, 1, 1],
                                     [0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0]], dtype=uint8),), iterations=1)
    cv2.dilate(img, dst=img, *(array([[0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [1, 1, 1, 1, 1, 1, 1],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0]], dtype=uint8),), **{'iterations': 8})
    return img

if __name__ == "__main__":

    img = cv2.imread("image1.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_copy = img_gray.copy()
    process = findcontour(img_gray)
    process = cv2.Canny(process, 200, 255, apertureSize=5)
    cnts, _ =  cv2.findContours(process, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, cnts, -1, (0, 255, 0), 3) //取原始照片(彩色)後而cnts輪廓放進來，(0, 255, 0),為BGR 顏色綠，3為輪廓粗細

    cv2.namedWindow("image1", cv2.WINDOW_NORMAL)
    cv2.namedWindow("compare", cv2.WINDOW_NORMAL)
    cv2.imshow("image1", img)
    cv2.imshow("compare", img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
![6](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/Thematic%20production%20-%20School%20Report/Img%20Placement%20area/OpenCv%20%26%20Python%20%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98/6%20%E6%8A%93%E5%8F%96%E5%9C%96%E7%89%87%E7%95%AB%E5%87%BA%E8%BC%AA%E5%BB%93.JPG)
### ●【畫中心點】(透過 for 對物體 Cotainer 做跌代，可以在這判斷結果)
```py
import cv2
import numpy as np
from numpy import array, uint8

def findcontour(img: np.ndarray):
    cv2.threshold(img, dst=img, *(89, 255, 0))
    cv2.morphologyEx(img, dst=img,  *(2, array([[0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [1, 1, 1, 1, 1, 1, 1],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0]], dtype=uint8)), iterations=6)
    cv2.erode(img, dst=img, *(array([[0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0],
                                     [1, 1, 1, 1, 1],
                                     [0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0]], dtype=uint8),), iterations=1)
    cv2.dilate(img, dst=img, *(array([[0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [1, 1, 1, 1, 1, 1, 1],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0]], dtype=uint8),), **{'iterations': 8})
    return img

if __name__ == "__main__":

    img = cv2.imread("image1.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_copy = img_gray.copy()
    process = findcontour(img_gray)
    process = cv2.Canny(process, 200, 255, apertureSize=5)
    cnts, _ =  cv2.findContours(process, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)

    for c in cnts:
        if cv2.contourArea(c) < 300: //如果面積小於300就不執行任何動作，若沒有的話就對這輪廓做計算
            continue
        M = cv2.moments(c)
        Cx = int(M["m10"] / M["m00"])
        Cy = int(M["m01"] / M["m00"])
        cv2.circle(img, (Cx, Cy), 10, (1, 227, 254), -1)

    cv2.namedWindow("image1", cv2.WINDOW_NORMAL)
    cv2.namedWindow("compare", cv2.WINDOW_NORMAL)
    cv2.imshow("image1", img)
    cv2.imshow("compare", img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
### 執行結果：
![7](https://github.com/ChengHan16/All-kinds-of-Project/blob/main/Thematic%20production%20-%20School%20Report/Img%20Placement%20area/OpenCv%20%26%20Python%20%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98/7%20%E6%89%BE%E5%87%BA%E4%B8%AD%E5%BF%83%E9%BB%9E.JPG)
### ● 【完成程式碼】
```py
import cv2
import numpy as np
from numpy import array, uint8

def findcontour(img: np.ndarray):
    cv2.threshold(img, dst=img, *(89, 255, 0))
    cv2.morphologyEx(img, dst=img,  *(2, array([[0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [1, 1, 1, 1, 1, 1, 1],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0]], dtype=uint8)), iterations=6)
    cv2.erode(img, dst=img, *(array([[0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0],
                                     [1, 1, 1, 1, 1],
                                     [0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0]], dtype=uint8),), iterations=1)
    cv2.dilate(img, dst=img, *(array([[0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [1, 1, 1, 1, 1, 1, 1],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 0, 0, 0]], dtype=uint8),), **{'iterations': 8})
    return img

if __name__ == "__main__":

    img = cv2.imread("image1.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_copy = img_gray.copy()
    process = findcontour(img_gray)
    process = cv2.Canny(process, 200, 255, apertureSize=5)
    cnts, _ =  cv2.findContours(process, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)

    for c in cnts:
        if cv2.contourArea(c) < 300:
            continue
        M = cv2.moments(c)
        Cx = int(M["m10"] / M["m00"])
        Cy = int(M["m01"] / M["m00"])
        cv2.circle(img, (Cx, Cy), 10, (1, 227, 254), -1)

    cv2.namedWindow("image1", cv2.WINDOW_NORMAL)
    cv2.namedWindow("compare", cv2.WINDOW_NORMAL)
    cv2.imshow("image1", img)
    cv2.imshow("compare", img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
