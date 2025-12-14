# first step
resources_InititalValues = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
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

userChoice = input('What would you like? (espresso/latte/cappuccino): ').lower()
if userChoice == "report":
    #Exibindo recursos iniciais
    print('-----------RESOURCES')
    for i in resources_InititalValues:
        print(f"{i.capitalize()}: {resources_InititalValues[i]}")
    print('\n')
    
#Implementar opção de aceitar moedas com base na escolha de cafe do usuario
elif userChoice == "espresso":


# --------------------Exibindo catálogo de cafés ----------#
for i in range(len(coffes_options)):
    for j in coffes_options[i]:
        print(f"{j}:", coffes_options[i][j])
    print('\n')

#TODOS: IMPLEMENTAR A FEATURE DE PEGAR O CAFE ESCOLHIDO PELO USUARIO E SUBTRAIR OS VALORES DOS RECURSOS NECESSARIOS
# 2 - ADICIONAR FEATURE PARA ACEITAR MOEDAS DO USUARIO