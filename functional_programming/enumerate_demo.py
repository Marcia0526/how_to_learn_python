l_enum = ["eat", "sleep", "repeat"]

print(list(enumerate(l_enum)))
print('---------------')
# printing the tuples in object directly
for ele in enumerate(l_enum):
    print(ele)
print('---------------')
# changing index and printing separately
for count, ele in enumerate(l_enum, 100):
    print(count, ele)
print('---------------')
# getting desired output from tuple
for count, ele in enumerate(l_enum):
    print(count)
    print(ele)