

def main():
    Greeting =  input("Greeting: "). strip()
    ...
    finish = value(Greeting)
    print(finish)

def value(Greeting):
    ...
    if Greeting.lower().startswith("hello"):
       
        return "0$"

    elif Greeting.lower().startswith("h") :  
      
        return  "20$"

    else:
        
        return "100$"
      


if __name__ == "__main__":
    main()