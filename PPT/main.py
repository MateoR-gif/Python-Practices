from modules import *

def game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins', computer_wins)
        print('user_wins', user_wins)

        user_option, computer_option, rounds = choose_option(rounds)
        user_wins, computer_wins = rules(user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print('El ganador es la computadora')
            break

        if user_wins == 2:
            print('El ganador es el usuario')
            break

game()