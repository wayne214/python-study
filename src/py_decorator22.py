# -*- coding: UTF-8 -*-
'''
装饰器

'''

import time


# def punch():
#     # 打卡功能
#     print('昵称：两点水  部门：做鸭事业部 上班打卡成功')

def add_time(func):
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    func()

def holiday():
    print('天气太冷，今天放假')

# add_time(punch)
# add_time(holiday)

# 装饰器写法
'''
装饰器函数一般做这三件事：

1.接收一个函数作为参数
2.嵌套一个包装函数, 包装函数会接收原函数的相同参数，并执行原函数，且还会执行附加功能
3.返回嵌套函数

Python 装饰器的核心可以说就是它的语法糖。
那么怎么使用它的语法糖呢？很简单，根据上面的写法写完装饰器函数后，直接在原来的函数上加 @ 和装饰器的函数名
'''

def decorator(func):
    def punch(*args, **kwargs):
        print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        func(*args, **kwargs)

    return punch
@decorator
def punch(name, department):
    # 打卡功能
    print('昵称：{0}  部门：{1} 上班打卡成功'.format(name, department))
@decorator
def print_args(reason, **kwargs):
    print(reason)
    print(kwargs)

punch('两点水','技术服务部')
print_args('点水点水', sex='男', age=99)