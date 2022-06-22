from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class VendingMachine:
    coffee_type = ["latte", "cappuccino", "espresso"]
    machine = True

    while machine:
        choice = input("Please choose a coffee: ")
        if choice == "off":
            print("Machine is off")
            machine = False
        elif choice in coffee_type:
            print(choice)
