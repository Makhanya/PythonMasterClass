print("Rock...")
print("Paper...")
print("Scissor...")

player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")

if player1 == "rock" and player2 == "scissors":
    print("Player 1 wins")
elif player1 == "rock" and player2 == "paper":
    print("Player 2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins!")
elif player1 == "paper" and player2 == "scissor":
    print("Player 2 wins!")
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 wins")
elif player1 == "scissor" and player2 == "paper":
    print("Player 1 wins!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("something went wrong")
