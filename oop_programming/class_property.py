# # class Student(object):
# #     def __init__(self, name, score):
# #         self.name = name
# #         self.score = score
# #
# #     def print_score(self):
# #         print('%s: %s' % (self.name, self.score))
# #
# #
# # bart = Student('hehe', 100)
# # bart.print_score()
# #
# # bart.score = 120
# # bart.print_score()
#
#
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')
# #
# bart = Student('hehe', 100)
# print(bart.get_name(), bart.get_score())
# bart.set_score(99)
# print(bart.get_score())
# bart.set_score(150)
# print(bart.get_score())


# class People(object):
#     pass
# people = People()
# print(type(people))
# print(type('abc'))
# print(type('abc') == str)

# print(isinstance([1, 2, 3], (list, tuple)))

# print(dir('abc'))
# print(len('abc'))
# print('abc'.__len__())

# class Myanimal(object):
#     ...
#
# class Mydog(object):
#     def __len__(self):
#         return 100
#
#
# my_animal = Myanimal()
# my_dog = Mydog()
# print(len(my_dog))
# print((len(my_animal)))

# class Mydemo(object):
#     def __init__(self, x=1):
#         self.x = x
#
#     def test(self):
#         print('hello world')
#
# my_demo = Mydemo()
# print(hasattr(my_demo, 'x'))
# print(getattr(my_demo, 'x'))
# setattr(my_demo, 'x', 2)
# setattr(my_demo, 'y', 3)
# print(getattr(my_demo, 'x'), getattr(my_demo, 'y'))
# print(getattr(my_demo, 'z', 404))


# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#
# s1 = Student('Bob')
# s1.score = 90
# print(s1.name, s1.score, s1.count)
#
# s2 = Student('Tim')
# print(s2.name, s2.count)
# print(s2.score)

# from types import MethodType
#
#
# class Student(object):
#     pass
#
#
# def set_age(self, age):
#     self.age = age
#
#
# def set_score(self, score):
#     self.score = score
#
# s1 = Student()
# s2 = Student()
# # ?????????s??????????????????
# s1.name = 'Tim'
# # ?????????s??????????????????
# s1.set_age = MethodType(set_age, s1)
# # ?????????????????????????????????
# Student.set_score = set_score
# s1.set_score(100)
# s2.set_score(90)
# print(s1.score, s2.score)
# s1.set_age(18)
# s2.set_age(19)
# print(s1.age, s2.age)

# class Student(object):
#     __slots__ = ('name', 'age') # ???tuple?????????????????????????????????
#
#
# s = Student()
# s.name = 'Tim'
# s.age = 18
# s.score = 100
# print(s.name, s.age, s.score)


# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# s = Student()
# s.score = 100
# print(s.score)
# s.score = 120
# print(s.score)


# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2015 - self._birth
#
#
# s = Student()
# s.birth = 100
# print(s.birth)
# print(s.age)


# class Animal(object):
#     pass
#
# class Eat(Animal):
#     pass
#
# class Runable(Animal):
#     pass
#
#
# class Dog(Eat, Runable):
#     pass
#
# from enum import Enum
#
# # ??????Month?????????????????????
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

# from enum import Enum, unique
#
# @unique
# class Weekday(Enum):
#     Sun = 0 # Sun???value????????????0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
#
# print(Weekday.Mon.value)
# print(Weekday['Tue'].value)
# print(Weekday(0))
# print(type(Weekday(0)))
#
# for name, member in Weekday.__members__.items():
#     print(name, '=>', member, '=>', member.value)
#


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     # def __str__(self):
#     #     return 'Student object (name:%s)' % self.name
#     # __repr__ = __str__
#
#
# s = Student('Tim')
# print(s)


# Python code showing use of iter() using OOPs

