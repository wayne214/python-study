# -*- coding: UTF-8 -*-
import time
import threading
'''
Condition条件变量
实用锁可以达到线程同步，但是在更复杂的环境，需要针对锁进行一些条件判断。
Python 提供了 Condition 对象。
使用 Condition 对象可以在某些事件触发或者达到特定的条件后才处理数据，
Condition 除了具有 Lock 对象的 acquire 方法和 release 方法外，
还提供了 wait 和 notify 方法。线程首先 acquire 一个条件变量锁。
如果条件不足，则该线程 wait，如果满足就执行线程，甚至可以 notify 其他线程。
其他处于 wait 状态的线程接到通知后会重新判断条件。

其中条件变量可以看成不同的线程先后 acquire 获得锁，
如果不满足条件，可以理解为被扔到一个（ Lock 或 RLock ）的 waiting 池。
直达其他线程 notify 之后再重新判断条件。不断的重复这一过程，从而解决复杂的同步问题。

'''

# 生产者与消费者
class Consumer(threading.Thread):
    def __init__(self, cond, name):
        #初始化
        super(Consumer,self).__init__()
        self.cond = cond
        self.name = name
    def run(self):
        time.sleep(1)
        self.cond.acquire()
        print(self.name + '：我这两件商品一起买，可以便宜点吗')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 我已经提交订单了， 你修改一下价格')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 收到，我支付成功了')
        self.cond.notify()
        self.cond.release()
        print(self.name + ': 等待收货')


class Producer(threading.Thread):
    def __init__(self, cond, name):
        super(Producer, self).__init__()
        self.cond = cond
        self.name = name
    def run(self):
        self.cond.acquire()
        # 释放对琐的占用，同时线程挂起在这里，直到被 notify 并重新占有琐。
        self.cond.wait()
        print(self.name + ': 可以的，你提交订单吧')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 好了，已经修改了')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 嗯，收款成功，马上给你发货')
        self.cond.release()
        print(self.name + ': 发货商品')

cond = threading.Condition()
consumer = Consumer(cond, "买家（张三）")
producer = Producer(cond, '卖家（李四）')
consumer.start()
producer.start()
