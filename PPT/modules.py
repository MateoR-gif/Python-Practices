import random

def choose_option(rounds):

    options = ('piedra', 'papel', 'tijera')

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    rounds += 1

    if not user_option in options:
        print('esa opcion no es valida')
        return None, None, rounds

    computer_option = random.choice(options)
    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    return user_option, computer_option, rounds

def rules(user_option, computer_option, user_wins, computer_wins):

    if user_option == None:
        print('¡Anulado!')
    elif user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer gano!')
            computer_wins += 1
    return user_wins, computer_wins

