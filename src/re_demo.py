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

'''
数量词

贪婪模式：它的特性是一次性地读入整个字符串，如果不匹配就吐掉最右边的一个字符再匹配，直到找到匹配的字符串或字符串的长度为 0 为止。
它的宗旨是读尽可能多的字符，所以当读到第一个匹配时就立刻返回。

懒惰模式：它的特性是从字符串的左边开始，试图不读入字符串中的字符进行匹配，失败，则多读一个字符，再匹配，如此循环，
当找到一个匹配时会返回该匹配的字符串，然后再次进行匹配直到字符串结束。

上面例子中的就是贪婪的，如果要使用非贪婪，也就是懒惰模式，怎么呢？

如果要使用非贪婪，则加一个 ? ，上面的例子修改如下：
'''


d = 'java*&39android##@@python'
# 贪婪与非贪婪
findall7 = re.findall('[a-z]{4,7}?',d)
print(findall7)