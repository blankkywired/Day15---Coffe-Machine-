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
        "name": "late",
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
coffee_list = []
# --------------------Adicionando opções de cafe para a lista ----------#
for i in range(len(coffes_options)):
    for j in coffes_options[i]:
        if j == "name":
            #print(coffes_options[i][j])
            coffee_list.append(coffes_options[i][j])

        else:
            continue

def showResources_and_catalog(answer):
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
def proccesCoins():
    quarters = float(input('How many quarters?: ')) * 0.25
    dimes = float(input('How many dimes?: ')) * 0.10
    nickles = float(input('How many nickles?: ')) * 0.05
    pennies = float(input('How many pennies?: ')) * 0.01

    totalSum = quarters + dimes + nickles + pennies
    print(f"${totalSum:.2f}")
    return totalSum

def main():
    userChoice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    showResources_and_catalog(userChoice)

    if userChoice == "espresso" or userChoice == "latte" or userChoice == "cappuccino":
        proccesCoins()
        return userChoice
    

#busca pelo preço com base no café escolhido
#Eu nao tenho ideia de como esse loop conseguiu retornar o exato valor do cafe escolhido pelo usuario apos chamar a função main
for i in range(0, len(coffee_list)):
    choice = main()
    for j in coffes_options[i]:
        if j == "money":
            print(coffes_options[i][j])


main()


#TODOS: IMPLEMENTAR A FEATURE DE PEGAR O CAFE ESCOLHIDO PELO USUARIO E SUBTRAIR OS VALORES DOS RECURSOS NECESSARIOS
# 2 - ADICIONAR FEATURE PARA ACEITAR MOEDAS DO USUARIO