class Animal(object):
    def run(self):
        print('Animal is running...')


class Cat(Animal):
    pass


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

#
# cat = Cat()
# cat.run()
# dog = Dog()
# dog.run()
# dog.eat()

# b = Animal() # b是Animal类型
# c = Dog() # c是Dog类型
# print(isinstance(b, Dog) and isinstance(b, Animal))
# print(isinstance(c, Dog) and isinstance(c, Dog))
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


def run_twice(animal):
    animal.run()
    animal.run()


animal = Animal()
cat = Cat()
dog = Dog()
tortoise = Tortoise()
run_twice(animal)
run_twice(cat)
run_twice(dog)
run_twice(tortoise)
