# While Loop Exercise
# While loops are really hard for me to write tests for
# (until we learn about things like lists),
# so this exercise is a bit tricky to explain.:
# (Here's the main idea:
#  Use a while loop to generate a random number between 1 and 10 until
#  you get the number 5. Every time the loop runs, increment the variable i .
# Here are more detailed steps:
#  Generate a random number between 1 and 10 using randint(1, 10),
#  storing the result in the number variable
#  Write a while loop to keep regenerating a new random number
#  between 1 and 10 while the random number is not equal to 5.
#  In order for my tests to work, please add 1 to i  each time through the loop.
#  My tests use this variable to check how many times your loops runs.

from random import randint

# use randint(a, b) to generate a random number between a and b
from random import randint

number = 0  # store random number in here, each time through
i = 0  # i should be incremented by one each iteration
number = randint(1, 10)


while i <= 5:
    if number != 5:
        number = randint(1, 10)
    i += 1

print(f"The loop iterated for {i} times")
