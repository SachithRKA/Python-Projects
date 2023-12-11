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
    "money": 0,
}

answer = True

def report():
    print(f"Water: {resources["water"]}ml  \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g \nMoney: ${resources["money"]} \n")


def enough_resources(drink_type):
    if drink_type == "espresso":
        water_amount = MENU[drink_type]["ingredients"]["water"]
        coffee_amount = MENU[drink_type]["ingredients"]["coffee"]
        return resources["water"] >= water_amount & resources["coffee"] >= coffee_amount
    elif drink_type == "latte":
        water_amount = MENU[drink_type]["ingredients"]["water"]
        coffee_amount = MENU[drink_type]["ingredients"]["coffee"]
        milk_amount = MENU[drink_type]["ingredients"]["milk"]
        return resources["water"] >= water_amount & resources["coffee"] >= coffee_amount & resources["milk"] >= milk_amount
    else:
        water_amount = MENU[drink_type]["ingredients"]["water"]
        coffee_amount = MENU[drink_type]["ingredients"]["coffee"]
        milk_amount = MENU[drink_type]["ingredients"]["milk"]
        return resources["water"] >= water_amount & resources["coffee"] >= coffee_amount & resources["milk"] >= milk_amount


def total_coins(penny, dime, nickel, quarter):
    return quarter * 0.25 + dime * 0.10 + nickel * 0.05 + penny * 0.01


def check_transaction(user_total, user_input):
    return user_total - MENU[user_input]["cost"]


def take_amount(user_input):
    if user_input == "espresso":
        resources["money"] += MENU[user_input]["cost"]
    elif user_input == "latte":
        resources["money"] += MENU[user_input]["cost"]
    else:
        resources["money"] += MENU[user_input]["cost"]


def deduct_resources(user_input):
    if user_input == "espresso":
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
    elif user_input == "latte":
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
        resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
    else:
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
        resources["milk"] -= MENU[user_input]["ingredients"]["milk"]


while (answer):
    user_input = input(f"What would you like? (espresso/latte/cappuccino): ")

    if not enough_resources(user_input):
        print(f"Sorry there is not enough resources.")
        print(report)
    else:
        # Expects user to enter a number that is larger than 0 for everything, so no error handling
        penny_num = int(input(f"Enter the number of penny you want to enter: "))
        dime_num = int(input(f"Enter the number of dimes you want to enter: "))
        nickel_num = int(input(f"Enter the number of nickel you want to enter: "))
        quarter_num = int(input(f"Enter the number of quarter you want to enter: "))

        user_total = total_coins(penny_num, dime_num, nickel_num, quarter_num)
        user_amount_validation = check_transaction(user_total, user_input)

        if user_amount_validation < 0:
            print(f"Sorry that's not enough money. Money refunded")
            exit_user = True
        elif user_amount_validation > 0:
            print(f"Here is ${user_amount_validation} in change")
            take_amount(user_input)
            deduct_resources(user_input)
            print(f"here is your {user_input}. Enjoy!")
        else:
            take_amount(user_input)
            deduct_resources(user_input)
            print(f"here is your {user_input}. Enjoy!")

        continueOrder = input(f"Do you want to continue: Yes or No: ")

        if continueOrder == "Yes":
            answer = True
        elif continueOrder == "No":
            answer = False
