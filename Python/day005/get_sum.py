# Kata from codewars.com
# Given two integers a and b, which can be positive or negative,
# find the sum of all the numbers between including them too and return it.
# If the two numbers are equal return a or b.
# Note: a and b are not ordered!


def get_sum(a, b):
    return sum(range(min(a, b), max(a, b)+1))


print(get_sum(1, 1))
print(get_sum(1, 0))
print(get_sum(1, 5))
print(get_sum(1, 2))
