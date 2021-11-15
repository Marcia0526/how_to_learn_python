import functools

sequence = [1, 2, 5, 4, 3]
max = functools.reduce(lambda a, b: a if a > b else b, sequence)
print(max)

