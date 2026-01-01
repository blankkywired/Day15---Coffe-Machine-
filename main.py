
# first step
resources_InititalValues = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cost": 0
}

coffee_options = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "cost": 1.50
        }
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
            "cost": 2.50
        }
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
            "cost": 3.50
        }
    }
}
revenue = 0

def off_machine(value):
    return value == 'off'
def resources_catalog(answer):
    """Display machine resources to the user.Exibe resources"""
    if answer == "report":
        print('----------RESOURCES----------')
        for i in resources_InititalValues:
            if i != "cost":
                print(f"{i.capitalize()}: {resources_InititalValues[i]}ml")
            else:
                print(f"{i.capitalize()}: ${resources_InititalValues[i]}")
        print('\n')
    elif answer == "catalog":
        print('----------CATALOG----------')
        for coffee in coffee_options:
            #print(coffee)
            print(coffee.upper()) # Exibir nome do café
            for ingredients in coffee_options[coffee]:
                for components in coffee_options[coffee][ingredients]: #Percorrer dentro do dicionario de ingredients de cada café
                    print( components , coffee_options[coffee][ingredients][components])
            print('\n')

#Implementar opção de aceitar moedas com base na escolha de cafe do usuario 
totalSum = 0
def insert_coins():
    global totalSum
    """Colect coins of the user to procced with the buyment"""
    print('Please insert coins')
    quarters = float(input('How many quarters?: ')) * 0.25
    dimes = float(input('How many dimes?: ')) * 0.10
    nickles = float(input('How many nickles?: ')) * 0.05
    pennies = float(input('How many pennies?: ')) * 0.01

    totalSum = quarters + dimes + nickles + pennies
    print(f"${totalSum:.2f}")
    #AMOUNT
    return totalSum


def find_coffee_price(choice):
    global coffee_cost
    for coffee in coffee_options:
        if coffee == choice:
            order = coffee_options[choice]['ingredients']
            for components in order:
                    if components == "cost":
                        coffee_cost = coffee_options[choice]['ingredients'][components]
                        return coffee_cost

def transaction(coffe_choosen_price, amount):
    """Check if the buyment can be executed with successfully"""
    
    if coffe_choosen_price > amount:
        print("Sorry, that's no enough money. Money refunded")
        print(f"Coffee value: ${(coffe_choosen_price):.2f}. Amount: ${(amount):.2f}")
        return False
    else:
        #Troco do usuario
        if (amount - coffe_choosen_price) > 0:
            exchange = amount - coffe_choosen_price
            print(f"Here's your ${round(exchange , 2)} in change")

        return True
       # making_coffee(choice)
def resources_sufficient(coffee):
    order = coffee_options[coffee]['ingredients']
    for item in order:
       if order[item] >  resources_InititalValues[item]:
            print('Sorry, there is no more resources enough')
            return False
       else:
           return True

def make_coffee(coffee):
    global revenue

    order = coffee_options[coffee]['ingredients']
    for item in order:
        if item != 'cost':
            resources_InititalValues[item] = resources_InititalValues[item] - order[item]
        else:
            resources_InititalValues[item] = resources_InititalValues[item] + order[item] #Adicionando os valores que a maquina recebe
            
    print(f"Here's your coffee. Enjoy your {choice} ☕!")
    

choice = ""
while True:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if choice == "off":
        break
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if resources_sufficient(choice):
            if transaction(find_coffee_price(choice), insert_coins()):
                make_coffee(choice)
    elif choice == "report":
        resources_catalog(choice)

    
