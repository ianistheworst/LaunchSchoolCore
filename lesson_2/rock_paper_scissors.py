"""
ROCK PAPER SCISSORS (LIZARD SPOCK) THUNDERDOME!!
A simple RPSLP program that will go until either player or
pc gets to 3, or 5 total games have been played. """

import random
def prompt(message):
    print(f'==> {message}')
def display_winner(player, computer):
    prompt(f'You have chosen {player}')
    prompt(f'The computer cas chosen {computer}')
    if ((player == 'ROCK' and computer == ('SCISSORS' or 'LIZARD')) or
        (player == 'PAPER' and computer == ('ROCK' or 'SPOCK')) or
        (player == 'SCISSORS' and computer == ('PAPER' or 'LIZARD')) or
        (player == 'LIZARD' and computer == ('PAPER' or 'SPOCK')) or
        (player == 'SPOCK' and computer == ('ROCK' or 'SCISSORS'))):
        prompt('You win!!')
        return 'win'
    elif player == computer:
        prompt('You tie!')
        return 'tie'
    else:
        prompt('You lose, you freaking loser. ')
        return "lose"


CHOICES = ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']
num_of_games = 0
player_wins = 0
computer_wins = 0
ties = 0

while num_of_games < 5:
    num_of_games += 1
    prompt('Welcome to the RPS Thunderdome! Play to Best of 5!')
    prompt("CHOOSE YOUR WARRIOR.")
    #player_choice = input(f'1- {CHOICES[0]}, 2- {CHOICES[1]}, 3- {CHOICES[2]}\n')
    player_choice = input('--'.join(CHOICES) + '\n').upper()


    while player_choice not in CHOICES:
        print('Invalid input.')
        player_choice = input('--'.join(CHOICES)+ '\n').upper()


    pc_choice = random.choice(CHOICES)

    winner = display_winner(player_choice, pc_choice)
    if winner == 'win':
        player_wins += 1
    elif winner == 'lose':
        computer_wins += 1
    else:
        ties += 1

    prompt(f'You have played {num_of_games} games. {5 - num_of_games} games left.')
    prompt(f'Player wins: {player_wins} -- Computer wins: {computer_wins} -- Ties: {ties}')
    if player_wins == 3 or computer_wins == 3:
        prompt(f'GAME OVER! Player wins: {player_wins} --'
               f'Computer wins: {computer_wins} -- Ties: {ties}')
        break
    if num_of_games == 5:
        print('End of games!')
        if player_wins > computer_wins:
            prompt('GAME OVER!! YOU WIN!!')
        elif computer_wins > player_wins:
            prompt('GAME OVER!! COMPUTER WINS!!')
        else:
            prompt('GAME OVER!! Looks like it\'s a tie...')
        break

    prompt('Play again? (y/n)')
    repeat = input()
    while repeat.casefold() != 'y':
        if repeat.casefold() == 'n':
            prompt('Thank you for playing!')
            quit()
        else:
            prompt('Invalid input. Play again? (y/n)')
            repeat = input()