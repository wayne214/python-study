# -*- coding: UTF-8 -*-
import multiprocessing
import time

def worker(interval, name):
    print(name + '[start]')
    time.sleep(interval)
    print(name + '[end]')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=worker, args=(2, 'wayne1'))
    p2 = multiprocessing.Process(target=worker, args=(3, 'wayne2'))
    p3 = multiprocessing.Process(target=worker, args=(4, 'wayne3'))

    p1.start()
    p2.start()
    p3.start()

    print('the number of CPU IS:' + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print('child p.name:' + p.name + "\tp.id" + str(p.pid))
    print("END!!!!!!!!!!!!!!!!!")


class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval
    def run(self):
        n = 5
        while n > 0:
            print("当前时间: {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1

p = ClockProcess(3)
# p.start()


def worker2(interval):
    print('工作开始时间：{0}'.format(time.ctime()))
    time.sleep(interval)
    print('工作结果时间：{0}'.format(time.ctime()))

pp = multiprocessing.Process(target=worker2, args=(3,))
# 如果在子进程中添加了 daemon 属性，那么当主进程结束的时候，子进程也会跟着结束。所以没有打印子进程的信息。
pp.daemon = True
pp.start()
# 那么我们可以用到 join 方法，join 方法的主要作用是：阻塞当前进程，
# 直到调用 join 方法的那个进程执行完，
# 再继续执行当前进程。
pp.join()

print('【END】')