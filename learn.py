import random

#Create a rock, paper, scissor
def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(options)
    return choices

def check_win(player_choice, computer_choice):
    print(f"You chose {player_choice}, computer chose {computer_choice}")
    if player_choice == computer_choice:
        return "It's a tie!"

print(check_win())