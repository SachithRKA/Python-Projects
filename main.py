from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeM = CoffeeMaker()
moneyM = MoneyMachine()
menu = Menu()
is_on = True

#user_input = input(f"What would you like? (espresso/latte/cappuccino): ")

while is_on:
    option = menu.get_items()
    choice = input(f"what would you like ? ({option}): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeeM.report()
        moneyM.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeM.is_resource_sufficient(drink) and moneyM.make_payment(drink.cost):
            coffeeM.make_coffee(drink)