# this is the attempt without help or using the hints

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


from day11logo import logo
import random
play_game = str(input('Do you want to play a game of Blackjack? Type "y" or "n": '))
if play_game == 'y':
    user_cards = []
    computer_cards = []
    print(logo)
    for card in range(0,2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    print(f'Your cards are {user_cards}')
    print(f'The dealer has a {computer_cards[0]}')
    user_sum = user_cards[0] + user_cards[1]
    computer_sum = computer_cards[0] + computer_cards[1]
    if user_sum == 21 and computer_sum !=  21:
        print(f'You have blackjack congratulations! Your total was {user_sum}')
    if computer_sum == 21:
        print('You lost, the computer has blackjack')
    if user_sum > 21:
        if 11 in user_cards:
            user_sum = user_sum - 10
        else:
            print(f'You lost, your score was {user_sum} try again')
    while user_sum < 21:
        another_card = str(input(f'Your total score is {user_sum} would you like to draw another card? "y" or "n": '))
        if another_card == 'y':
            user_cards.append(random.choice(cards))
            user_sum += user_cards[2]
            print(user_sum)
