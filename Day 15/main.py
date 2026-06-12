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
