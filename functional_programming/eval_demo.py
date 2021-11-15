def test():
    # age = 18
    print(eval("{'name':'linux','age':age}", globals(), locals()))

    print(eval("{'name':'linux','age':age}"))

    print(eval("{'name':'linux','age':age}", {"age": 1822}))

    print(eval("{'name':'linux','age':age}", {"age": 1822}, {"age": 1823}))

    print(eval("{'name':linux,'age':age}", {"age": 1822, "linux": "java"}, {"age": 1823}))


age = 19

test()
# if __name__ == "__main__":
#     test1()