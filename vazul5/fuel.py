while True:
    try:  
        f = input("Fraction: ")
        parts = f.split('/')
        x = int(parts[0])
        y = int(parts[1])
        percent = round(x / y, 2 ) * 100
        if percent > 100:
            pass
            
        
        else:
            if 1< percent < 99:
                print(f"{round(percent)}" "%")
                break
            elif percent <= 1:
                print("E")
                break
            elif percent >= 99:
                print("F")
                break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass        
    
       
   
