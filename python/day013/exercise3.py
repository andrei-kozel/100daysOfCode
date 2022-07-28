# Read this the code
# Spot the problems 🐞.
# Modify the code to fix the program.

for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:  # if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:  # if number % 5 == 0:
        print("Buzz")
    else:
        print(number)
