import os
import time
from source import logo,emoji,MENU
defaultParameters={'water':300,
                   'coffee':100,
                   'milk':200
                   }

money=0
cost=0
def makeCoffee(choice):
    '''process the choosen coffee, increases money'''
    global MENU,defaultParameters,money,cost
    defaultParameters['water']-=MENU[choice]['ingredients']['water']
    defaultParameters['milk'] -= MENU[choice]['ingredients']['milk']
    defaultParameters['coffee']-=MENU[choice]['ingredients']['coffee']
    money += MENU[choice]['cost']
    cost= MENU[choice]['cost']


def inputMoney():
    '''inputs coins and return the processed total money'''
    print("Insert the coins you have :)")
    quarters = int(input("Enter the number of quarters you have: "))
    dimes = int(input("Enter the number of dimes you have: "))
    nickles = int(input("Enter the number of nickels you have: "))
    pennies = int(input("Enter the number of pennies you have: "))
    monetaryValue = quarters * .25 + dimes * .1 + nickles * .05 + pennies * .01
    # monetaryValue = int(input("Enter the number of quarters you have: ")) * .25 + int(
    #     input("Enter the number of dimes you have: ")) * .10 + int(
    #     input("Enter the number of nickels you have: ")) * 5 + int(
    #     input("Enter the number of pennies you have: ")) * .01
    return monetaryValue


def checkResource(choice):
    '''it basically will take the choice and return true or false on the basis of if there is enough resources for the thing ordered.'''
    hwllo=1
    global MENU,defaultParameters
    for item in defaultParameters:
        if(defaultParameters[item]<MENU[choice]['ingredients'][item]):
            print(f"Sorry, there i not enough {item}.")
            hwllo=0

    if(hwllo):
        return True

    else:
        return False

def enoughMoney(choice,monetaryValue):
    '''check if there is enough money entered and returns true or false'''
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
        print(f"Water: {defaultParameters['water']}ml")#we have to print g and ml otherwise this would have been handled by a single print statement.
        print((f"Milk: {defaultParameters['milk']}ml"))#otherwise would have been for ingredient in defaultParameters: print...........
        print(f"Coffee: {defaultParameters['coffee']}g")
        print(f"Money: ${money}")
        time.sleep(5)
    elif(choice=="off"):
        os.system('cls')
        break
    elif(choice=='espresso' or choice=='latte' or choice=='cappuccino'   ):
        ok=checkResource(choice)
        if(ok):
            monetaryValue=inputMoney()

            shouldMakeCoffee=enoughMoney(choice,monetaryValue)
            if(shouldMakeCoffee):
                makeCoffee(choice)
                print(emoji)
                time.sleep(2)
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

