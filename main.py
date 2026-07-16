MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
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
    "money":0,
}

def generate_report():
    return f"""
    Water: {resources["water"]}ml
    Milk: {resources["milk"]}ml
    Coffee: {resources["coffee"]}g
    Money: ${resources["money"]}
    """

def are_resources_sufficient(drink):
    for item in MENU[drink]["ingredients"]: # water, milk, coffee
        if resources[item] < MENU[drink]["ingredients"][item]: # If milk in resources < milk for drink
            return f"Sorry, there is not enough {item}."
    return True

def process_payment(drink):
    drink_cost = MENU[drink]["cost"]
    q = float(input("Insert Quarters: "))
    d = float(input("Insert Dimes: "))
    n = float(input("Insert Nickels: "))
    p = float(input("Insert Pennies: "))

    total_payment = (q * 0.25) + (d * 0.1) + (p * 0.01) + (n * 0.05)
    if total_payment >= drink_cost:
        change = round(total_payment - drink_cost, 2)
        print(f"Your change is ${change}")
        resources["money"] += drink_cost
        return True
    elif total_payment < drink_cost:
        print("Not enough money. Money Refunded.")
        return False

def make_coffee(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    return f"Here is your {drink}. Enjoy!"


# print(are_resources_sufficient(user_input))

# TODO. 4. If yes, ask them for coins

loop = True

while loop:
    print("\nWelcome to Coffee Machine")
    user_input = input("What drink would you like?:\n"
                   "~ Latte\n"
                   "~ Espresso\n"
                   "~ Cappuccino\n"
                   ": ").lower()

    if user_input == "report":
        print(generate_report())
    elif user_input == "off":
        print("Turning Off.")
        loop = False
    else:
        if are_resources_sufficient(user_input) == True:
            if process_payment(user_input):
                print(make_coffee(user_input))
        else:
            print(are_resources_sufficient(user_input))

# TODO. 6. Make the drink, and subtract resources.
# TODO. 7. "Here is your {drink}, enjoy!"

