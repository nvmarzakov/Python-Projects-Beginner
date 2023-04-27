from time import sleep

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 0.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 1.00,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 0.70,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources_func(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            
            return False
          
    return True


def process_coins():
    """Return the total calculated from coins inserted."""
    
    print("Please insert coins.")
    total = int(input("How many coins with value 0.05?: ")) * 0.05
    total += int(input("How many coins with value 0.10?: ")) * 0.10
    total += int(input("How many coins with value 0.20?: ")) * 0.20
    total += int(input("How many coins with value 0.50?: ")) * 0.50
    total += int(input("How many coins with value 1.00?: ")) * 1
    total += int(input("How many coins with value 2.00?: ")) * 2

    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if monet is insufficient"""
    
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        
        if change > 0:
            print(f"Here is BGN {change} in change.")
        global profit
        profit += drink_cost
        
        return True
    
    print(f"Sorry that's not enough money. Money refunded.")
    return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    
    time = "Please wait.....⌛⌛⌛⌛⌛⌛⌛"

    print(time)
    sleep(5)
    print(f"\nHere is your drink {drink_name}! Enjoy it!")
    print()


print("☕☕☕ Welcome to Sweet Coffee Machine! ☕☕☕")

is_on = True

while is_on:
    choice = input("What drink can i do for you? \n"
                   "Please choose you number or turn me OFF: \n"
                   "    1 - espresso \n"
                   "    2 - latte \n"
                   "    3 - cappuccino\n"
                   "You choose: ")

    if choice == "off":
        print("\nHave a nice day!")
        is_on = False
    
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: BGN {profit}")
        print()
    
    else:
        if choice == '1':
            choice = 'espresso'
       
        elif choice == '2':
            choice = 'latte'
        
        elif choice == '3':
            choice = 'cappuccino'
        drink = MENU[choice]
        
        if check_resources_func(drink['ingredients']):
            payment = process_coins()
            
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
        else:
            print("Please come back tomorrow!")
            is_on = False
