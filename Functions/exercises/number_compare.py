'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''


def number_compare(num1, num2):
    if num1 == num2:
        return "Numbers are equal"
    elif num1 > num2:
        return "First number is greater"
    else:
        return "Second number is greater"


print(number_compare(14, 7*2))
