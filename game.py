import random

print("Welcome to rock-paper-scissors")

player_choice = str(input("Choose rock, paper, or scissors: "))

print("You chose:" , player_choice)

# --------------- you do computer choice ---------------
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print("Computer chose:", computer_choice)


if player_choice.lower().strip() == computer_choice.lower().strip():
    print("You win")
else:
    print("You lose")