#   The syntax
#       {_:_for_ in _}
#
#       our first example
#           members = dict(first=1,second = 2, third = 3)
#           squared_numbers = {key:value ** 2 for key,value in numbers.items()}
#           print(squared_numbers) #{first':1, 'second':4, 'third':9}
#

# members = dict(first=1, second=2, third=3, forth=4)
# print(members)
# squared_members = {x: (y**2) for x, y in members.items()}
# print(squared_members)

#   More examples

# print({num: num ** 2 for num in [1, 2, 3, 4, 5, 6, 7]})
# str1 = "ABC"
# str2 = "123"
# comb = {str1[i]: str2[i]for i in range(0, len(str1))}
# print(comb)

# instructor = {'name': 'makhanya', ' city': 'Bisho',
#               'color': 'purple'}
# print(instructor)
# print({x.upper(): y.upper() for x, y in instructor.items()})

#       Conditional logig with dictionaries
#           num_list = [1,2,3,4]
#           {num:("even" if num % 2 == 0 else "odd") for num in num_list}
#           {1:'odd', 2: 'even', 3:'odd', 4:'even'}

num_list = [1, 2, 3, 4]
print({num: ('even' if num % 2 == 0 else 'odd') for num in range(1, 10)})
