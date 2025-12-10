# first step

coffees = [
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

for i in range(len(coffees)):
    for j in coffees[i]:
        print(coffees[i][j])
