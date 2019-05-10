#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

a = 'Python*Android*Java-888'
# 把字符串中的 * 字符替换成 & 字符
sub1 = re.sub('\*', '&', a)

print(sub1)

# 把字符串中的第一个 * 字符替换成 & 字符
sub2 = re.sub('\*', '&', a, 1)
print(sub2)

# 把字符串中的 * 字符替换成 & 字符,把字符 - 换成 |

# 1、定义一个函数
def convert(value):
    group = value.group()
    if (group == '*'):
        return '&'
    elif (group == '-'):
        return '|'

# 第二个参数，要替换的字符可以为一个函数
sub3 = re.sub('[\*-]', convert, a)

print(sub3)

'''
re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None；
而 re.search 匹配整个字符串，直到找到一个匹配。这就是它们之间的区别了。
'''

b = '<img src="https://s-media-cache-ak0.pinimg.com/originals/a8/c4/9e/a8c49ef606e0e1f3ee39a7b219b5c05e.jpg">'
# 使用 re.search
search = re.search('<img src="(.*)">', b)
# group(0) 是一个完整的分组
print(search.group(0))
print(search.group(1))
# 使用 re.findall
findall = re.findall('<img src="(.*)">', b)
print(findall)
# 多个分组的使用（比如我们需要提取 img 字段和图片地址字段）
re_search = re.search('<(.*) src="(.*)">', b)
# 打印 img
print(re_search.group(1))
# 打印图片地址
print(re_search.group(2))
# 打印 img 和图片地址，以元祖的形式
print(re_search.group(1, 2))
# 或者使用 groups
print(re_search.groups())