from asyncio import sleep

import gevent
from gevent.pool import Pool


def talk(data):
    print('Size of group %s' % len(pool))
    gevent.sleep(1)
    print('-------g%s' % data)
    return data

pool = Pool(2)
res = pool.imap(talk, range(5))


for i in res:
    print(i)



# from gevent.pool import Pool
#
# def talk(data):
#     print('Size of group %s' % len(group))
#     print('Hello from Greenlet %s' % data)
#     return data
#
#
# group = Pool(2)
# res = group.imap(talk, range(5))
#
# print(type(res))
# print(res)
# for i in res:
#     print(i)