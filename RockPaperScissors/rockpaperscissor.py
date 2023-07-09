print("...rock...")
print("...paper...")
print("...scissor...")
value1 = input("Enter Player 1's choice): ")

value2 = input("Enter Player 2's choice): ")

if value1 == "rock":
    if value2 == "paper":
        print("Player 2 wins")
    if value2 == "scissor":
        print("Player 1 wins")

if value1 == "paper":
    if value2 == "scissor":
        print("Player 2 wins")
    if value2 == "rock":
        print("Player 1 wins")

if value1 == "scissor":
    if value2 == "rock":
        print("Player 2 wins")
    if value2 == "paper":
        print("Player 1 wins")
elif value1 == value2:
    print("Draw")
else:
    print("Something went wrong")
