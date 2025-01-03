# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
#
# while(True):
#     choice = input("What would you like: Espresso($1.50)/Latte($2.50)/Cappuccino($3.00)? : ").lower()
#     machine=CoffeeMaker()
#     money=MoneyMachine()
#     drinks=Menu()
#     drinks.__init__()
#     money.__init__()
#     machine.__init__()
#
#     if(choice=='report'):
#         machine.report()
#         money.report()
#     elif(choice=='off'):
#         break
#     elif(choice==  'show'):
#         print(drinks.get_items())
#     elif(choice=='search'):
#         what_to_search=input("What do you want to search? : ").lower()
#         print(f"Items available are: {drinks.find_drink(what_to_search)}.")
#     elif(choice=='espresso' or'latte' or'cappuccino'):
#         for item in drinks.menu:
#             if (item.name == choice):
#
#                 # global cost
#                 drink = item
#                 # print(drink)
#         checkResource= machine.is_resource_sufficient(drink)
#         if(checkResource):
#             # money_entered=money.process_coins()
#             # drinks.menu()
#             cost=0
#             for item in drinks.menu:
#                 if (item.name==choice):
#                     # global cost
#                     cost=item.cost
#             is_money_sufficient=money.make_payment(cost)
#             if(is_money_sufficient):
#                 for item in drinks.menu:
#                     if (item.name == choice):
#                         machine.make_coffee(item)
#
#             else:
#                 continue
#
#
#
#
#
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
