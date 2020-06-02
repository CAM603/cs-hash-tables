my_list = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]


def divisible_by_three(arr):
    new_arr = [num for num in arr if num % 3 == 0]

    # for num in arr:
    #     if num % 3 == 0:
    #         new_arr.append(num)

    return new_arr


print(divisible_by_three(my_list))
