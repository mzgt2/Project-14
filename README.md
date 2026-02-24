# Project-14

## Coffee Machine Simulator ☕

A command-line coffee machine simulator that manages resources, processes payments, and dispenses drinks. Choose from espresso, latte, or cappuccino!

## Requirements

- Python 3.x
- No external libraries needed

## How to Run
```bash
python coffee_machine.py
```

## Available Drinks

| Drink | Water | Milk | Coffee | Cost |
|-------|-------|------|--------|------|
| **Espresso** | 50ml | 0ml | 18g | $1.50 |
| **Latte** | 200ml | 150ml | 24g | $2.50 |
| **Cappuccino** | 250ml | 100ml | 24g | $3.00 |

## Starting Resources

- Water: 300ml
- Milk: 200ml
- Coffee: 100g
- Money: $0.00

## How to Use

### Order a Drink
```
What would you like? (espresso/latte/cappuccino): latte

Please insert coins.
how many quarters?: 10
how many dimes?: 0
how many nickels?: 0
how many pennies?: 0

Here's your latte. and your change of $0.00, enjoy!
```

### Check Resources
```
What would you like? (espresso/latte/cappuccino): report

Water: 100
Milk: 50
Coffee: 76
Money: $2.50
```

### Turn Off Machine
```
What would you like? (espresso/latte/cappuccino): off
```

## Commands

- **espresso / latte / cappuccino** - Order a drink
- **report** - Display current resources and money collected
- **off** - Exit the program

## Payment System

The machine accepts US coins:
- **Quarter**: $0.25
- **Dime**: $0.10
- **Nickel**: $0.05
- **Penny**: $0.01

### Payment Process
1. Machine prompts for coin quantities
2. Calculates total inserted
3. Checks if sufficient funds provided
4. Dispenses drink and returns change (if applicable)
5. Refunds money if insufficient

## Features

- ✅ **Resource management** - Tracks water, milk, and coffee levels
- ✅ **Insufficient resource detection** - Alerts when ingredients run low
- ✅ **Coin processing** - Accepts multiple coin types
- ✅ **Change calculation** - Returns exact change to 2 decimal places
- ✅ **Transaction validation** - Checks if payment is sufficient
- ✅ **Money tracking** - Accumulates total revenue
- ✅ **Reporting** - View current machine status
- ✅ **Input validation** - Handles invalid drink selections

## Game Logic

1. **Check resources** - Verifies sufficient ingredients before accepting payment
2. **Process payment** - Calculates total coins inserted
3. **Validate transaction** - Compares payment to drink cost
4. **Deduct resources** - Reduces ingredient levels after successful purchase
5. **Add revenue** - Tracks total money collected

## Error Handling
```python
# Insufficient resources
"Sorry there is not enough water"

# Insufficient payment
"Sorry that's not enough money. Money refunded."

# Invalid input
"Invalid input."
```

## Example Session
```
What would you like? (espresso/latte/cappuccino): espresso
Please insert coins.
how many quarters?: 6
how many dimes?: 0
how many nickels?: 0
how many pennies?: 0
Here's your espresso. and your change of $0.00, enjoy!

What would you like? (espresso/latte/cappuccino): report
Water: 250
Milk: 200
Coffee: 82
Money: $1.50

What would you like? (espresso/latte/cappuccino): cappuccino
Please insert coins.
how many quarters?: 12
how many dimes?: 0
how many nickels?: 0
how many pennies?: 0
Here's your cappuccino. and your change of $0.00, enjoy!

What would you like? (espresso/latte/cappuccino): off
```

## What I Learned

Building this coffee machine taught me:

- **Nested data structures** - Working with dictionaries containing dictionaries
- **Resource management** - Tracking and deducting inventory dynamically
- **Financial calculations** - Handling money with proper rounding (`.2f` formatting)
- **Global variables** - Using `global` keyword to modify money across functions
- **Function design** - Creating reusable functions for coin insertion and calculations
- **Dictionary iteration** - Using `.items()` to check and modify resources
- **Conditional logic** - Validating resources and payments before processing
- **User input handling** - Processing various commands and drink selections

This project reinforced practical programming concepts like inventory systems and transaction processing.

Enjoy your virtual coffee! ☕
