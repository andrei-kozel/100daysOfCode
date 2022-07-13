import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
game_over = False
lives = 6
stages = hangman_art.stages

print(hangman_art.logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = ['_' for i in range(0, len(chosen_word))]

while not game_over:
    guess = input("Guess a letter: ").lower()
    print(f"You guessed {guess}")
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")

    print(' '.join(display))

    if "_" not in display:
        game_over = True
        print("You win")
