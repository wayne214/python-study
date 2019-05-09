# -*- coding: UTF-8 -*-
'''
进程池
使用进程池的方法批量创建子进程。
'''
from multiprocessing import Pool, Process, Queue
import os, time, random


def long_time_task(name):
    print('进程的名称：{0} ；进程的PID: {1}'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('进程 {0} 运行了 {1} 秒'.format(name, (end - start)))





def write(q):
    # 写数据进程
    print(' 写进程 的Pid：{0}'.format(os.getpid()))
    for value in ['两点水', '三点水', '四点水']:
        print('写进 Queue 的值为：{0}'.format(value))
        q.put(value)
        time.sleep(random.random())
def read(q):
    # 读取数据进程
    print('读进程的PID:{0}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('从 Queue 读取的值为：{0}'.format(value))


if __name__ == '__main__':
    print('主进程的PID:{0}'.format(os.getpid()))
    p = Pool(5)
    for i in range(6):
        p.apply_async(long_time_task, args=(i,))

    p.close()
    p.join()
    print(' 【END】')

    # 父进程创建 Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程 pw
    pw.start()
    # 启动子进程pr
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr 进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()