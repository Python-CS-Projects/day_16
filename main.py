from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class VendingMachine:
    menu = Menu()
    coffee_maker = CoffeeMaker()
    coffee_type = menu.get_items()
    money_machine = MoneyMachine()
    machine = True

    def run_vending_machine(self):
        while self.machine:
            choice = input(f"What would you like? ({self.coffee_type}): ")
            if choice == "off":
                print("Machine is off")
                self.machine = False
            elif choice == "report":
                print(self.coffee_maker.report())
                print(self.money_machine.report())
            elif choice in self.coffee_type:
                menu_item = self.menu.find_drink(choice)
                self.process_order(menu_item)

    def process_order(self, menu_item):
        enough_resources = self.coffee_maker.is_resource_sufficient(menu_item)
        if enough_resources:
            cost = menu_item.cost
            print(f"Please pay: ${cost}")
            is_payment_successful = self.money_machine.make_payment(cost)
            if is_payment_successful:
                self.coffee_maker.make_coffee(menu_item)
        else:
            print("Sorry there is not enough water")


# Run program
machine = VendingMachine()
machine.run_vending_machine()