# class PowerTwo:
#     def __init__(self, maxi=0):
#         self.maxi = maxi
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n < self.maxi:
#             self.n += 1
#             return 2 ** self.n
#         else:
#             raise StopIteration
#
#
# pt = PowerTwo(5)
#
# # based on iteration
# pt_iteration = iter(pt)
# try:
#     while True:
#         print(next(pt_iteration))
# except:
#     print('stop iteration')
#
# # for loop
# for item in pt:
#     print(item)
#

# class PositiveDescriptor:
#     def __init__(self, name, value):
#         self.name = name
#         self._value = value
#
#     def __get__(self, instance, owner):
#         print('call __get__ method')
#         print('instance:{}'.format(instance))
#         print('owner:{}'.format(owner))
#         return self._value
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('cannot be negative')
#         else:
#             print('call __set__ method')
#             print('instance:{}'.format(instance))
#             print('value:{}'.format(value))
#             self._value = value
#
#     def __delete__(self, instance):
#         print('call __delete__ method')
#         print('instance:{}'.format(instance))
#
#
# class Apple(object):
#     price = PositiveDescriptor('name_price', 0)
#
#     def __init__(self):
#         self.price = 10
#
#
# apple = Apple()
# apple.price
# # apple.price = -10
# del apple.price


# class mproperty(object):
#     def __init__(self, fget, fset=None, fdel=None):
#         self._fget = fget
#         self._fset = fset
#         self._fdel = fdel
#
#     def __get__(self, obj, klass):
#         return self._fget(obj)
#
#
#     def __set__(self, obj, val):
#         if not hasattr(self._fset, '__call__'):
#             raise AttributeError("Readonly attribute!")
#         self._fset(obj, val)
#
#
#     def __delete__(self, obj):
#         if not hasattr(self._fdel, '__call__'):
#             raise AttributeError("Can't delete the attribute!")
#         self._fdel(obj)
#
#
#     def setter(self, fset):
#         self._fset = fset
#         return self
#
#
#     def deleter(self, fdel):
#         self._fdel = fdel
#         return self
#
#
# class Apple(object):
#
#     def __init__(self, price=0):
#         self._price = price
#
#     @mproperty
#     def price(self):
#         return self._price
#
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price must be greater than 0")
#         self._price = value
#
#     @price.deleter
#     def price(self):
#         print("delete price")
#
#
# apple = Apple(10)
# print(apple.price)

#
# class Foo:
#     def __init__(self):
#         print("??????init??????")
#
#     def __new__(cls, *args, **kwargs):
#         print('??????new??????')
#         r = super(Foo, cls).__new__(cls)
#         return r
#
#
# obj = Foo()
# print(obj)

# class Test(object):
#     def __init__(self):
#         print("Hello World !")
#
#     def __del__(self):
#         print("Goodbye World QAQ")
#
# T = Test()
# del T


# class Yeah(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __delattr__(self, name):
#         print('invoke __delattr__', name)
#
#     # def __getattr__(self, item):
#     #     print('__getattr__ ', item)
#     #     try:
#     #         return super(Yeah, self).__getattr__(item)
#     #     except AttributeError as attr:
#     #         print('__getattr__', attr)
#     #
#     def __getattribute__(self, item):
#         print('__getattribute__ ', item)
#         try:
#             return super(Yeah, self).__getattribute__(item)
#         except AttributeError as attr:
#             print('__getattribute__', attr)
#
#
# y1 = Yeah('yes')
# # y1.score = 100
# # y1.name
# # y1.value
# # y1.name
# del y1.name
# # y1.name


# class A:
#     num = 10
#
#     def fun(self):
#         print('Hello World')
#
#
# #  determine whether there is any in a fun property or method
# if hasattr(A, 'fun'):
#     #  get the memory address of the fun method
#     f = getattr(A, 'fun')
#     #  execution a fun the method of
#     f(' ')
#
# #  add attributes to a buf
# setattr(A, 'buf', [1, 2, 3])
# print(A.buf)
#
# #  delete the attribute num from the class
# delattr(A, 'num')
# print(A.num)


