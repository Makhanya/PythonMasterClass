import random
print("Rock...")
print("Paper...")
print("Scissors...\n")

player = input("Player, make your move: ").lower()
rand_num = random.randint(0, 2)

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("Player wins!")
    elif computer == "papepr":
        print("Computer wins")
elif player == "paper":
    if computer == "rock":
        print("Player wins!")
    elif computer == "scissors":
        print("Computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("Player wins!")
    elif computer == "rock":
        print("Computer wins!")
else:
    print("Something went wrong")
