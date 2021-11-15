import gevent


def eat(name):
    print('%s start task' % name)
    gevent.sleep(2)
    print('%s end task' % name)
    return name + " finished callback"


def play(name):
    print('%s start task' % name)
    gevent.sleep(1)
    print('%s end task' % name)
    return name + " finished callback"


def callback(greenlet):
    print("callback successfully: " + greenlet.value)


g1 = gevent.spawn(eat, 'marcia')
g1.link(callback)
g2 = gevent.spawn(play, name='joe')
g2.link(callback)
gevent.joinall([g1, g2])
print('主')

# import gevent
# from gevent import Greenlet
#
#
# def callback_func():
#     print("callback successfully")
#
#
# class MyGreenlet(Greenlet):
#     def __init__(self, timeout, msg):
#         Greenlet.__init__(self)
#         self.timeout = timeout
#         self.msg = msg
#
#     def _run(self):
#         print("I'm from subclass of Greenlet and want to say: %s" % (self.msg,))
#         gevent.sleep(self.timeout)
#         print("done after sleep %s" % self.timeout)
#
#
# greenlet1 = MyGreenlet(2, 'hello')
# greenlet2 = MyGreenlet(1, 'world')
# greenlet1.start()
# greenlet2.start()
# greenlet1.rawlink(callback_func())
#
# gevent.joinall([greenlet1, greenlet2])
# print("main")
#
