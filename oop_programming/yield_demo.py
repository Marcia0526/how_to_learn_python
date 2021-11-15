# # Function returns a generator when it encounters 'yield'.
# def simple_generator():
#     x = 1
#     yield x
#     yield x + 1
#     yield x + 2
#
#
# for i in simple_generator():
#     print(i)
#
#
# for i in simple_generator():
#     print(i)

# generator_object = simple_generator()
# print(generator_object)
# for i in generator_object:
#     print(i)
#
# # Calling the generator again wont work.
# for i in generator_object:
#     print(i)


# class Iterable(object):
#     def __iter__(self):
#         x = 1
#         yield x
#         yield x + 1
#         yield x + 2
#
#
# iterable = Iterable()
#
# for i in iterable:  # iterator created here
#     print(i)
#
# for i in iterable:  # iterator again created here
#     print(i)


# def generator_func():
#   num = 1
#   print("First time execution of the function")
#   yield num
#   num = 10
#   print("Second time execution of the function")
#   yield num
#   num = 100
#   print("Third time execution of the function")
#   yield num
#
# obj = generator_func()
#
# print(next(obj))
# print(next(obj))
# # print(next(obj))


# my_list = [1, 3, 5]
# for i in my_list:
#     print(i)


#
# mygenerator = (x*x for x in range(3))
# for i in mygenerator:
#     print(i)
# for i in mygenerator:
#     print(i)


# def create_generator():
#     my_list = range(3)
#     for j in my_list:
#         yield j * j
#
#
# my_generator = create_generator()
# print(my_generator)
# for i in my_generator:
#     print(i)

# def simple_generator():
#     x = 1
#     yield x
#     yield x + 1
#     yield x + 2
#
#
# generator_object = simple_generator()
# print(generator_object)
# print(next(generator_object))
# print(next(generator_object))
# print(next(generator_object))
# print(next(generator_object))


# def generator_fun():
#     yield 1
#     yield 2
#     yield 3
#
#
# for value in generator_fun():
#     print(value)

def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
    print('a:', a, 'b:', b)
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(next(x))  # In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)