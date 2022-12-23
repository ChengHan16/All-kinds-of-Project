### [網路爬蟲_Facebook粉絲團貼文與留言](https://tlyu0419.github.io/2019/05/01/Crawl-Facebook/)
### [[爬蟲]如何用Python與Facebook API蒐集各大網站下面的"FB留言"?](http://bhan0507.logdown.com/posts/1406669-python-facebook-api-comments)
### [Day 21：專案04 - Facebook爬蟲02 | Selenium](https://ithelp.ithome.com.tw/articles/10272370)
-----
### [爬蟲教學](https://gist.github.com/HaoHsiu-Huang/f4a68bec77c17e0e118a6a5cb4dffed1)

# fb爬蟲教學

# 緣起
因為有朋友託我爬fb上的資料，方便收集貼文與留言，於是就利用python寫了這篇教學文。而fb是動態網頁，比方說往下滑動會新增貼文，要按顯示更多才會顯示剩下的留言。因此需要利用selenium這個測試套件來模擬人的動作，包括輸入資料，點擊...等等。
# 網址列表
由於fb粉專是公開的，我就只列一個做教學用，如果要增加的話，可以陸續加上，然後再用for迴圈給它一個一個跑。
```python
urls = ['https://www.facebook.com/groups/507155215969553']
```
# 瀏覽器設定
由於登陸fb後chrome瀏覽器會跳出通知，然後整個鎖住頁面，因此一開始就先設定關掉。
```python
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values':{'notifications': 2}}
options.add_experimental_option('prefs', prefs)
```
接著打開chrome，因為有些社團沒有登入fb是無法看到的，所以要登錄fb。
```python
driver = webdriver.Chrome(options=options)
driver.get('https://www.facebook.com/')
driver.find_element_by_id('email').send_keys('你的email')
driver.find_element_by_id('pass').send_keys('你的密碼')
driver.find_element_by_id('u_0_b').click()
```
其中find_element_by_id會定位到你指定的位置，依序輸入email和密碼，然後點擊登入。
我們先初始化資料格式為DataFrame，因此要載入pandas模組。
```python
import pandas as pd

collect_comment = pd.DataFrame()
collect_fb = pd.DataFrame()
```
進入目標頁面，我們只取一個來做教學，如果有很多個網址的話，可以用for迴圈給它跑。
```python
u = urls[0]
driver.get(u)
```
有一些留言的資料是隱藏起來的，需要把它點開來才會顯示出來。
```python
from time import sleep

def click_more(driver, text):
    for i in range(3):
        comment_more = driver.find_elements_by_partial_link_text(text)
        if len(comment_more) == 0:
            break
        for btn in comment_more:
            try:
                btn.click()
                sleep(1)
                print('. ',end='')
            except:
                continue
```
使用find_elements_by_partial_link_text定位，找到顯示更多的位置，並按下去。如果沒有可按的位置的話就跳出，然而有一些是會出現無法按的情況，所以使用try...except...來做例外處理。
將可以按的文字都按下去，觀察發現會出現以下四種文字。
```python
click_more(driver, '顯示先前')
click_more(driver, '檢視另')
click_more(driver, '查看另')
click_more(driver, '已回覆')
```
# 網頁分析
接下來把網頁原始碼拿出來，使用BeautifulSoup來做網頁分析。
```python
from bs4 import BeautifulSoup

htmltext = driver.page_source
soup = BeautifulSoup(htmltext, 'html5lib')
```
透過find_all來找出所有的貼文。
```python
articles = soup.find_all('div', class_='_4-u2 mbm _4mrt _5jmm _5pat _5v3q _7cqq _4-u8')
```
# 定義函式
接下來一個一個取出我們感興趣的內容，分析出來之後可以定義函式，方便記憶與運用。  
粉絲專頁名：
```python
def club_title(soup):
    return soup.title.string
```
貼文者：
```python
def article_person(article):
    return article.h5.a.string
```
貼文日期：
```python
def article_date(article):
    return article.abbr.string
```
貼文內容：
```python
def article_content(article):
    d = article_date(article)
    content = article.find('div', class_="_1dwg _1w_m _q7o").text.replace(d, '')
    return content
```
留言內容：
```python
def article_comment(article):
    try:
        comments = article.find('ul', class_="_7791").find_all('li')
        comment = []
        for i, c in enumerate(comments):
            if '隱藏或檢舉' in c.text:
                comment.append(c.text.split('隱藏或檢舉')[0])
            if '尋求支援' in c.text:
                comment.append(c.text.split('尋求支援')[0])
        return comment
    except:
        return []
```
# 取出資料並儲存
透過定義好的函式，將感興趣的資料一個一個取出來。
```python
titles = []
sites = []
persons = []
dates = []
contents = []
comments = []
for a in articles:
    titles.append(club_title(soup))
    sites.append(u)
    persons.append(article_person(a))
    dates.append(article_date(a))
    contents.append(article_content(a))
    comments.append(article_comment(a))
```
將資料整理成DataFrame的格式，方便編輯與查看。
```python
comments_len = [f'{len(c)}則留言' for c in comments]
df_fb = pd.DataFrame({'title': pd.Series(titles),
                      'site': pd.Series(sites),
                      'person': pd.Series(persons),
                      'date': pd.Series(dates),
                      'content': pd.Series(contents),
                      'comment': pd.Series(comments_len)
                     })
collect_fb = pd.concat([collect_fb, df_fb], ignore_index=True)
for c in comments:
    collect_comment = pd.concat([collect_comment, pd.Series(c)], axis=1)
```
看了一下collect_comment沒有欄位名，給它欄位名。
```python
x, y = collect_comment.shape
collect_comment.columns = [f'index{i}' for i in range(y)]
```
分析完成可以關閉瀏覽器了。
```python
driver.quit()
```
最後存成excel檔。
```python
writer = pd.ExcelWriter('output1.xlsx', engine='xlsxwriter')
collect_fb.to_excel(writer, sheet_name='fb', encoding='utf-8')
collect_comment.to_excel(writer, sheet_name='comment', encoding='utf-8')
writer.save()
```
