from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_status = True

while machine_status:

    drink = input(f"What would you like? {menu.get_items()} :").lower()

    if drink == "off":
        print("Powering off")
        exit()
    elif drink == "report":
        coffee.report()
        money_machine.report()
    elif drink == "latte" or drink == "espresso" or drink == "cappuccino":
        drink_details = menu.find_drink(drink)
        if coffee.is_resource_sufficient(drink_details) and money_machine.make_payment(drink_details.cost):
            coffee.make_coffee(drink_details)
