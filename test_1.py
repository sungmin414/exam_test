import os
from urllib import parse

import requests
from bs4 import BeautifulSoup


class Notice:
    def __init__(self, title, date, view):
        self.title = title
        self.date = date
        self.view = view

file_path = 'data/lol_list.html'
url = 'http://www.leagueoflegends.co.kr/?m=news&cate=notice'

if os.path.exists(file_path):
    html = open(file_path,'rt').read()

else:
    response = requests.get(url)
    html = response.text
    open(file_path,'wt').write(html)


soup = BeautifulSoup(html,'lxml')



table = soup.select('table.request-list > tbody > tr')

notice_list = list()

for title_list in table:
    title = title_list.select_one('td.tleft').text
    date = title_list.select_one('td:nth-of-type(2)').text
    view = title_list.select_one('td:nth-of-type(3)').text
    notice_list.append(Notice(title, date, view))


for notice in notice_list:
    print(notice.title)
    print(notice.date)
    print(notice.view)
    print()