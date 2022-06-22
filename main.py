from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class VendingMachine:
    menu = Menu()
    coffee_maker = CoffeeMaker()
    coffee_type = menu.get_items()
    machine = True

    def run_vending_machine(self):
        while self.machine:
            choice = input(f"What would you like? ({self.coffee_type}): ")
            if choice == "off":
                print("Machine is off")
                self.machine = False
            elif choice == "report":
                print(self.coffee_maker.report())
            elif choice in self.coffee_type:
                self.process_order(choice)

    def process_order(self, choice):
        print(choice)


# Run program
machine = VendingMachine()
machine.run_vending_machine()
