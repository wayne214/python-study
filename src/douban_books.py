#-*- coding:utf-8 -*-
import requests
from lxml import etree
import time
from bs4 import BeautifulSoup

# url = 'https://www.baidu.com/'
# data = requests.get(url)
# data.encoding='utf-8'
# print(data.text)

url = 'https://book.douban.com/top250'
#给定url并用requests.get()方法来获取页面的text，用etree.HTML()
#来解析下载的页面数据“data”。
data = requests.get(url).text

s = etree.HTML(data)

books = s.xpath('//*[@id="content"]/div/div[1]/div/table')
# scores = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[2]/text()')

for i in range(10):
    url = 'https://book.douban.com/top250?start={}'.format(i * 25)
    # 总共10页，用 i*25 保证已25为单位递增
    data = requests.get(url).text
    s = etree.HTML(data)

    for div in books:
        name = div.xpath('./tr/td[2]/div[1]/a/@title')[0]
        score = div.xpath('tr/td[2]/div[2]/span[2]/text()')[0]
        comment = div.xpath('tr/td[2]/p[2]/span/text()')[0]
        # 加个睡眠，防止IP被封
        time.sleep(1)

        print('书名：{} --> 评分：{} --> 评价：{}'.format(name, score, comment))