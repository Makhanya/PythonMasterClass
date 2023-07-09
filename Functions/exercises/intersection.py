# intersection
# Write a function called intersection. This function should
# accept two lists and return a list with the values that are in both input lists.


# flesh out intersection pleaseeeee
def intersection(values, values1):
    list = [x for x in values if x in values1]
    return list


print(intersection([1, 2, 3], [2, 3, 4]))  # [2,3]
print(intersection(['a', 'b', 'z'], ['x', 'y', 'z']))  # ['z']
