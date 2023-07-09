#   Scope
#       Where our variables can be accessed
#       Variables created in functions are scoped in that function!

# instructor = "Makhanya"


# def say_hello():
#     return f'Hello {instructor}'


# say_hello()


def say_hello():
    instructor = "Makhanya"
    return f'Hello {instructor}'


say_hello()
print(say_hello())
