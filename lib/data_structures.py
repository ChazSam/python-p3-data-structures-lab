# import ipdb

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy = [n["name"] for n in spicy_foods]
    return spicy
   

def get_spiciest_foods(spicy_foods):
    spiciest = [n for n in spicy_foods if n['heat_level'] > 5 ]
    return spiciest


def print_spicy_foods(spicy_foods):
    for n in spicy_foods:
        print(f"{n['name']} ({n['cuisine']}) | Heat Level: {n['heat_level'] * '🌶'}" )


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for n in spicy_foods:
        if n['cuisine'] == cuisine:      
            return n
   

def print_spiciest_foods(spicy_foods):
    for n in spicy_foods:
        if n['heat_level'] > 5:
            print(f"{n['name']} ({n['cuisine']}) | Heat Level: {n['heat_level'] * '🌶'}" )

def get_average_heat_level(spicy_foods):
    average=0
    for n in spicy_foods:
        average += n['heat_level']

    return average / len(spicy_foods)
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
