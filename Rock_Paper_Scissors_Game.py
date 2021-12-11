

import sys
import random

options_list = ['Rock','Paper','Scissor']

computer_player = random.choice(options_list)

human_player = input('Choose either of the 3 options below:- \n 1.Rock \n  2.Paper \n 3.Scissor \n')

score = 0

while condition:

        # Computer Winning
    if human_player == 'Rock' and computer_player == 'Paper':
        print('Computer wins!!')
        break
    elif human_player == 'Scissor' and computer_player == 'Rock':
        print('Computer wins!!')
        break
    elif human_player == 'Paper' and computer_player == 'Scissor':
        print('Computer wins!!')
        break
        # Human Winning
    elif human_player == 'Paper' and computer_player == 'Rock':
        print('You win!!')
        break
    elif human_player == 'Rock' and computer_player == 'Scissor':
        print('You win!!')
        break
    elif human_player == 'Scissor' and computer_player == 'Paper':
        print('You win!!')
        break
        #sys.exit()

print('Thanks for playing this wonderful Game, have a nice day.')