# class A:
#     num = 10
#     def fun(self):
#         print('Hello World')
#
#
# obj = A()
# #  determine whether there is any in the object obj fun method
# if hasattr(obj, 'fun'):
#     #  get the memory address of the fun method in the object
#     f = getattr(obj, 'fun')
#     #  executing obj fun method
#     f()
#
# #  add properties to object obj buf
# setattr(obj, 'buf', [1, 2, 3])
# print(obj.buf)
#
# #  delete attributes in obj buf
# delattr(obj, 'buf')
# #  delete the attribute of class a num
# delattr(obj, 'num')


# import sys
#
#
# class A:
#     num = 10
#
#     def fun(self):
#         print('Hello World')
#
#
# def f():
#     print('reflect the current module')
#
#
# #  get the current module
# current_module = sys.modules[__name__]
#
# #  get class a under the current module
# if hasattr(current_module, 'A'):
#     obj_A = getattr(current_module, 'A')
#     obj_A.fun('')
#
# #  get the function f under the current module
# if hasattr(current_module, 'f'):
#     obj_f = getattr(current_module, 'f')
#     obj_f()


# x = 5
# s = "geeksforgeeks"
# y = [1,2,3]
# print(type(x))
# print(type(s))
# print(type(y))

# Python code for type() with a name,
# bases and dict parameter

# o1 = type('X', (object,), dict(a='foo', b=12))
# print(o1)
# print(type(o1))
# print(vars(o1))
#
# print('')
#
# class test:
#     c = '001'
# o2 = type('Y', (test,), dict(a='Foo', b=12))
# print(type(o2))
# print(vars(o2))

# class Test:
#     a = 5
#
#
# TestInstance = Test()
#
# print(isinstance(TestInstance, Test))
# print(isinstance(TestInstance, (list, tuple)))
# print(isinstance(TestInstance, (list, tuple, Test)))

# x = 5
#
#
# def testFunction():
#     print("Test")
#
#
# y = testFunction
#
# if (callable(x)):
#     print("x is callable")
# else:
#     print("x is not callable")
#
# if (callable(y)):
#     print("y is callable")
# else:
#     print("y is not callable")

# class Foo1:
#   def __call__(self):
#     print('Print Something')
#
#
# print(callable(Foo1))


# number = [1,2,3]
# print(dir(number))
#
# characters = ["a", "b"]
# print(dir(number))

# class Employee:
#     salary = 25000
#     company_name= "geeksforgeeks"
#
# employee = Employee()
# print('The salary is:', getattr(employee, "salary"))
# print('The salary is:', employee.salary)

# class Example:
#     def __init__(self):
#         print("Instance Created")
#
#     # Defining __call__ method
#     def __call__(self):
#         print("Instance is called via special method")
#
#
# # Instance created
# e = Example()
#
# # __call__ method will be called
# e()


# class Product:
#     def __init__(self):
#         print("Instance Created")
#
#     # Defining __call__ method
#     def __call__(self, a, b):
#         print(a * b)
#
#
# # Instance created
# ans = Product()


# ???????????????????????????
# class MyOpen(object):
#
#     def __init__(self, file_name):
#         """???????????????"""
#         self.file_name = file_name
#         self.file_handler = None
#         return
#
#     def __enter__(self):
#         """enter???????????????file_handler"""
#         print("enter:", self.file_name)
#         self.file_handler = open(self.file_name, "r")
#         return self.file_handler
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """exit??????????????????????????????True"""
#         print("exit:", exc_type, exc_val, exc_tb)
#         if self.file_handler:
#             self.file_handler.close()
#         return True
#
# # ????????????
# with MyOpen("test.py") as file_in:
#     for line in file_in:
#         print(line)
#         raise ZeroDivisionError


# class Supermarket:
#
#     # Function __dir()___ which list all
#     # the base attributes to be used.
#     def __dir__(self):
#         return ['customer_name', 'product',
#                 'quantity', 'price', 'date']
#
#
# # user-defined object of class supermarket
# my_cart = Supermarket()
#
# # listing out the dir() method
# print(dir(my_cart))

