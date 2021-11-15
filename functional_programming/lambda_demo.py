
lambda_cube = lambda y: y * y * y
print(lambda_cube(5))
print('-----------------')

# 1. lambda function with list comprehension
tables = [lambda x=x: x*10 for x in range(1, 11)]
for table in tables:
    print(table())
print('-----------------')

# 2. lambda function with if else
Max = lambda a, b: a if (a > b) else b
print(Max(1, 2))
print('-----------------')

# 3. lambda function with multiple statements
List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]
sort_list = lambda x: (sorted(i) for i in x)
print(list(sort_list(List)))
second_largest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = second_largest(List, sort_list)
# res = lambda List, sort_list: [y[len(y) - 2] for y in sort_list(List)]
print(res)
print('-----------------')


# 4. lambda function with filter
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))
print(adults)
print('-----------------')


# 5. lambda function with map
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x * 2, li))
print(final_list)
animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
print(uppered_animals)
print('-----------------')

# 6. lambda function with reduce
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)
lis = [1, 3, 5, 6, 2, ]
print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, lis))
print('-----------------')
