caloria = [
    {"name": "Apple", "Calories":  130},
    {"name": "Banana","Calories": 110 },
    {"name": "Avocado", "Calories":  50},
    {"name": "Cantaloupe","Calories": 50 },
    {"name": "Grapefruit", "Calories":  60},
    {"name": "Grapes","Calories":90 },
    {"name": "Honeydew Melon", "Calories":  50},
    {"name": "Lemon","Calories": 15 }
]
gyumölcs = input("item: ")



for gyömi in caloria:
    
    if gyumölcs.lower() == gyömi["name"].lower():
        print(gyömi["Calories"])

