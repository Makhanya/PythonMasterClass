# #   Dictionary Methods
#         working with dictionaries is very
#         common - there are quite a few things
#         we can do!

#   Clear
#       Clears the dictionary

# d = dict(a=1, b=2, c=3)
# d.clear()
# d  # {}
# print(d)


#   Copy
#       Copy the dictionary but have different address in memory

# d = dict(a=1, b=2, c=3)
# c = d.copy()
# print(c)
# print(f"c is d = {c is d}")

#   fromkeys
#       Create key-value pairs from comma separated values:

# {}.fromkeys("a", "b")  # {'a':'b"}
# {}.fromkeys(["email"], 'unknown')  # {'email':'unknown'}
# {}.fromkeys("a", [1, 2, 3, 4, 5])  # {'a':[1,2,3,4,5]}

#   Get
#       Retrieves a key in an object and return None
#       instead of a KeyError if the Key does not exits

# d = dict(a=1, b=3, c=4)
# d['a']  # 1
# d.get('a')  # 1
# d['b']  # 3
# d.get('b')  # 3
# d['no_key']  # KeyError
# d.get('no_key')  # None

# instructor = {
#     "name": "Colt",
#     "owns_dog": True,
#     "num_courses": 4,
#     "favorite_language": "Python",
#     "is_hilarious": False,
#     44: "my favorite number!"
# }

# result = instructor.get('email')
# print(result)

# #   Pop
#         Takes a single argument corresponding to a key and removes that key-value pair from the dictionary.
#         Returns the value corresponding to the key that was removed

# d = dict(a=1, b=2, c=3)
# d.pop()  # TypeError: pop expected at least 1 arguments, got 0
# d.pop('a')  # 1
# d  # {'c':3,'b':2}
# d.pop('e')  # KeyError

# print(instructor.pop("owns_dog"))

# #   popitem
# # Removes a last key in a dictionary

# d = dict(a=1, b=2, c=3, d=5, e=4)
# print(d.popitem())
# print(d.popitem('a'))  # TypeError: popitem() takes no arguments (1 given)

#   Update
#       Update keys and values in a dictionary with another set of key values pairs
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}

second.update(first)
# second()  # {'a':1,'b':2,'c':3,'d':4,'e':5}

# lets overwrite an axisting key
second['a'] = "AMAZING"

# if we update again
second.update(first)  # {'a':1,'b':2,'c':3,'d':4,'e':5}

# the update overrides our values
# second()  # {'a':1,'b':2,'c':3,'d':4,'e':5}

person = {'city': "Bisho"}
person.update(first)

print(person)
