from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on_coffee_machine = True

while on_coffee_machine:
    get_input_str = menu.get_items()
    order = input(f"what you want {get_input_str}: ").lower()

    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        on_coffee_machine = False
    else:
        if menu.find_drink(order) is None:
            continue
        else:
            menuItem = menu.find_drink(order)
            print(menuItem.ingredients)
            if coffee_maker.is_resource_sufficient(menuItem) and money_machine.make_payment(menuItem.cost):
                coffee_maker.make_coffee(menuItem)
            else:
                on_coffee_machine = False





