menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
mony= 0 
while True:
    try:
        order = input("Item: ").strip()
    except EOFError:
      break

    for kay in menu:
        if kay.lower() == order.lower():
            mony += menu[kay]
            print(f"Total {mony:.2f}")
            break
        if kay.lower() != order.lower():
            pass