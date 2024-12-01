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

money = 0


def report(resource):
    water_quan = resource["water"]
    milk_quan = resource["milk"]
    coffee_quan = resource["coffee"]
    return (f"water: {water_quan}ml\nmilk: {milk_quan}ml\ncoffee: {coffee_quan}g\nmoney: ${money}")

# TODO:3 process coins.


def process_coins():
    """Returns the total calculated from the coins inserted."""
    print("Please insert coins")
    total =  int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

# TODO:2 check resource sufficient?.


def is_resource_sufficient(order_ingredients):
    """Returns True when the order can made, False if ingredient are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

# TODO:4 check transaction successful?


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if the money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO:5 make coffee.


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} enjoy.")

# TODO:1 print a report.


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(report(resources))
    else:
        drink = MENU[choice]
#        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
