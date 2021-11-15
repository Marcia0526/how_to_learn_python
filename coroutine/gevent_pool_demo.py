import time
import gevent
from gevent.pool import Pool
from gevent import monkey
# 一，定义最大并发数
p = Pool(10)
# 二，导入gevent猴子补丁，没有它，协程就不会并发执行
monkey.patch_all()


#  三，耗时任务或者阻塞任务，异步执行的或者需要并发的就是它了
def task(i):
    print('start:'+str(i))
    time.sleep(1)
    print("-------------" + str(i))


# 四，任务派发，将15个任务派发给协程去做
threads = [p.spawn(task, i) for i in range(15)]

# 五，在此阻塞，等所有协程全部完成退出，这一步才执行完
gevent.joinall(threads)
print("main")


from asyncio import sleep

# from gevent.pool import Group
# # from gevent.pool import Pool
# from gevent import getcurrent
#
#
# def talk(data):
#     print('Size of group %s' % len(group))
#     # sleep(5)
#     print('Hello from Greenlet %s' % id(getcurrent()))
#     return data
#
#
# group = Group()
# res = group.imap(talk, range(5),maxsize=2)
#
# print(type(res))
# print(res)
# for i in res:
#     print(i)

# from gevent.pool import Pool
#
# pool = Pool(2)
#
#
# def hello_from(n):
#     print('Size of pool %s' % len(pool))
#     return n
#
#
# res = pool.map(hello_from, range(5))
# for i in res:
#     print(i)



# import gevent
# from gevent.pool import Pool
#
#
# class TestPool(object):
#     def __init__(self, maxsize=2):
#         self.pool = gevent.pool.Pool(maxsize)
#
#     def run(self):
#         for i in range(5):
#             gworker = gevent.spawn(self._worker, i)
#             self.pool.add(gworker)
#             print('sizeof pool is %d' % (len(self.pool),))
#             for gworker in self.pool:
#                 print(gworker)
#             # print('worker %d in? %r' % (i, gworker in self.pool))
#         self.pool.join()
#         print('All tasks done.')
#
#     def _worker(self, pid):
#         print('My pid is %d' % (pid,))
#         gevent.sleep(1)
#         print('%d has done.' % (pid,))
#
#
# if __name__ == '__main__':
#     test = TestPool()
#     test.run()