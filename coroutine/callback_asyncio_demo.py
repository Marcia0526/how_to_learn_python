# 绑定回调函数
import asyncio
import time


async def do_some_work(x):  # async关键字定义一个协程
    print('Waiting:', x)
    return 'Done after {}s'.format(x)  # 返回值


def callback(future):  # 定义一个回调函数，最后一个参数是future对象，如果这里有多个参数，下方通过偏函数导入
    print('Callback: ', future.result())  # 返回future的结果


coroutine = do_some_work(2)  # 协程的调用不会直接执行，而是返回一个协程对象

loop = asyncio.get_event_loop()  # 创建一个事件循环

task = loop.create_task(coroutine)  # 创建task，此时的task尚未加入事件循环，状态为pending
task.add_done_callback(callback)  # 绑定回调函数，在task执行完毕的时候获取执行的结果
loop.run_until_complete(task)  # run_until_complete将task注册到事件循环，并启动事件循环。
# task执行完后，状态为finished
