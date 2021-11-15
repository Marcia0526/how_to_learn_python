# x = [2, 8, 1, 4, 6, 3, 7]
# print("\nOriginal list not modified :"),
# print(x)
#
# print("\nSorted List returned :"),
# print(sorted(x))
#
# print("\nReverse sort :"),
# print(sorted(x, reverse=True))

# L = ["cccc", "b", "dd", "aaa"]
#
# print("Normal sort :", sorted(L))
#
# print("Sort with len :", sorted(L, key=len))


def func(x):
    return x % 7


L = [15, 3, 11, 7]
print("Normal sort :", sorted(L))
print("Sorted with key:", sorted(L, key=func))