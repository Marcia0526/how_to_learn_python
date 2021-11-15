# Python program to illustrate
# nested functions
# def outerFunction(text):
#     text = text
#
#     def innerFunction():
#         print(text)
#
#     innerFunction()
#
#
# if __name__ == '__main__':
#     outerFunction('Hey!')


# def outerFunction(text):
#     text = text
#
#     def innerFunction():
#         print(text)
#
#     # Note we are returning function
#     # WITHOUT parenthesis
#     return innerFunction
#
#
# if __name__ == '__main__':
#     myFunction = outerFunction('Hey!')
#     myFunction()


# list = []
# for i in range(0, 3):
#     def mak_func(i):
#         def func(x):
#             return x*i
#         return func
#     list.append(mak_func(i))
#
# for f_item in list:
#     print(f_item(2))


def func_1(arg, *args):
    print(arg, args)


func_1('你好', 'hi','marcia','!')


def func_2(arg, **args):
    print(arg, args)


func_2('关键字参数', a=1, b=2, c=1)