# class Animals is declared
# class Animals:
#
#     # constructor
#     def __init__(self):
#         # keys are initialized with
#         # their respective values
#         self.lion = 'carnivore'
#         self.dog = 'omnivore'
#         self.giraffe = 'herbivore'
#
#     def printit(self):
#         print("Dictionary from the object fields\
# 		belonging to the class Animals:")
#
#
# # object animal of class Animals
# animal = Animals()
#
# # calling printit method
# # animal.printit()
# # calling attribute __dict__ on animal
# # object and printing it
# print(animal.__dict__)
# print(vars(animal))
# print(Animals.__dict__)
# print(vars(Animals))

# class test:
#     def say(self):
#         pass
#
# print(test.say)
# print(test().say)

# class test:
#     math = 100
#     # ?????????????????????????????????
#     def __init__(self):
#         self.Chinese = 90
#         self.English = 80
#     # ????????????
#     def say(self):
#         print('????????????????????????{}'.format(self.Chinese))
#
# # ?????????
# A = test()
# # ??????????????????
# A.say()
# print(A.say)
# # ????????????self
# test.say(A)

# class test:
#     math = 100
#     # ?????????????????????????????????
#     def __init__(self):
#         self.Chinese = 90
#         self.English = 80
#
#     @staticmethod
#     def say():
#         print('?????????????????????90')
#
# # ???.?????????
# test.say()
# print(test.say)
# # ?????????
# A = test()
# A.say()
# print(A.say)

# class Foo():
#     def getter(self) -> object:
#         print("accessing the attribute to get the value")
#         return 42
#
#     def setter(self, value) -> None:
#         print("accessing the attribute to set the value")
#         raise AttributeError("Cannot change the value")
#
#     attribute1 = property(getter, setter)
#
#
# my_foo_object = Foo()
# x = my_foo_object.attribute1
# print(x)

# class test:
#     math = 100
#     # ?????????????????????????????????
#     def __init__(self):
#         self.Chinese = 90
#         self.English = 80
#     @classmethod
#     def say(cls):
#         print('????????????????????????{}'.format(cls.math))
#
# # ???.?????????
# test.say()
# print(test.say)
# # ???????????????
# test().say()
# print(test().say)


# class mstaticmethod(object):
#
#     def __init__(self, func):
#         print('enter into staticmethod __init__')
#         self._func = func
#
#     def __get__(self, obj, klass=None):
#         print('enter into __get__', self, obj)
#         return self._func

# @property
# def __func__(self):
#     print('enter into property __func__')
#     return self._func


# class Apple(object):
#
#     def __init__(self, price=0):
#         self._price = price
#
#     @mstaticmethod
#     def kg2jin(weight):
#         print('enter into kg2jin')
#         # ?????????????????????
#         return weight * 2
#
#
# instan = Apple(2)
# print(instan.kg2jin(5))


# def outer(func):
#     def inner():
#         print("?????????????????????")
#     return inner
#
# def foo():
#     print("?????????????????????")
#
# outer(foo)
# outer(foo())

# def outer(func):
#     def inner():
#         print("???????????????")
#         result = func()
#         print("??????????????????")
#         return result
#     return inner
#
# @outer
# def f1():
#     print("????????????1????????????......")
#
#
# f1()


# def outer1(func1):
#     def inner1(*args, **kwargs):
#         print("???????????????")
#         result = func1(*args, **kwargs)
#         print("??????????????????")
#         return result
#
#     return inner1
#
#
# def outer2(func2):
#     def inner2(*args, **kwargs):
#         print("???????????????????????????")
#         result = func2(*args, **kwargs)
#         print("???????????????????????????")
#         return result
#
#     return inner2
#
#
# @outer1
# @outer2
# def f1(name, age):
#     print("%s ????????????????????????1????????????......" % name)
#
#
# f1("jack", 18)

