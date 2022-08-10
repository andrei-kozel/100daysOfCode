# Take a look inside file1.txt and file2.txt.
# They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.

# Write your code above 👆
with open("file1.txt") as file_1:
    numbers_1 = [int(x) for x in file_1.read().split()]

with open("file2.txt") as file_2:
    numbers_2 = [int(x) for x in file_2.read().split()]


result = [num for num in numbers_1 if num in numbers_2]

print(result)