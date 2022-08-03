from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_turned_on = True
while is_turned_on:
    user_res = input(f"What would you like? {menu.get_items()}: ")

    if user_res == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_res == "off":
        is_turned_on = False
    else:
        drink = menu.find_drink(user_res)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
