#  Positive or Negative Checking
#  In this exercise x  and y  are two random variables.
#  The code at the top of the file randomly assigns them (
#    we'll learn how it works later on).  For now, just leave it alone: )

# 1.   If both are positive numbers, print "both positive".
# 2.   If both are negative, print "both negative".
# 3.   Otherwise, tell us which one is positive and which one is negative, e.g. "x is positive and y is negative"
#
#      The print statements are filled in for you, just add logic.

#     For the tests to pass, don't change the print statements!


# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| \
from random import randint  # |  \
# x = randint(-100, 100)  # |   \
# while x == 0:  # make sure x isn't zero              #|    \
#     x = randint(-100, 100)  # |     NO TOUCHING!!!!!! (please)
# y = randint(-100, 100)  # |    /
# while y == 0:  # make sure y isn't zero              #|   /
#     y = randint(-100, 100)  # |  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /
x = 1
y = -90

# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if x and x >= 1:
    if y and y >= 1:
        print("both positive")
if x and x <= - 1:
    if y <= -1:
        print("both negative")
if (x >= 1) and (y <= -1):
    print("x is positive and y is negative")
if (y >= 1) and (x <= -1):
    print("y is positive and x is negative")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
