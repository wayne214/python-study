# -*- coding: UTF-8 -*-
'''
线程间通信
Python 还提供了 Event 对象用于线程间通信，
它是由线程设置的信号标志，如果信号标志位真，则其他线程等待直到信号接触。
'''
import threading


class mThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        # 使用全局Event对象
        global event
        # 判断Event对象内部信号标志
        if event.isSet():
            event.clear()
            event.wait()
            print(self.getName())
        else:
            print(self.getName())
            # 设置Event对象内部信号标志
            event.set()

# 生成event对象
event = threading.Event()
# 设置Event对象内部信号标志
event.set()

t1 = []
for i in range(10):
    t = mThread(str(i))
    # 生成线程列表
    t1.append(t)

for i in t1:
    # 运行线程
    i.start()