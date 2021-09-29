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
