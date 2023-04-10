from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def prompt_user():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while True:
        print("What would you like? ")
        text_input = input(f"({menu.get_items()}):")
        if text_input == "off":
            return
        if text_input == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        selected_drink = menu.find_drink(text_input)
        if selected_drink is not None:
            if coffee_maker.is_resource_sufficient(selected_drink):
                if money_machine.make_payment(selected_drink.cost):
                    coffee_maker.make_coffee(selected_drink)

            
if __name__ == "__main__":
    prompt_user()
