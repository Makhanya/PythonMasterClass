from random import randint

num = randint(1, 10)
print(f"test the {num}")
guess = int(input("Guess a number between 1 and 10: "))
flag = None
while flag != True:
    if num == guess:
        print("You guessed it! You won!")
        new = input("Do you want to keep playing? (y/n) ")
        if new == "y":
            flag = False
        else:
            flag = True
            break

    if num > guess:
        print("Too low. try again")

    if num < guess:
        print("Too high, try again")

    guess = int(input("Guess a number between 1 and 10: "))
