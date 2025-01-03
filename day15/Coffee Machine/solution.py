import os
import time
from source import logo,emoji,MENU
defaultParameters={'water':300,
                   'milk':200,
                   'coffee':100,
                   }

money=0
cost=0
def makeCoffee(choice):
    global MENU,defaultParameters
    defaultParameters['water']-=MENU[choice]['ingredients']['water']
    defaultParameters['milk'] -= MENU[choice]['ingredients']['milk']
    defaultParameters['coffee']-=MENU[choice]['ingredients']['coffee']
    defaultParameters['coffee'] += MENU[choice]['cost']
def checkResource(choice):
    global water,milk,coffee
    hwllo=1
    if (choice == 'espresso'):
        if(water< 50):
            print("Sorry there is not enough water.")
            hwllo=0
        milk -= 0
        if(coffee < 18):
            print("Sorry there is not enough coffee.")
            hwllo = 0
    elif (choice == 'latte'):
        if(water < 200):
            print("Sorry there is not enough water.")
            hwllo = 0
        if(coffee < 24):
            print("Sorry there is not enough coffee.")
            hwllo = 0
        if(milk < 150):
            print("Sorry there is not enough milk.")
            hwllo = 0
    elif (choice == 'cappuccino'):
        if (water < 250):
            print("Sorry there is not enough water.")
            hwllo = 0
        if (coffee < 24):
            print("Sorry there is not enough coffee.")
            hwllo = 0
        if (milk < 200):
            print("Sorry there is not enough milk.")
            hwllo = 0
    if(hwllo):
        return True

    else:
        return False

def enoughMoney(choice,monetaryValue):
    fax=True
    if(choice=='espresso'):
        if(monetaryValue<1.50):
            fax = False
    if(choice=='latte'):
        if(monetaryValue<2.50):
            fax = False
    if(choice=='cappuccino'):
        if(monetaryValue<3.00):
            fax = False
    return fax
while(True):
    os.system('cls')

    print(logo)

    choice=input("What would you like? (espresso($1.50)/latte($2.50)/cappuccino($3.00):  ").lower()
    if(choice=='report'):
        print(f"Water: {water}ml")
        print((f"Milk: {milk}ml"))
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")
        time.sleep(8)
    elif(choice=="off"):
        os.system('cls')
        break
    elif(choice=='espresso' or choice=='latte' or choice=='cappuccino'   ):
        ok=checkResource(choice)
        if(ok):


            print("Insert the coins you have :)")
            quarters=int(input("Enter the number of quarters you have: "))
            dimes=int(input("Enter the number of dimes you have: "))
            nickles=int(input("Enter the number of nickels you have: "))
            pennies=int(input("Enter the number of pennies you have: "))
            monetaryValue=quarters*.25+dimes*.1+nickles*.05+pennies*.01
            shouldMakeCoffee=enoughMoney(choice,monetaryValue)
            if(shouldMakeCoffee):
                makeCoffee(choice)
                print(emoji)
                print("Here is your coffee .\nThanks for using the machine.")
                returnMoney =round(monetaryValue-cost,2)
                if(returnMoney>0):
                    time.sleep(5)
                    print(f"Here is your ${returnMoney} in return.")
                    time.sleep(4)
            else:
                print("Sorry, that's not enough money. Money Refunded.\nPlease try something different.")
                time.sleep(3)

        else:
            print("Please try something else.")
            time.sleep(3)

    else:
        print("Please enter a valid input.")
        time.sleep(3)

# # project14Day15:Coffee Machine
# 1.makes 3 hot flavours:
# espresso : 50 ml water, 18 g coffee : $1.50
# latte : 200 ml water 24g coffee 150 ml milk:: $2.50
# cappuccino: 250 ml water 24g coffee 100 ml milk: $3.00
#
# machine starts with: 300ml water , 200 ml milk , 100 gm coffee
#
# 2. coin operated: american coins: penny(1 cent=$.01),dime(10 cents=$0.1), nickel(5 cents$.05),quarter(25 cents$.25)
#
# #program requirements: 1.print report(how much what left)
# type report: see what left
# 2. check resources sufficient at order
# 3. process coins : not enough money , or how much money add and then tell the surplus .
# 4. check transactions successful: make coffee and deduct the resources, increase money
# 5.make coffee
#
