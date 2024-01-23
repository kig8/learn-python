szám=input("")

x, y, z = szám.split(" ")
x = float(x)
z = float(z)

if y == "*":
     vége = x * z

elif y == "-":
    vége = x-z


elif y == "+":
     vége = x + z

elif y == "/" :
     if z != 0:
         vége = x / z  
     else:
          vége="n"      
else :
        vége = "h"


if vége=="h":
     print("hiba")
elif vége == "n":
     print("0 val nem")     
    
else:
    print(f"{vége:.1f}")