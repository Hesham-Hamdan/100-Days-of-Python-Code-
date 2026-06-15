from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()


def ordering():
    continue_ordering = True
    while continue_ordering:
        order = input(f"What would you like? ({menu.get_items()})")
        if order == "report":
            coffe_maker.report()
            money_machine.report()
        elif order == "off":
            continue_ordering = False
        else:
            choice = menu.find_drink(order)
            if coffe_maker.is_resource_sufficient(
                choice
            ) and money_machine.make_payment(choice.cost):
                coffe_maker.make_coffee(choice)


ordering()
