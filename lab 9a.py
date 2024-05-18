# Tianhao Zhang

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random
choices = ['rock', 'paper', 'scissors']

def get_user_choice():
    choice = input('Pick one of rock, paper or scissors: ').lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    return choice

def get_human_choices(num_players):
    choices = []
    for i in range(num_players):
        choice = get_user_choice()
        choices.append(choice)
    return choices

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choices, computer_choices):
    if len(player_choices) == 1:  
        p1 = player_choices[0]
        p2 = computer_choices[0]
        if p1 == p2:
            return "It's a tie!"
        elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
            return "Player 1 wins!"
        else:
            return "Computer wins!"
    elif len(player_choices) == 2:  
        p1 = player_choices[0]
        p2 = player_choices[1]
        if p1 == p2:
            return "It's a tie!"
        elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    else:  
        computer_wins = computer_choices.count('rock') + computer_choices.count('paper') + computer_choices.count('scissors')
        return f"Computer wins by default with {computer_wins} choices."

def play_game(num_human_players):
    if num_human_players > 0:
        player_choices = get_human_choices(num_human_players)
    else:
        player_choices = []
    computer_choices = [get_computer_choice() for _ in range(2 - num_human_players)]
    print(f"Player choices: {player_choices}")
    print(f"Computer choices: {computer_choices}")
    print(determine_winner(player_choices, computer_choices))

num_players = int(input("Enter the number of human players (0-2): "))
play_game(num_players)
