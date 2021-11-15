# import gevent
# from gevent.pool import Group
#
#
# def talk(msg):
#     for i in range(2):
#         print(msg)
#
#
# g1 = gevent.spawn(talk, 'bar')
# g2 = gevent.spawn(talk, 'foo')
# group = Group()
# group.add(g1)  # 将greenlet添加进group
# group.add(g2)  # 将greenlet添加进group
# group.join() #等待Group中所有协程任务执行完毕

# from gevent.pool import Group
# from gevent import getcurrent
#
#
# def talk(data):
#     print('Size of group %s' % len(group))
#     print('Hello from Greenlet %s' % id(getcurrent()))
#     return data
#
#
# group = Group()
# res = group.map(talk, [1, 2, 3])
# print(type(res))
# print(res)


# from gevent.pool import Group
# from gevent import getcurrent
#
#
# def talk(data):
#     print('Size of group %s' % len(group))
#     print('Hello from Greenlet %s' % id(getcurrent()))
#     return data
#
#
# group = Group()
# res = group.imap(talk, [1, 2, 3])
#
# print(type(res))
# print(res)
#
# for i in res:
#     print(i)


# from gevent.pool import Group
# from gevent import getcurrent
#
#
# def talk(data):
#     print('Size of group %s' % len(group))
#     print('Hello from Greenlet %s' % id(getcurrent()))
#     return data
#
#
# group = Group()
# res = group.imap(talk, range(5), maxsize=2)
#
# print(type(res))
# print(res)
# for i in res:
#     print(i)


#


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
# res = pool.imap(hello_from, range(5))
# for i in res:
#     print(i)
import gevent
from gevent.pool import Pool
from gevent import monkey
monkey.patch_all()


class TestPool(object):
    def __init__(self, maxsize=2):
        self.pool = gevent.pool.Pool(maxsize)

    def run(self):
        for i in range(5):
            print("*******" + str(i))
            gworker = gevent.spawn(self._worker, i)
            self.pool.add(gworker)
            print('sizeof pool is %d' % (len(self.pool),))
            print('worker %d in? %r' % (i, gworker in self.pool))
        # add this statement to trap into the loop
        self.pool.join()
        print('All tasks done.')

    def _worker(self, pid):
        print('My pid is %d' % (pid,))
        gevent.sleep(1)
        print('%d has done.' % (pid,))


if __name__ == '__main__':
    test = TestPool()
    test.run()