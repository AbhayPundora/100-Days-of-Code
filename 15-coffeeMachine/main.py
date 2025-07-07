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

def show_report():
    """ Display the current resources"""
    for resource in resources:
        if resource == "money":
            print(f"{resource.title()} : ${resources[resource]}")
        else:
            print(f"{resource.title()} : {resources[resource]}")

def calc_money():
    """Returns the total amount the user paid"""
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    return  quarters + dimes + nickles + pennies

def final_resources(ingredients, profit):
    """Deduct the resources by specific coffee resources and add coffee cost as profit to resources dictionary """
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

    if not "money" in resources:
        resources["money"] = profit
    else:
        resources["money"] += profit


def make_coffee(coffee_type):
    """Checks for enough resource to make the coffee and also compare the payment with actual cost of the coffee"""
    coffee_ingredients = MENU[coffee_type]["ingredients"]
    coffee_cost = MENU[coffee_type]["cost"]

    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return

    print("Please insert coins.")
    money = round(calc_money(),2)

    def show_message():
        """Display the successful message, and calls final_resources()"""
        final_resources(coffee_ingredients, coffee_cost)
        print(f"Here is your {coffee_type} ☕️. Enjoy!")

    if money < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
    elif money == coffee_cost:
        show_message()
    else:
        print(f"Here is ${round(money - coffee_cost, 2)} in change.")
        show_message()


on_coffee_machine = True

while on_coffee_machine:
    """Starting point of the program"""
    want_to_know = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if want_to_know == "report":
        show_report()
    elif want_to_know == "off":
        on_coffee_machine = False
    else:
        make_coffee(want_to_know)



