rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

rps_items = [rock, paper, scissors]
item_id = int(input("What do you choose? Type 0 for Rock, 1  for Paper, 2 for Scissors > "))

if item_id > 2:
    print("You typed an invalid number, you lose!")
    exit()

user_input = rps_items[item_id]
print(user_input)

pc_input = rps_items[random.randint(0, 2)]
print("Computer chose:")
print(pc_input)

if pc_input == user_input:
    print("It's a draw")
elif pc_input == rock and user_input == scissors:
    print("You lose.")
elif pc_input == scissors and user_input == paper:
    print("You lose.")
elif pc_input == paper and user_input == rock:
    print("You lose.")
else:
    print("You win")
