# TODO: 1. Import menu and resources  from data.py
from data import MENU, resources

# TODO: 2. Create report() function which prints the resources we have and also the money.
money = 0.0
def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")

# TODO: 3. Create resource_sufficient('coffee') function which returns a 'boolean value' and a 'resource name'
def resource_sufficient(coffee):
    ingredients = MENU[coffee]['ingredients']
    milk = ingredients.get('milk', 0.0)
    water = ingredients['water']
    coffee = ingredients['coffee']
    milk_left = resources['milk'] - milk
    water_left = resources['water'] - water
    coffee_left = resources['coffee'] - coffee
    if milk_left >= 0 and water_left >= 0 and coffee_left >= 0:
        return True, None
    elif milk_left < 0:
        return False, 'Sorry, Milk is not sufficient.'
    elif water_left < 0:
        return False, 'Sorry, Water is not sufficient.'
    elif coffee_left < 0:
        return False, 'Sorry, Coffee is not sufficient.'





# TODO: 4. process_coins() function which gets coins as input and return the total amount in dollars.
def process_coins():
    quarter = int(input("Enter the number of quarters: "))
    dime = int(input("Enter the number of dime: "))
    nickel = int(input("Enter the number of nickel: "))
    penny = int(input("Enter the number of penny: "))
    total_money = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)
    return total_money

# TODO: 5. transaction(amount, 'coffee') which checks for enough money and returns change.
def transaction(amount, coffee):
    cost = MENU[coffee]['cost']
    change = round(amount - cost, 2)
    if change >= 0:
        return True, f'You have ${change} in change.'
    else:
        return False, f"You don't have enough money, cash refunded."


# TODO: 6. make_coffee('coffee') reduces the water, milk, coffee from the resources and prints coffee ready!.
def make_coffee(coffee_name):
    global money
    gain = MENU[coffee_name]['cost']
    ingredients = MENU[coffee_name]['ingredients']
    milk = ingredients.get('milk', 0.0)
    water = ingredients['water']
    coffee = ingredients['coffee']

    resources['milk'] -= milk
    resources['water'] -= water
    resources['coffee'] -= coffee
    money += gain

    print(f"Your {coffee_name} is ready 😊")


# TODO: 7. Implement the start() function to start the coffee_machine and implement the logic of coffee_machine.

def start():
    stop_machine = False
    while not stop_machine:
        choice = input("Do you want to order (espresso, latte, cappuccino) : ").lower()
        if choice == 'report':
            report()
        elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            is_sufficient, in_sufficient_msg = resource_sufficient(choice)
            if is_sufficient:
                amount = process_coins()
                is_success, change_msg = transaction(amount, choice)
                print(change_msg)
                if is_success:
                    make_coffee(choice)
            else:
                print(in_sufficient_msg)

        elif choice == 'off':
            stop_machine = True

start()


