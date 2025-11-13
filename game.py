print("Welcome to rock-paper-scissors")

player_choice = str(input("Choose rock, paper, or scissors: "))

print("You chose:" , player_choice)

# --------------- you do computer choice ---------------

if player_choice.lower().strip() == computer_choice.lower().strip():
    print("You win")
else:
    print("You lose")
# meow