def main():
    fruit = input("Item: ")
    calories = get_calories(fruit)
    print(calories) if calories is not None else None


def get_calories(f):
    fruit_calorie_dict = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80,
    }

    # dict comprehension
    temp_fruits = {key.lower(): fruit_calorie_dict[key] for key in fruit_calorie_dict}

    if f.lower() in temp_fruits:
        return f"Calories: {temp_fruits[f.lower()]}"
    else:
        return


main()
