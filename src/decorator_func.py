# 装饰器
# 装饰器需要传递多个参数
# 通常情况下，我们会把*args和**kwargs，作为装饰器内部函数 wrapper() 的参数。
# *args和**kwargs，表示接受任意数量和类型的参数，
# 装饰器应用：
# 1.身份认证
# 2.日志记录
# 3.输入合理性检查
# 4.缓存
# 所谓的装饰器，其实就是通过装饰器函数，来修改原函数的一些功能，使得原函数不需要修改。


import functools
import time


# 函数执行时间装饰器
def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 100))
        return res

    return wrapper


def my_decorator(func):
    # 使用内置的装饰器 @ functools.wrap，它会帮助保留原函数的元信息（也就是将原函数的元信息，拷贝到对应的装饰器函数里）
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator function')
        func(*args, **kwargs)

    return wrapper


def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1 function')
        func(*args, **kwargs)

    return wrapper


# 类装饰器 ：：类装饰器主要依赖于函数__call__()，每当你调用一个类的示例时，函数__call__()就会被执行一次。
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)


# 装饰器嵌套，从上到下，从里到外执行，相当于log_execution_time(my_decorator1(my_decorator(greet)))
@log_execution_time
@my_decorator1
@my_decorator
def greet(messsage):
    print(messsage)


@Count
@my_decorator
def celebrate(name, message):
    print(name, message)


@log_execution_time
def logExecute():
    print('---test')


# greet = my_decorator(greet)

# greet('hha')

celebrate('wayne', 'hello world')
#
# logExecute()
