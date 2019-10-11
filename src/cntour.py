import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.cntour.cn/'
strhtml = requests.get(url)

soup = BeautifulSoup(strhtml.text, 'lxml')

data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')

# #main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li:nth-child(1) > a
for item in data:
    result = {
        'title': item.get_text(),
        'link': item.get('href'),
        'ID': re.findall('\d+', item.get('href'))
    }

print(result)