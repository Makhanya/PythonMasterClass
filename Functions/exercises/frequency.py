'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''


def frequency(value, key):
    return value.count(key)


print(frequency([1, 2, 3, 4, 4, 4], 4))  # 3
print(frequency([True, False, True, True], False))  # 1
