# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# You are going to write a program that tests the compatibility between two people.
# Write your code below this line 👇
combine_name = name1.lower() + name2.lower()

t = combine_name.count('t')
r = combine_name.count('r')
u = combine_name.count('u')
e = combine_name.count('e')
l = combine_name.count('l')
o = combine_name.count('o')
v = combine_name.count('v')
e = combine_name.count('e')

score = int(str(t + r + u + e) + str(l + o + v + e))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 or score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")