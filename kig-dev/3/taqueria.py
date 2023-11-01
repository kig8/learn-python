def main():
    taqueria_items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    add_item(taqueria_items)


def add_item(items):
    total = 0

    while True:
        try:
            inp = input("Item: ").title()
            item_price = items[inp]
        except KeyError:
            pass
        except EOFError:
            break
        else:
            total += item_price
            print(f"${total:.2f}")


main()
