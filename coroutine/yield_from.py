# from itertools import chain
#
#
# def generator2():
#     for i in range(10):
#         yield i
#
#
# def generator3():
#     for j in range(10, 20):
#         yield j
#
#
# # def generator():
# #     yield from generator2()
# #     yield from generator3()
#
# def generator():
#     for v in chain(generator2(), generator3()):
#         yield v
#
#
# g = generator()
# for i in range(30):
#     print(next(g))


# 子生成器
def test(n):
    i = 0
    while i < n:
        yield i
        i += 1


# 委派生成器
def test_yield_from(n):
    print("test_yield_from start")
    yield from test(n)
    print("test_yield_from doing")
    yield from test(n)
    print("test_yield_from end")


for i in test_yield_from(3):
    print(i)