acceptable_coins = [5, 10, 25]
coke_price = 50
inserted_amount = 0

while inserted_amount <= coke_price:
    add_coin = int(input("Insert coin: "))

    if add_coin in acceptable_coins:
        inserted_amount += add_coin

    if coke_price - inserted_amount > 0:
        print(f"Amount due: {coke_price - inserted_amount}")

if inserted_amount >= coke_price:
    print(f"Change owed: {-coke_price + inserted_amount}")
