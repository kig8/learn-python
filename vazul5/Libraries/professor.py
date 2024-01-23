import random


def main():
    level = get_level()
    tasks = 2
    score = 0
    while tasks > 0:
        x,y = generate_integer(level)
       
        
        try:
            ansa = int(input(f"{x} + {y} ="))
        except ValueError:
            ansa = "s"
                
        if ansa == x + y:
            tasks = tasks - 1
            score = score + 1
            continue 

        elif True:
            error = 3    
            while True:
                if ansa != x + y:
                    error = error - 1
                    print("EEE")
                    try:
                        ansa = int(input(f"{x} + {y} =")) 
                    except ValueError:
                        pass    
                    if error == 0:
                        tasks = tasks - 1 
                        break
                    if ansa == x + y:
                        tasks = tasks -1
                        score = score + 1
                        break               
    if tasks == 0:
        print(f"score: {score}") 
               
def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if 1 <= lvl <= 3:
                return lvl
                
        except ValueError:
            continue
        
            
        else:
            continue
        '''  ha nem 1 ,2,3 akkor ujrakérdez'''  

def generate_integer(level):
    if level == 1:
        x  = random.randint(0,9)
        y  = random.randint(0,9)
        return x , y
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        return x , y
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
        return x , y
    ...
if __name__ == "__main__":
    main()
           