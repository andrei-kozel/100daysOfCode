# ############## Blackjack House ####################

import art
import random
import utilities

should_continue = True


def get_random_card():
    """ Returns a random card from the deck """
    cards = [11, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def deal_cards(hand):
    """ Deal 2 cards for user and computer """
    for _ in range(2):
        hand.append(get_random_card())


def calculate_score(_cards):
    """ Take a list of cards and returns the calculated score """
    if sum(_cards) == 21 and len(_cards) == 2:
        return 0
    elif 11 in _cards and sum(_cards) > 21:
        _cards.remove(11)
        _cards.append(1)
    return sum(_cards)


def true_or_false():
    """ Returns True or False """
    return random.choice([True, False])


def computer_turn(computer):
    """ Computer random logic """
    if calculate_score(computer) <= 21 and true_or_false():
        computer.append(get_random_card())


def compare(user_score, computer_score):
    """ Find a winner/loser or it is a draw """

    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play():
    user_cards = []
    computer_cards = []
    should_computer_continue = True
    game_over = False
    deal_cards(user_cards)
    deal_cards(computer_cards)

    print(art.logo)

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(get_random_card())
            else:
                game_over = True

    while calculate_score(computer_cards) < 18 and should_computer_continue:
        computer_turn(computer_cards)
        should_computer_continue = true_or_false()

    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
    print(compare(calculate_score(user_cards), calculate_score(computer_cards)))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    utilities.clear_console()
    play()
