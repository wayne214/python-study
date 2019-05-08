# -*- coding: utf-8 -*-
# 面向对象,创建新式类
# 旧式类
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