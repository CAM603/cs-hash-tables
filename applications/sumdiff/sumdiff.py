"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))


# for num in q:
#     print(f(num))
# f(1) -> 10
# f(3) -> 18
# f(4) -> 22
# f(7) -> 34
# f(12) -> 54

# Choose 4 numbers from q and call them a, b, c, d
# a = 1
# b = 3
# c = 4
# d = 7
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


# f(a) + f(b) = f(c) - f(d)
def add(a, b):
    return f(a) + f(b)


def subtract(c, d):
    return f(c) - f(d)

# add(a, b) = subtract(c, d)


# Initialize cache
add_cache = {}
sub_cache = {}

# Build lookup table


def generate_cache(a_set):
    for a in a_set:  # loop through tuple

        for b in a_set:
            # grab from a_set
            add_key = (a, b)
            add_result = add(a, b)

            # add to cache if not there
            if not add_key in add_cache.keys():
                add_cache[add_key] = add_result

            sub_key = (a, b)
            sub_result = subtract(a, b)

            # add to cache if not there
            if not sub_key in sub_cache.keys():
                sub_cache[sub_key] = sub_result

            # do something


generate_cache(q)

# I have a collection of all possible add and subtract results for the numbers in q
# I need to find which ones match

add_list = list(add_cache.items())
sub_list = list(sub_cache.items())

equal_cache = {}

# for i in range(len(add_list)):
#     for j in range(len(sub_list)):
#         if add_list[i][1] == sub_list[j][1]:
#             key = add_list[i][0]
#             value = sub_list[j][0]
#             equal_cache[key] = value

# equal_list = list(equal_cache.items())

# for item in equal_list:
#     print(
#         f'f({item[0][0]}) + f({item[0][1]}) = f({item[1][0]}) - f({item[1][1]})')

for i in range(len(add_list)):
    for j in range(len(sub_list)):
        if add_list[i][1] == sub_list[j][1]:
            key = add_list[i]
            value = sub_list[j]
            equal_cache[key] = value

equal_list = list(equal_cache.items())

for item in equal_list:
    # print(item)
    # print(item[0][0][1])
    # print(item[1][0][0])
    # print(item[1][0][1])

    print(
        f'f({item[0][0][0]}) + f({item[0][0][1]}) = f({item[1][0][0]}) - f({item[1][0][1]})', end="     ")
    print(
        f'{f(item[0][0][0])} + {f(item[0][0][1])} = {f(item[1][0][0])} - {f(item[1][0][1])}')
