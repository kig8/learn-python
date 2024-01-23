import random
def main():
    nmax = max()
    number = random.randint(1,nmax)
    
    while True:      
    
        try:          
          
            guess = int(input("Guess: "))

            if guess <= 0:
                continue
            
        except ValueError:
                continue
    
        if guess == number:
            print("Just right!")
            break

        elif guess > number:
            print("Too large!  ")
            continue
        else:
            print("Too small!")
            continue


def max():
    while True:
        try:

            n = int(input("level: "))
            
        except ValueError:
            continue    
        if n <= 1:
            continue
        else:
            return n
        
main()