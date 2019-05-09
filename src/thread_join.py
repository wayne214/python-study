# -*- coding: UTF-8 -*-
import time
import threading

# 线程合并-join
# 主线程要等待子线程运行完后，再退出
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, i))
            time.sleep(1)

def main():
    print('Start main threading')


    # 创建三个线程
    threads = [MyThread() for i in range(3)]
    # 启动三个线程
    for t in threads:
        t.start()

    # 一次让新创建的线程执行join
    for t in threads:
        t.join()

    print('end Main threading')


if __name__ == '__main__':
    main()


# 线程同步与互斥锁， Lock
lock = threading.Lock
# 获取锁
lock.acquire()
# 释放锁
lock.release()

#重入锁
# 当然为了支持在同一线程中多次请求同一资源，Python 提供了可重入锁（RLock）。
# RLock 内部维护着一个 Lock 和一个 counter 变量，counter 记录了 acquire 的次数，
# 从而使得资源可以被多次 require。直到一个线程所有的 acquire 都被 release，其他的线程才能获得资源
r_lock = threading.RLock

# 实用锁可以达到线程同步，但是在更复杂的环境，需要针对锁进行一些条件判断。
# Python 提供了 Condition 对象