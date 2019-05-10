#-*- coding:utf-8 -*-
import requests
from lxml import etree
import time
from bs4 import BeautifulSoup

# url = 'https://www.baidu.com/'
# data = requests.get(url)
# data.encoding='utf-8'
# print(data.text)

url = 'https://movie.douban.com/subject/26942674/'
#给定url并用requests.get()方法来获取页面的text，用etree.HTML()
#来解析下载的页面数据“data”。
data = requests.get(url).text

s = etree.HTML(data)
'''
获取电影的xpath信息并获得文本
s.xpath('元素的xpath信息/text()')
'''


film_name = s.xpath('//*[@id="content"]/h1/span[1]/text()') #电影名称
film_director = s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()') #导演
actor = s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()') #主演
movie_time=s.xpath('//*[@id="info"]/span[13]/text()')#片长

# 多个导演
ds = []
for d in film_director:
    ds.append(d)
# 多个主演
acs = []
for a in actor:
    acs.append(a)
print('电影名:',film_name)
print('导演:',ds)
print('主演:',acs)
print('片长:',movie_time)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko)\
      Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'lxml')
element = soup.select('#content h1 span')
print(element)