MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0


def get_ingredients(drink_name):
    """Get all ingredients"""
    return MENU[drink_name]["ingredients"]


def get_price(drink_name):
    """Get drink price"""
    return MENU[drink_name]["cost"]


def has_ingredients(drink_name):
    """Returns True when order can be made, False if ingredients are insufficient."""
    ingredients = get_ingredients(drink_name)
    for ingredient in ingredients:
        if ingredient in resources.keys() and ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def remove_ingredients(drink_name):
    """Deduct the required ingredients from the resources."""
    for ingredient in get_ingredients(drink_name):
        resources[ingredient] -= get_ingredients(drink_name)[ingredient]


def make_a_payment(drink_name):
    """Returns true if the payment was successful"""
    global money
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    if total > get_price(drink_name):
        print(f"Here is ${total - get_price(drink_name)} in change")
        money += get_price(drink_name)
        return True
    if total == get_price(drink_name):
        money += get_price(drink_name)
        return True
    else:
        print("Sorry, there is not enough money.")
        return False


def make_drink(drink_name):
    """Make a drink if payment was successful, and we have all ingredients"""
    if has_ingredients(drink_name):
        is_payment_successful = make_a_payment(drink_name)
        if is_payment_successful:
            print(f"Here is your {drink_name}! Enjoy!")
            remove_ingredients(drink_name)


# Start
is_turned_on = True
while is_turned_on:
    user_res = input("What would you like? (espresso/latte/cappuccino): ")

    if user_res == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif user_res == "off":
        is_turned_on = False
    else:
        make_drink(user_res)
