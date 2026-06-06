# Python Restaurant Management System

# This is a beginner-friendly Python project that simulates a simple restaurant ordering system.
# The program displays a menu, allows customers to place orders, and automatically calculates the total bill based on selected items. 
# It demonstrates the use of Python dictionaries, conditional statements, user input handling, and basic billing logic.



# Define the menu of the restaurant


menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

# Greet
print("Welcome to our PYTHON Restaurant")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

order_total = 0
item_1 = input("Enter the name of item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet !!")

another_order = input("Do you want to add another item? (Yes/no) ").lower()
if another_order == "yes":
    item_2 = input("Enter the name of second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")
        
print(f"The total amount of items to pay is {order_total}")




