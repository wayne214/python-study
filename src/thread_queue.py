# -*- coding: UTF-8 -*-
'''
线程间通信
从一个线程向另一个线程发送数据最安全的方式可能就是使用 queue 库中的队列了。
创建一个被多个线程共享的 Queue 对象，这些线程通过使用 put() 和 get() 操作来向队列中添加或者删除元素。
'''

from queue import Queue
from threading import Thread

isRead = True

def write(q):
    #写数据进程
    for value in ['两点水', '三点水', '四点水']:
        print('写进queue 的值为：{0}'.format(value))
        q.put(value)
def read(q):
    while isRead:
        value = q.get(True)
        print("从 queue 读取的值为：{0}".format(value))

if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=write, args=(q,))
    t2 = Thread(target=read, args=(q,))
    t1.start()
    t2.start()