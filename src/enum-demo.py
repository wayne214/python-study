from enum import Enum, unique

Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September '
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'


if __name__ == '__main__':
    for name, member in Month.__members__.items():
        print(name, '---------', member, '----------', member.value)

# 枚举成员不是有序的，所以它们只支持通过标识(identity) 和相等性 (equality) 进行比较
import enum
# 使用 IntEnum 类进行枚举，就支持比较功能。
class User(enum.IntEnum):
    Twowater = 98
    Liangdianshui = 30
    Tom = 18
try:
    print('\n'.join(s.name for s in sorted(User)))
except TypeError as err:
    print('Error: {}'.format(err))