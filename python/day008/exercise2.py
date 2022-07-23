# You need to write a function that checks whether if the number passed into it is a prime number or not.
# Write your code below this line 👇
import math


def prime_checker(number):
    rounded_square_root = math.ceil(math.sqrt(number))
    if number == 2 or number == 1:
        print("It's a prime number.")
    else:
        for _n in range(2, rounded_square_root + 1):
            if number % _n != 0:
                print("It's a prime number.")
                break
            else:
                print("It's not a prime number.")
                break


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
