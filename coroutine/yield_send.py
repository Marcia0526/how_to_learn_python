import random


def cf():
    while True:
        val = yield
        print(val)


def pf(generator):
    while True:
        val = random.randint(1, 10)
        generator.send(val)
        yield


if __name__ == '__main__':
    c = cf()
    c.send(None)
    p = pf(c)
    # pf(c)

    for wow in range(10):
        next(p)