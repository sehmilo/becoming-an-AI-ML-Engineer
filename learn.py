import random

#Create a rock, paper, scissor
def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(options)
    return choices

def check_win(player, computer):
    print("You chose " + player + ", computer chose " + computer)
    if player == computer:
        return "It's a tie!"

print(check_win("rock", "scissors"))