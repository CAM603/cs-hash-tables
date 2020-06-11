# Your code here
import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


cache = {}


def lookup_table():
    for x in range(2, 14):
        for y in range(3, 6):
            v = math.pow(x, y)
            v = math.factorial(v)
            v //= (x + y)
            v %= 982451653
            cache[(x, y)] = v


lookup_table()


def slowfun(x, y):

    if (x, y) in cache:
        return cache[(x, y)]

    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    cache[(x, y)] = v
    return cache[(x, y)]

# def slowfun(x, y):
#     """
#     Rewrite slowfun_too_slow() in here so that the program produces the same
#     output, but completes quickly instead of taking ages to run.
#     """
#     if (x, y) in cache:
#         return cache[(x, y)]

#     v = math.pow(x, y)
#     v = math.factorial(v)
#     v //= (x + y)
#     v %= 982451653

#     cache[(x, y)] = v
#     return v


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
