from  art import logo
from  random import randint

print(logo)

game_over = False

# Get random number
print("I'm thinking of a number between 1 and 100.")
number = randint(1, 100)
print(f"Pssst ... it's {number}")

# Set the difficulty and guesses amount
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "hard":
    max_turns = 10
elif  difficulty == "hard":
    max_turns = 5
else:
    print("You typed some gibberish ... I give you random amount of attempts")
    max_turns = randint(2, 20)

# Play a guess game
while not game_over and max_turns != 0:
    print(f"You have {max_turns} attempts remaining to guess a number")
    guess = int(input("Make a guess: "))

    if guess < number / 2:
        print("Too low.\nGuess again")
    elif guess > number / 2:
        print("Too high.\nGuess again")
    elif guess == number:
        print(f"You got it! The answer was {number}")
        game_over = True

    max_turns -= 1

if max_turns == 0:
    print("You have run out of guesses, you lose")