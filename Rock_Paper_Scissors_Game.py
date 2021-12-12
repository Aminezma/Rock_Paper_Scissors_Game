
import random
import sys

print('ROCK, PAPER, SCISSORS')

print('0 Wins, 0 Losses, 0 Ties')

human_score = 0

options_list = ['r','p','s']

computer_score = 0

tie = 0

computer_move = random.choice(options_list)

for i in range(10):

    player_move = input('Enter your Move: (r)ock (p)aper (s)cissors or (q)uit \n')

            # TIE GAME
    if player_move == 'p' and computer_move == 'p':

        print('It is a tie!')

        computer_score = 0
        human_score = 0
        tie = tie + 1

    elif player_move == 'r' and computer_move == 'r':

        print('It is a tie!')

        computer_score = 0
        human_score = 0
        tie = tie + 1


    elif player_move == 's' and computer_move == 's':

        print('It is a tie!')

        computer_score = 0
        human_score = 0
        tie = tie + 1


                # COMPUTER WINNING
    elif player_move == 'p' and computer_move == 's':

        print('Computer Wins!')

        computer_score = computer_score + 1

        human_score = 0

        tie = 0


    elif player_move == 's' and computer_move == 'r':


        print('Computer Wins!')

        computer_score = computer_score + 1

        human_score = 0

        tie = 0


    elif player_move == 'r' and computer_move == 'p':


        print('Computer Wins!')

        computer_score = computer_score + 1

        human_score = 0

        tie = 0



        # HUMAN WINNING
    elif player_move == 's' and computer_move == 'p':


        print('You Win!')

        computer_score = 0

        human_score = human_score + 1

        tie = 0


    elif player_move == 'r' and computer_move == 's':


        print('You Win!')

        computer_score = 0

        human_score = human_score + 1

        tie = 0

    elif player_move == 'p' and computer_move == 'r':


        print('You Win!')

        computer_score = 0

        human_score = human_score + 1

        tie = 0

    elif player_move == 'q':

        print('Thank you for playing!')

        sys.exit()



print(str(human_score) + 'Wins, ' + str(computer_score) + 'Losses, ' +  str(tie) + 'Ties')
