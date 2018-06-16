import os
from urllib import parse

import requests
from bs4 import BeautifulSoup

file_path = 'data/lol_list.html'
url = 'http://www.leagueoflegends.co.kr/?m=news&cate=notice'

if os.path.exists(file_path):
    html = open(file_path,'rt').read()

else:
    response = requests.get(url)
    html = response.text
    open(file_path,'wt').write(html)


soup = BeautifulSoup(html,'lxml')


table = soup.select_one('table.request-list')
tr_list = table.select('td > a')

for a in tr_list:
    print(f'{a.string}')
