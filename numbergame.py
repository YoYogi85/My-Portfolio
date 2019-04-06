from random import *


def main():
    result = randint(1, 10)
    start_game = False

    while start_game is False:
        print('Welcome to the number game, 5 or higher you win, 4 or lower you lose, do you want to play?')
        answer = str.upper(input('Y/N: '))

        if answer == 'Y':
            start_game = True
            if result < 5:
                print(result)
                print('You Lose!!')
            else:
                print(result)
                print('You Win!!')
        elif answer == 'N':
            print('Goodbye')
            exit()
        else:
            print('Start again:')


if __name__ == '__main__':
    main()
