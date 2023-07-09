'''
last_element([1,2,3]) # 3
last_element([]) # None
'''


def last_element(lit):
    if lit:
        return lit[-1]
    return None


print(last_element([1, 2, 3, 4, 5, 6, 7, 8]))
