'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''


def capitalize(string):
    return string[0].upper() + string[1:]


print(capitalize("tim"))  # "Tim"
print(capitalize("matt"))  # "Matt"
