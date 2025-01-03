# OOP: object-oriented programming: when our code starts getting complex. Procedural Programming becomes complex when
# we have to perform multiple actions , according to our program requirements it is one of the oldest method.
# maintaining simple relationship while dealing with complex problems. for example project 14 has followed procedural
# programming and so there is little bit complexities we basically cannot create large project or things using the
# procedural programming easily. for example : car : we can have different guys or teams working on different part of
# car, or ppp is similar to one man restaurant. while in large restaurants , we have different guy who knows their
# work well , "their work"
# we use same concept to make our complex project scalable
# it is called oop because it is trying to model a real life object
# class is basically datatype of the object
# class is the blueprint used to model objects

# from turtle import Turtle, Screen
# abhi = Turtle()
# abhi.color('red')
# abhi.shape("turtle")
# print(abhi)
# abhi.forward(100)  # here we are using these methods of class turtle
# myScreen = Screen()  # 300 height and width by default
# print(myScreen.canvheight)
# myScreen.exitonclick()
# read things from turtle graphics from python module.

# about prettyTable: installing python package . basically pyPI or python Package index allows users to search for
# packages by keywords or by filters against their metadata
from prettytable import PrettyTable

table = PrettyTable()
print(table)
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
print(table)
# we can even change the attributes of an object too
# means we can basically change the things about the table style here
print(table.align)
table.align = 'l'
print(table.align)
print(table)
# seen creating object from the classes, using methods or functions, and changing attributes of objects
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
