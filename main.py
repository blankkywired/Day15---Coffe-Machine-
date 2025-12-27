# first step
resources_InititalValues = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coinsValues = [{"quarters": 0.25}, {"dimes": 0.10}, {"nickles": 0.05}, {"pennies": 0.01}]
#for i in range(len(coinsValues)):
 #   for j in coinsValues[i]:
 #       print(coinsValues[i][j])
#print(coinsValues[3]["pennies"])

coffes_options = [
    {
        "name": "espresso",
        "water": 50,
        "coffee": 18,
        "money": 1.50
    },

    {
        "name": "latte",
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "money": 2.50
    },

    {
        "name": "cappuccino",
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "money": 3.50
    }
]


def showResources_and_catalog(answer):
    """Display machine resources to the user.Exibe resources"""
    if answer == "report":
        print('----------RESOURCES----------')
        for i in resources_InititalValues:
            if i != "money":
                print(f"{i.capitalize()}: {resources_InititalValues[i]}ml")
            else:
                print(f"{i.capitalize()}: ${resources_InititalValues[i]}")
        print('\n')
    elif answer == "catalog":
        print("----------CATALOG----------")
        for i in range(len(coffes_options)):
            for j in coffes_options[i]:
                print(f"{j}:", coffes_options[i][j])
            print('\n')

#Implementar opção de aceitar moedas com base na escolha de cafe do usuario 
def insert_coins():
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

userChoice = ""
def main():
    global userChoice
    userChoice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    showResources_and_catalog(userChoice)

    if userChoice == "espresso" or userChoice == "latte" or userChoice == "cappuccino":
        transaction(find_coffee_price(userChoice), insert_coins())        
        return userChoice
        
    
def find_coffee_price(coffee_option):
    """Find the price of coffee based on the user's choice."""
     #Guardando escolha do usuario
    for coffee in coffes_options:
        for name in coffee:
            if coffee["name"] == coffee_option:
                coffee_price = coffee["money"]
    
    return coffee_price

def transaction(coffe_choosen_price, amount):
    if coffe_choosen_price > amount:
        print("Sorry, that's no enough money. Money refunded")
        print(f"Coffee value: {coffe_choosen_price}. Amount:{amount}")

    else:
        #Troco do usuario
        if (amount - coffe_choosen_price) > 0:
            exchange = amount - coffe_choosen_price
            print(f"Here's your ${round(exchange)} in change")
        print(f"Here's your coffee. Enjoy your {userChoice} ☕!")




main()

#TODOS: IMPLEMENTAR A FEATURE DE PEGAR O CAFE ESCOLHIDO PELO USUARIO E SUBTRAIR OS VALORES DOS RECURSOS NECESSARIOS
# 2 - ADICIONAR FEATURE PARA ACEITAR MOEDAS DO USUARIO