# def sum_all_nums(num1, num2, num3):
#     return num1+num2+num3

# print(sum_all_nums(4, 6, 9))

# def sum_all_nums(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total


# print(sum_all_nums(4, 56, 7, 8, 9, 0))

# print(sum_all_nums(3, 5))

#   Another Example
def ensure_correct_info(*args):
    if "Makhanya" in args and "Mzili" in args:
        return "Welcome back Makhanya"
    return "Not sure who you are..."


print(ensure_correct_info())  # Not sure who you are...)
print(ensure_correct_info(1, True, "Mzili", "Makhanya"))
