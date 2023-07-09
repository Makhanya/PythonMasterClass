# def exponent(num, power=2):
#     return num ** power


# print(exponent(2, 3))  # 8
# print(exponent(3))  # 9
# print(exponent(7))  # 49

# #   Default Parameters - Example


def show_information(first_name="Makhanya", is_instructor=False):
    if first_name == "Makhanya" and is_instructor:
        return "Welcome back instructor Makhanya"
    elif first_name == "Makhanya":
        return "I really thought you were an instructor..."
    return f"Hello {first_name}!"


# print(show_information())  # "I really thought you were an instructor..."
# print(show_information(is_instructor=True))  # "Welcom back instuctor Makhanya"
# print(show_information("Molly"))  # Hello Molly

#   Why have Default Params
#       Allows you to be more defensive
#       Avoids errors with incorrect parameters
#       More readable examples!

#   Keyword arguments


def full_name(first, last):
    return f"Your name is {first} {last}"


print(full_name(first="Makhanya", last="Mzili"))
print(full_name(last="Mzili", first="Makhanya"))

#       You may not see the value now, but it's useful
#       when passing a dictionary to a function and
#       unpacking its values - we'll see that later!
