from math import factorial


# 高阶函数

def high_func(f, arr):
    return [f(x) for x in arr]

def square(n):
    return n ** 2

print(high_func(factorial, list(range(10))))

print(high_func(square, list(range(10))))