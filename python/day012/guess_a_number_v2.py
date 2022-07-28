from art import logo
from random import randint

HARD_DIFFICULTY = 5
EASY_DIFFICULTY = 10


def check_answer(guess, number, turns):
    """ Checks answer against guess. Returns the number of turns remaining."""
    if guess > number:
        print("Too high.")
        return turns - 1
    elif guess < number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {number}.")


def set_difficulty():
    """ Set the game difficulty """
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        return HARD_DIFFICULTY
    else:
        return EASY_DIFFICULTY


def game():
    # Logo
    print(logo)

    # Get random number
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)

    # For testing
    print(f"Pssst ... it's {number}")

    # Set amount of attempts based on difficulty
    turns = set_difficulty()
    guess = 0

    # Ask user to guess a number
    while guess != number:
        print(f"You have {turns} attempts remaining to guess a number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")


# Start the game
game()
