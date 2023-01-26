'''
Rock Paper Scissors
-----------------------------------------------
'''

import random
import os
import re


def play_status():
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input('Do you want to play Rock Paper Scissors again? You might beat me this time (yes/no): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')
            
            if response.lower() == 'yes':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing!')
                exit()

        except ValueError as err:
            print(err)

def play_game():
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Rock, Paper, Scissors - Shoot!!!')

        user_choice = input('What\'s your weapon?'
                            '   [R]ock, [P]aper, or [S]cissors: ')
        
        if not re.match("[SsRrPp]", user_choice):
            print('You haven\'t chosen a weapon.')
            user_choice = input('What\'s your weapon?'
                            '   [R]ock, [P]aper, or [S]cissors: ')
            # print('[R]ock, [P]aper, or [S]cissors')
            # continue

        print(f'You chose: {user_choice}')

        choices = ['R', 'P', 'S']
        computer_choice = random.choice(choices)

        print(f'I chose: {computer_choice}')

        if computer_choice == user_choice.upper():
            print('It\'s a tie!! You can\'t beat a computer! Ha ha!!')
        elif computer_choice == 'R' and user_choice == 'S':
            print('Rock beats Scissors, so I win!!!!!!!! What a loser you are.')
            play = play_status()
        elif computer_choice == 'P' and user_choice == 'R':
            print('Paper covers Rock, so I win!!!!!!!! What a loser you are.')
            play = play_status()
        elif computer_choice == 'S' and user_choice == 'P':
            print('Scissors cuts Paper, so I win!!!!!!!! What a loser you are.')
            play = play_status()
        else:
            print('You win!!!!!!! Congratulations, you beat a computer!! Call the press!!!')
            play = play_status()

if __name__ == '__main__':
    play_game()