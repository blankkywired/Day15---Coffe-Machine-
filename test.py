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
#choice = input()
def find_value():
    for i in range(0, len(coffes_options)):
        for j in coffes_options[i]:
            if j == "name" or j == "money":
                print(coffes_options[i][j])


#find_value()

#index of the coffee options
list_coffees = []
choiceUser = input("")
for coffee in coffes_options:
    for flavour in coffee:
        if coffee["name"] == choiceUser:
            print("Café encontrado" , coffee["money"])
            break
   
            


                    



        


