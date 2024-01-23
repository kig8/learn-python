
name = input("name?")
   

for c in name: 
    snake = c if c.islower() else "_" + c
    snake = snake.lower()
    print(snake, end = "")