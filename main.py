# first step

coffes_options = [
    {
        "name": "espresso",
        "water": 50,
        "coffee": 18,
        "price": 1.50
    },

    {
        "name": "late",
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "price": 2.50
    },

    {
        "name": "cappucciono",
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price": 3.50
    }
]

#Statement to print any components value

#or i in coffees[1]:
#    print(coffees[1][i])


for i in range(len(coffes_options)):
    for j in coffes_options[i]:
        print(f"{j}:", coffes_options[i][j])
    print('\n')

