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
    },
}


def change_resources(order, resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]

    for key in MENU:
        if key == order:
            water -= MENU[order]["ingredients"]["water"]
            coffee -= MENU[order]["ingredients"]["coffee"]
            money += MENU[order]["cost"]
            if order != "espresso":
                milk -= MENU[order]["ingredients"]["milk"]

    changed = {
        "water": water,
        "milk": milk,
        "coffee": coffee,
        "money": money,
    }

    return changed


def print_report(resources):
    for key in resources:
        if key == "coffee":
            print(f"{resources[key]}g")
        elif key == "money":
            print(f"${resources[key]}")
        else:
            print(f"{resources[key]}ml")


def check_resources(resources, order):
    new_resources = resources
    new_resources = change_resources(order, resources)
    for key in new_resources:
        if new_resources[key] <= 0 and key != "money":
            print(f" Sorry there is not enough {key}.")
            return
        else:
            return True


def check_pay(order, prices):
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    pay = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if prices[order]["cost"] > pay:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(pay - prices[order]["cost"], 2)
        print(f"Here is ${change} change.\nHere is your {order} Enjoy")


def ordering(resources, prices):
    continue_ordering = True
    while continue_ordering:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "report":
            print_report(resources)
        elif order == "off":
            continue_ordering = False
        else:
            if check_resources(resources, order):
                check_pay(order, prices)
                resources = change_resources(order, resources)
