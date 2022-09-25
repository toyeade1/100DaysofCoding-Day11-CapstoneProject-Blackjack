# :(
import random
from day11logo import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)

def calculate_score(listofcards):
    if listofcards[0] + listofcards[1] == 21:
        return 0
    if 11 in listofcards and sum(listofcards) > 21:
        listofcards.remove(11)
        listofcards.append(1)
    return sum(listofcards)

def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    for card in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_end = False

    print(f'Your cards are: {user_cards}')
    print(f'The computers first card is: {computer_cards[0]}')

    if calculate_score(user_cards) == 0:
        print('You have blackjack!')
        game_end = True
    if calculate_score(computer_cards) == 0:
        print('The computer has blackjack. You lose!')
        game_end = True
    if calculate_score(user_cards) > 21:
        print('Your score is over 21. You lose.')
        game_end = True

    while not game_end:
        user_choice = str(input('Would you like to draw another card? "y" or "n":\n'))
        if user_choice == 'y':
            user_cards.append(deal_card())
            calculate_score(user_cards)
            if calculate_score(user_cards) == 0:
                print('You have blackjack! You win!')
                game_end = True
            if calculate_score(computer_cards) == 0:
                print('The computer has blackjack. You lose!')
                game_end = True
            if calculate_score(user_cards) > 21:
                print(f'Your score is {calculate_score(user_cards)}, which is over 21. You lose.')
                game_end = True
            print(f'Your cards are: {user_cards}')
        if user_choice == 'n':
            while calculate_score(computer_cards) < 17:
                computer_cards.append(deal_card())
            game_end = True

    def compare():
        if calculate_score(user_cards) == calculate_score(computer_cards):
            print('Its a draw!')
        if calculate_score(computer_cards) > 21:
            print('The computers score is over 21. You win!')
        if calculate_score(user_cards) != calculate_score(computer_cards) and calculate_score(
                computer_cards) < 21 and calculate_score(user_cards) < 21 and calculate_score(
                user_cards) != 0 and calculate_score(computer_cards) != 0:
            if calculate_score(user_cards) > calculate_score(computer_cards):
                print('Your score was higher than the computers. You win!')
            else:
                print(f'The computers score was {calculate_score(computer_cards)}, Your score was lower. You lose.')

    if game_end:
        compare()
        restart_game = str(input('Would you like to restart the game? "yes" or "no" '))
        if restart_game == 'yes':
            blackjack()
        else:
            print('Thank you for playing! Good bye.')
            print(logo)

blackjack()