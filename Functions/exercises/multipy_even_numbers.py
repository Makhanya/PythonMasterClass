'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''


def multiply_even_numbers(list):
    sum = 1
    for x in list:
        if x % 2 == 0:
            sum = sum * x
    return sum


print(multiply_even_numbers([2, 3, 4, 5, 6]))  # 48
