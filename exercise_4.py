# Task 4
#
# Rock Paper Scissors
#
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game.
#
# Remember the rules:
#
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock


def decider(i1, i2):
    if i1 == i2:
        print('Its a Tie')

    elif i1 == 'rock':

        if i2 == 'scissors':
            print('Player 1 wins')
        elif i2 == 'paper':
            print('Player 2 wins')
        else:
            print('Player 2 has entered invalid input')

    elif i1 == 'paper':

        if i2 == 'rock':
            print('Player 1 wins')
        elif i2 == 'scissors':
            print('Player 2 wins')
        else:
            print('Player 2 has entered invalid input')

    elif i1 == 'scissors':

        if i2 == 'paper':
            print('Player 1 wins')
        elif i2 == 'rock':
            print('Player 2 wins')
        else:
            print('Player 2 has entered invalid input')

    else:
        print('Invalid Input')


print('Welcome to 2 Player Rock-Paper-Scissors game')

restart = True

while restart:
    ip1 = str(input('\nPlayer 1, enter rock, paper or scissors\n'))
    ip2 = str(input('Player 2, enter rock, paper or scissors\n'))
    decider(ip1, ip2)
    restart_ip = str(input('\nStart a  new game: yes or no?\n'))

    if restart_ip == 'no':
        restart = False
