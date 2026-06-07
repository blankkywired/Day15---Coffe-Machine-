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
def show_resources_catalog(answer):
    for coffee in coffee_options:
        #print(coffee)
        print(coffee.upper()) # Exibir nome do café
        for ingredients in coffee_options[coffee]:
            for components in coffee_options[coffee][ingredients]: #Percorrer dentro do dicionario de ingredients de cada café
                print( components , coffee_options[coffee][ingredients][components])
        print('\n')

choice = input("insert a coffee name: ")

#Pesquisar preço
def find_coffee_price():
    
    for coffee in coffee_options:
        if coffee == choice:
            for ingredients in coffee_options[coffee]:
                for components in coffee_options[coffee][ingredients]:
                    if components == "cost":
                        coffee_cost = coffee_options[coffee][ingredients][components]
    
                        return coffee_cost
print(find_coffee_price())


order = coffee_options["cappuccino"]['ingredients']['cost']
print(order)
    

        


