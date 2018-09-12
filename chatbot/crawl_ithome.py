import requests
from bs4 import BeautifulSoup
from datetime import date
# import pymssql
# conn = pymssql.connect(server='127.0.0.1:1433',
#                        user='SA',
#                        password='Asus#1234',
#                        database='SideProject',
#                        charset="utf8")
# cursor = conn.cursor()

today = date.today()
today = today.strftime("%Y-%m-%d")

def crawl_ithome():
    re=[]
    for p in range(2):

        r = requests.get("https://www.ithome.com.tw/news?page=%s"%p)
        soup = BeautifulSoup(r.text,"html5lib")
        select_item = soup.select('div.item')
        for i in select_item:
            select_title = i.select('p.title')
            select_url = i.select('p.title > a')
            select_day = i.select('p.post-at')
            select_photo = i.select('p.photo > a > img ')

            title = select_title[0].text
            url = 'https://www.ithome.com.tw'+select_url[0].get('href')
            day = select_day[0].text.strip(' ')
            photo = select_photo[0].get('src')

            if day == today:
                re.append((title[:40],url,day,photo))

    return re

print(crawl_ithome())
# ## "依序"一次插入一筆資料
# count=1
# insert_data = """INSERT INTO IThome VALUES (%s, %s)"""
# for d in IThome_data:
#     cursor.execute(insert_data,d)
#     print(count,d)
#     count+=1
# # 執行SQL動作
# conn.commit()
# conn.close()