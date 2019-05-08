# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print('main')
else:
    print('not main')


# 作用域，在 Python 中，是通过 _ 前缀来实现的private函数
# 一般情况下，外部不需要引用的函数全部定义成 private，只有外部需要引用的函数才定义为 public。

def _diamond_vip(lv):
    print ('尊敬的钻石会员，您好')
    vip_name = 'DiamondVIP' + str(lv)
    return vip_name
def _gold_vip(lv):
    print ('尊敬的黄金会员,您好')
    vip_name = "GoldVIP" + str(lv)
    return vip_name

def vip_lv_name(lv):
    if lv == 1:
        print (_gold_vip(lv))
    elif lv == 2:
        print (_diamond_vip(lv))

vip_lv_name(2)