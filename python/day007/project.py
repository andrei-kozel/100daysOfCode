# Step 2

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = ['_' for i in range(0, len(chosen_word))]

guess = input("Guess a letter: ").lower()

for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = guess
    else:
        print("Wrong")

print(' '.join(display))
