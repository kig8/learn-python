
szám=input("")

x, y, z = szám.split(" ")
x = float(x)
z = float(z)

match y:
    case "/":
         if   z != 0: 
                vége = x / z
         else:
              vége="n"

    case "*":
        vége = x * z
    case "-":
        vége = x - z
    case "+":
        vége = x + z
    case _:
        vége = "h"
        
if vége=="n":
    print("0val ne")    
elif vége=="h":
    print("hiba") 
else:              
    print(f" {vége:.1f}")


