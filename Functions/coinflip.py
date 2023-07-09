from random import random


# def flip_coin():
#     #   generate random number 0-1
#     r = random()
#     if r > 0.5:
#         return "Heads"
#     else:
#         return "Tails"

# def flip_coin():
#     #   generate random number 0-1
#     if random() > 0.5:
#         return "Heads"
#     else:
#         return "Tails"


# print(flip_coin())
# def generate_evens():
#     return ([x for x in range(1, 50)if x % 2 == 0])
# print(generate_evens())

# def square_of_7():
#     print("I AM BEFORE THE RETURN")
#     return 7**2
#     print("I AM AFTER THE RETURN!")
# result = square_of_7()
# print(result)

# def square(num):
#     return num*num

# print(square(4))
# print(square(8))


# def add(a, b):
#     return a+b


# print(f"sum of a + n {add(5, 9)}")
def yell(val):
    val = val.upper()
    return ("{}!".format(val))


print(yell("go away"))
print(yell("leave me alone"))
