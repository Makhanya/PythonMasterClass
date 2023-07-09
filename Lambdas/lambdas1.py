"""
    Lambdas

"""


def square(num):
    return num*num

# print(square(9))


def square2(num): return num*num
def add(a, b): return a+b


print(square2(9))
print(add(3, 10))

print(square2.__name__)
print(square.__name__)
print(add.__name__)
