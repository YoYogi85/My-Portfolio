from random import shuffle

def main():
    start_game = False
    cards = ['AH', 'AS', 'AD', 'AC']
    while start_game is False:
        print('Welcome to my card game, do you want to play? ')
        answer = str.upper(input('Y/N: '))

        if answer == 'Y':
            start_game = True
            if answer == 'Y':
                shuffle(cards)
                print(cards[0])
                if cards[0] == 'AS':
                    print('You Win!')
                else:
                    print('You Lose!')
        elif answer == 'N':
            print('Goodbye')
            exit()
        else:
            print('Start again:')


if __name__ == '__main__':
    main()

