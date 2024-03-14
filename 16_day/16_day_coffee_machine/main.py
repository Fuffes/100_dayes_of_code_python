from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

menu = Menu()
coffee_machine = CoffeeMaker()
coffee_machine.report()
money_machine = MoneyMachine()
money_machine.report()


while is_on:
    chose = input(f"What would you like? {menu.get_items()}?").lower()

    drink = menu.find_drink(order_name=chose)

    if chose == "off":
        is_on = False
    elif chose == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(order=drink)
        else:
            print("Sorry there is not enough.")
            is_on == True


