import copy

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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


# TODO: 1. getting reports from the data base
def report():
    global profit
    print(f"Water: {current_resources["water"]}ml\n"
          f"Milk: {current_resources["milk"]}ml\n"
          f"Coffee: {current_resources["coffee"]}g\n"
          f"Money: ${profit}"
          )


# TODO 2. Calculating the total Money inserted by user
def asking_and_calculating_money():
    """ Function will ask user for input and add all money, Returns the values"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


# TODO 3. Function to check resources are sufficient or not
def resources_checker(current_resources, ordered_coffee):
    """This Function checks weather machine have sufficent number of resources"""
    for items in MENU[ordered_coffee]["ingredients"]:
        if current_resources[items] >= MENU[ordered_coffee]["ingredients"][items]:
            current_resources[items] -= MENU[ordered_coffee]["ingredients"][items]
        elif current_resources[items] < MENU[ordered_coffee]["ingredients"][items]:
            print(f"Sorry there is not enough {items}.")
            return 1


# TODO 4. FUNCTION FOR calculating the change and money
def money_checker(orders_coffee, total_money):
    """This Function will calculate the return change and if insufficient money entered"""
    global profit
    if total_money > MENU[orders_coffee]["cost"]:
        total_money -= MENU[orders_coffee]["cost"]
        print(f"Here is ${round(total_money, ndigits=2)} in change.")
        profit += MENU[orders_coffee]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


profit = 0
current_resources = copy.copy(resources)   # Creating copy of the resources so that we can modify it accordingly

#using whileloop and giving all posible outcomes and results using above created functions
CoffeeMachine = True
while CoffeeMachine:
    Ordered_Coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if Ordered_Coffee == "off":  # To power off the Machine
        CoffeeMachine = False
        print("Powering off")
        break
    elif Ordered_Coffee == "report":  # report Gives us the resources currently we have and profit
        report()
    elif Ordered_Coffee == "espresso" or Ordered_Coffee == "latte" or Ordered_Coffee == "cappuccino": # To check and user ordered coffee and process it
        resources = resources_checker(current_resources, Ordered_Coffee)
        if resources == 1:
            continue
        Total_Money = asking_and_calculating_money()
        money = money_checker(Ordered_Coffee, Total_Money)
        if money != 0:
            print(f"Here is your {Ordered_Coffee} ☕️. Enjoy!")
    else:                                               # If user has entered any typo this will stop poping up error
        print("Enter the correct details.")
