# Web image crawler
> ### 虛擬環境：conda create --name Webimagec python=3.8
> ### 啟動：conda activate Webimagec
> ### 關閉：conda deacivate
---
```py
# 第一個簡單的爬取圖片的程式
import urllib.request # python自帶的爬操作url的庫
import re # 正則表示式

# 該方法傳入url,返回url的html的原始碼
def getHtmlCode(url):
  # 以下幾行註釋的程式碼在本程式中有加沒加效果一樣,但是為了隱藏自己避免被反爬蟲可以假如這個偽裝的頭部請求
  headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36', }

  # 將headers頭部新增到url，模擬瀏覽器訪問
  url = urllib.request.Request(url,headers=headers)

  # 將url頁面的原始碼儲存成字串
  page = urllib.request.urlopen(url).read()
  # 字串轉碼
  page = page.decode('UTF-8')
  return page


# 該方法傳入html的原始碼，通過擷取其中的img標籤，將圖片儲存到本機
def getImage(page):
  # [^\s]*? 表示最小匹配， 兩個括號表示列表中有兩個元組
  # imageList = re.findall(r'(https:[^\s]*?(png))"',page)
  imageList = re.findall(r'(https:[^\s]*?(jpg|png|gif))"',page)
  x = 0
  # 迴圈列表
  for imageUrl in imageList:
    try:
      print('正在下載: %s' % imageUrl[0])
      # 這個image資料夾需要先建立好才能看到結果
      image_save_path = './image/%d.jpg' % x
      # 下載圖片並且儲存到指定資料夾中
      urllib.request.urlretrieve(imageUrl[0],image_save_path)
      x = x + 1
    except:
      continue
  pass
  print("---下載完成---")

if __name__ == '__main__':
  # 指定要爬取的網站
  url = "https://www.jkforum.net/thread-11188010-1-1.html"
  # 得到該網站的原始碼
  page = getHtmlCode(url)
  # 爬取該網站的圖片並且儲存
  getImage(page)
  # print(page)
```
