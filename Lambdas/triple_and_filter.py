'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''


# def triple_and_filter(l):
#     return list(x*3 for x in l if x % 4 == 0)
def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))


print(triple_and_filter([1, 2, 3, 4]))  # [12]
print(triple_and_filter([6, 8, 10, 12]))  # [24,36]
