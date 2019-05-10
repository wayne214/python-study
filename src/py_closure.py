# -*- coding: UTF-8 -*-
'''
闭包

这种内部函数的局部作用域中可以访问外部函数局部作用域中变量的行为，我们称为： 闭包。更加直接的表达方式就是，当某个函数被当成对象返回时，夹带了外部变量，就形成了一个闭包。k

闭包避免了使用全局变量，此外，闭包允许将函数与其所操作的某些数据（环境）关连起来。而且使用闭包，可以使代码变得更加的优雅。而且下一篇讲到的装饰器，也是基于闭包实现的。
'''

time = 0
def study_time(time):
    def insert_time(min):
        # nonlocal 关键字,表示在函数或其他作用域中使用外层(非全局)变量
        nonlocal time
        time = time + min
        return time
    return insert_time

f = study_time(time)
# 所有函数都有一个 __closure__ 属性，如果函数是闭包的话，那么它返回的是一个由 cell 组成的元组对象。
# cell 对象的 cell_contents 属性就是存储在闭包中的变量。
print(f.__closure__)
print(f(2))
print(time)
print(f.__closure__[0].cell_contents)
print(f(10))
print(time)
print(f.__closure__[0].cell_contents)