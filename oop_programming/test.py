# L = []
# for i in range(1, 11):
#     L.append(i*i)
# print(L)
#
# print([i*i for i in range(1, 11)])
# print([i*i for i in range(1, 11) if i % 2 == 0])
#
#
# # L = []for x in range(1, 11): L.append(x * x)print( [m + n for m in 'ABC' for n in 'XYZ'])
#
#
#
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# print([k + '=' + v for k, v in d.items()])
#
#
# train_dict = {1: ['a', 'b', 'c'],
#               2: ['d', 'e', 'f'],
#               3: ['a', 'c', 'd']}
# all_test = []
# for i in train_dict.keys():
#     for ipc in train_dict[i]:
#         if ipc in all_test:
#             continue
#         else:
#             all_test.append(ipc)
# print(all_test)
#
#
# print([ipc for i in train_dict.keys() for ipc in train_dict[i]])
# print({ipc for i in train_dict.keys() for ipc in train_dict[i]})
#
# print([m + n for m in 'ABC' for n in 'XYZ'])
#
#
# print([x if x % 2 == 0 else -x for x in range(1, 11)])
# print([x for x in range(1, 11) if x % 2 == 0])


s = ["a111", "b222", "c333", "d444", "e555"]
for word in s:
    if word.startswith("z"):
        found = True
        print("发现以字母z开头的项")
        break
else:
    print("没有发现以字母z开头的项")