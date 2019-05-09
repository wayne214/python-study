# -*- coding: utf-8 -*-
# 面向对象,创建新式类
# 旧式类
from hello import Hello
class OldClass:
    pass

# 新式类
class NewClass(object):
    pass

class test(object):
    # 直接在类中定义属性
    age = 1
    # 构造函数中定义属性
    # 一般情况下使用双下划线__定义private属性
    def __init__(self, name, account):
        self.name = name
        self.__account = account

    def getName(self):
        return self.name

    def get_account(self):
        return self.__account
    @property
    def get_name(self):
        return self.name

t = test('hha', 10000)

print (t.getName())
print (t.age)
print (t.get_account())
print (t.__dict__)
print (t.get_name)

print (test.age)

# 继承父类
class userInfo(test):
    pass

userInfo2 = userInfo('wayne', 1000)
print (userInfo2.get_account())


# 重写父类方法
class UserInfo(test):
    def __init__(self, name, account, sex):
        super(UserInfo, self).__init__(name, account)
        self.sex = sex

uss = UserInfo('ll', 100,'女')
print (uss.__dict__)

print (isinstance(userInfo2, userInfo))
print (isinstance(2222, int))
print (isinstance(2222, str))

# 多态, 有继承才有多态
class User(object):
    def __init__(self, name):
        self.name = name
    def printUser(self):
        print ('hello' + self.name)
class UserVip(User):
    def printUser(self):
        print ('hello 尊敬的VIp用户:' + self.name)
class UserGeneral(User):
    def printUser(self):
        print('Hello ! 尊敬的用户：' + self.name)
def printUserInfo(user):
    user.printUser()

vip = UserVip('大王')
printUserInfo(vip)
gen = UserGeneral('小王')
printUserInfo(gen)


# magic method
# 双下划线包起来的方法，都统称为"魔术方法
print (dir(NewClass()))

h = Hello()
h.hello()

print(type(Hello))
print(type(h))

# 使用type函数动态创建类
def printHello(self, name='py by type function'):
    # 定义一个打印hello 的函数
    print('Hello,', name)


# 创建一个Hello2类
Hello2 = type('Hello2',(object,), dict(hello=printHello))
# 实例化Hello2类
h2 = Hello2()
# 调用hello2类的方法
h2.hello()
# 查看Hello2 class的类型
print(type(Hello2))
# 查看实例h2的类型
print(type(h2))

# 1、class 的名称，比如例子中的起名为 Hello
#
# 2、继承的父类集合，注意 Python 支持多重继承，如果只有一个父类，tuple 要使用单元素写法；例子中继承 object 类，
# 因为是单元素的 tuple ，所以写成 (object,)
#
# 3、class 的方法名称与函数绑定；例子中将函数 printHello 绑定在方法名 hello 中
#
# 具体的模式如下：
#
# type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

# type() 函数是一个元类。type() 就是 Python 在背后用来创建所有类的元类。
# 元类就是类的类。也就是元类就是负责创建类的一种东西。
# 你也可以理解为，元类就是负责生成类的。而 type 就是内建的元类。也就是 Python 自带的元类。


# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        # 复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        return type.__new__(upperattr_metaclass, future_class_name, future_class_parents, uppercase_attr)