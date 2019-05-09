# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import re
'''
正在表达式
'''


# 设定一个常量
a = '两点水|twowater|liangdianshui|草根程序员|ReadingWithU'

# 正则表达式
findall = re.findall('两点水', a)
print(findall)
if len(findall) > 0:
    print('a 含有“两点水”这个字符串')
else:
    print('a 不含有“两点水”这个字符串')

re_findall = re.findall('[a-z]', a)
print(re_findall)

b = 'uav,ubv,ucv,uwv,uzv,ucv,uov'

b_findall = re.findall('u[a-c]v', b)
b1_findall = re.findall('u[^abc]v', b)
print(b_findall)
print(b1_findall)

c = 'uav_ubv_ucv_uwv_uzv_ucv_uov&123-456-789'
# 概括字符集
# \d 相当于【0-9】，匹配所有数字字符
# \D 相当于 【^0-9】,匹配所有非数字字符
findall1 = re.findall('\d', c)
findall2 = re.findall('[0-9]',c)
findall3 = re.findall('\D', c)
findall4 = re.findall('[^0-9]',c)

print(findall1)
print(findall2)
print(findall3)
print(findall4)

# \w 匹配包括下划线的任何单词字符， 等价于 【A-Za-z0-9_】
findall5 = re.findall('\w', c)
findall6 = re.findall('[A-Za-z0-9_]', c)
print(findall5)
print(findall6)