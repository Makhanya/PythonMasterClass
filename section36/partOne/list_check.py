# list_check
# Write a function called list_check,
# which accepts a list and returns True
# if each value in the list is a list.
# Otherwise the function should return False.

def list_check(l):
    print(all(type(x) == list for x in l))


list_check([[], [1], [2, 3], (1, 2)])  # False
list_check([1, True, [], [1], [2, 3]])  # False
list_check([[], [1], [2, 3]])  # True
