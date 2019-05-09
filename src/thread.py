# -*- coding: UTF-8 -*-
import time
import threading

# 创建线程
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

    print('end Main threading')


if __name__ == '__main__':
    main()