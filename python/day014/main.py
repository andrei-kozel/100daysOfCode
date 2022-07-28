from game_data import data
from art import logo
from art import vs
from random import choice
from utilities import clear_console


def compare_followers(comp_a, comp_b):
    """ Checks followers against user's guess
        and returns True if they got it right.
        Or False if they got it wrong."""
    if comp_a['follower_count'] > comp_b['follower_count']:
        return True
    else:
        return False


def get_random_account():
    """Get data from random account"""
    return choice(data)


def game():
    score = 0
    result = True

    while result:
        print(logo)

        if score > 0:
            print(f"You're right! Current score: {score}.")

        random_comp_a = get_random_account()
        random_comp_b = get_random_account()

        print(f"Compare A: {random_comp_a['name']}, a {random_comp_a['description']}, from {random_comp_a['country']}.")
        print(vs)
        print(f"Compare B: {random_comp_b['name']}, a {random_comp_b['description']}, from {random_comp_b['country']}.")

        answer = input("Who has more followers? Type 'A' or 'B': ")

        if answer == 'A':
            result = compare_followers(random_comp_a, random_comp_b)
        else:
            result = compare_followers(random_comp_b, random_comp_a)
        if result:
            score += 1
            clear_console()

    if not result:
        clear_console()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}.")


game()
