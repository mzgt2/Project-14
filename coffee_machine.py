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
money = round(0, 2)
coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}
machine_on = True




while machine_on:
        choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
        def insert_coin():
            """Generates the coins inserted into coffee machine."""
            print("Please insert coins.")
            quarters = int(input("how many quarters?: ")) * coins["quarter"]
            dimes = int(input("how many dimes?: ")) * coins["dime"]
            nickels = int(input("how many nickels?: ")) * coins["nickel"]
            pennies = int(input("how many pennies?: ")) * coins["penny"]
            total_coins = [quarters, dimes, nickels, pennies]
            total_coins = sum(total_coins)
            return total_coins
        def calculate(choice):
            """Calculates the inserted coins and checks to see if machine has enough ingredients and enough money for
            drink purchase."""
            global money
            drink = MENU[choice]
            drink_cost = drink["cost"]
            for key, value in drink["ingredients"].items():
                if resources[key] < value:
                    print(f"Sorry there is not enough {key}")
                    return False
            inserted = insert_coin()
            if drink_cost <= inserted:
                    change = round(float(inserted - drink_cost), 2)
                    money += drink_cost
                    for key, value in drink["ingredients"].items():
                        resources[key] -= value
                    print(f"Here's your {choice}. and your change of ${change:.2f}, enjoy!")
                    return True
            else:
                print("Sorry that\'s not enough money. Money refunded.")
                return False

        if choice == "report":
            print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${money:.2f}")
        elif choice == "off":
            exit()
        elif choice in MENU:
            calculate(choice)
        else:
            print("Invalid input.")
