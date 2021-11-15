# import asyncio
#
# @asyncio.coroutine
# def compute(x, y):
#     print("Compute %s + %s ..." % (x, y))
#     yield from asyncio.sleep(1.0)
#     return x + y
#
# @asyncio.coroutine
# def print_sum(x, y):
#     result = yield from compute(x, y)
#     print("%s + %s = %s" % (x, y, result))
#
# loop = asyncio.get_event_loop()
# print("start")
# # 中断调用，直到协程执行结束
# loop.run_until_complete(print_sum(1, 2))
# print("end")
# loop.close()


def jumping_range(up_to):
    """Generator for the sequence of integers from 0 to up_to, exclusive.

    Sending a value into the generator will shift the sequence by that amount.
    """
    index = 0
    while index < up_to:
        jump = yield index
        if jump is None:
            jump = 1
        index += jump


if __name__ == '__main__':
    iterator = jumping_range(5)
    print(next(iterator))  # 0
    print(iterator.send(2))  # 2
    print(next(iterator))  # 3
    print(iterator.send(-1))  # 2
    for x in iterator:
        print(x)  # 3, 4