# ????????????
# def  auth(request,kargs):
#     print("1. ???????????????")
# # ????????????
# def log(request,kargs):
#     print("3. ??????????????????!")
# # ???????????????????????????????????????????????????????????????????????????????????????
# def Filter(auth_func,log_func):
#     # ??????????????????f1??????????????????????????????main_fuc????????????
#     def outer(main_func):
#         # ??????????????????auth???log???????????????????????????????????????
#         def wrapper(request,kargs):
#             # ??????????????????????????????????????????????????????????????????????????????
#             before_result = auth(request,kargs)
#             if(before_result != None):
#                 return before_result;
#
#             main_result = main_func(request,kargs)
#             if(main_result != None):
#                 return main_result;
#
#             after_result = log(request,kargs)
#             if(after_result != None):
#                 return after_result;
#
#         return wrapper
#     return outer
# # ???????????????????????????????????????????????????????????????????????????filter??????
# # ?????????filter???????????????????????????????????????????????????????????????????????????
# # ???????????????Filter(auth,log) = outer , @Filter(auth,log) =  @outer
# @Filter(auth,log)
# def f1(name,age):
#
#     print("2. %s ????????????????????????1????????????......"%name)
#
# # ????????????
# f1("jack",18)

# class Test():
#     def __init__(self, func):
#         print("1. ----?????????----")
#         print("2. func name is %s"%func.__name__)
#         self.__func = func
#
#     def __call__(self):
#         print("3. ----?????????????????????----")
#         self.__func()
#         print("5. ----????????????????????????----")
#
# @Test
# def demo():
#     print("4. ----demo----")
#
#
# demo()

# class Decrator(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __get__(self, instance, owner):
#         '''
#         instance:???????????????sum??????self
#         owner?????????????????????Test???
#
#         '''
#         print('1. ????????????get??????')
#         return self.func(instance)  # instance??????Test??????self
#
#
# class Test(object):
#     def __init__(self):
#         self.result = 0
#
#     @Decrator
#     def sum(self):
#         print('2. There is the Func in the Class !')
#         return 'succeed'
#
#
# t = Test()
# print(t.sum)


# def wrap_func(cls):
#     def inner(value):
#         print('1. class name:', cls.__name__)
#         return cls(value)
#     return inner
#
#
# @wrap_func
# class Foo:
#     def __init__(self, a):
#         self.a = a
#
#     def fun(self):
#         print('2. self.a=', self.a)
#
#
# m = Foo('student')
# m.fun()

# class Decorate:
#     def __init__(self, cls):
#         self._cls = cls
#
#     def __call__(self, var):
#         print('1. class name:', self._cls.__name__)
#         return self._cls(var)
#
#
# @Decorate
# class Demo:
#     def __init__(self, a):
#         self.a = a
#
#     def fun(self):
#         print('2. demo value:', self.a)
#
#
# demo = Demo('student')
# demo.fun()


# class Student:
#     def getter(self) -> object:
#         print("begin get validation...")
#         return 42
#     def setter(self, value) -> None:
#         print("begin set validation...")
#         if (value > 100) | (value < 0):
#             raise AttributeError("score can only between 0 and 100")
#         else:
#             print('validated successfully and score is', value)
#
#     score = property(getter, setter)
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
# student = Student('Tim', 99)
# student.score
#
# print('---------------------')
# student_new = Student('Tim', 101)

class ScoreValidator:
    def __init__(self, func):
        self._func = func

    def __get__(self, instance, owner):
        print('instance:', instance)
        print('owner:', owner)

        def inner():
            print('I am %s with score: %d'%(instance.name, instance.score))
            print('begin validating score...')
            if instance.score < 80:
                raise AttributeError("your score is not up to standard and cannot go to play now")
            else:
                self._func(instance)
        return inner


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @ScoreValidator
    def have_fun(self):
        print('Great! please have fun!')


tim = Student('Tim', 99)
tim.have_fun()
jak = Student('Jak', 60)
jak.have_fun()

