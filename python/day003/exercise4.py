# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Congratulations, you've got a job at Python Pizza.
# Your first job is to build an automatic pizza order program.
# Write your code below this line 👇
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
sm_pepperoni = 2
md_lg_pepperoni = 3
cheese = 1

bill = 0

if size == 'S':
    bill += small_pizza_price
elif size == "M":
    bill += medium_pizza_price
elif size == "L":
    bill += large_pizza_price

if add_pepperoni == "Y":
    if size == "S":
        bill += sm_pepperoni
    else:
        bill += md_lg_pepperoni

if extra_cheese == "Y":
    bill += cheese

print(f"Your final bill is: ${bill}.")