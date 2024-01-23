
coin = int(input("Amount Due: 50\nInsert Coin:"))
cola = 50
now = 0
coins = [25,10,5]
# if coin not in coins:
#     print("Amount Due: 50")

    
# else:    
   
while True:
    if coin in coins:
        now = now + coin
    
    # if now == cola:
           
    #     print("Change Owed: 0 ")
    #     break
    
    elif now >= cola:
        change = now - cola
        print(f"Change Owe: {change}")
        break 

    elif now < cola:
        cola_now = cola - now
        if coin not in coins:
            
            print(f"Amount Due: {cola_now}")
            coin = int(input("ezaz Coin: "))
            continue

        if coin in coins:  
            print(f"LEGYENunt Due: {cola_now}")
            coin = int(input("Insert Coin: "))
            

