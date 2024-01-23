# input ami mm dd yyyy 

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
] 
new_list = [elem[:3] for elem in month]


l = input("Dates: ").replace("/","-").replace("," , "-").replace(" ", "-")

x , y, z = l.split("-") 

print(x)
print(y)

# while True :
#    try:
#         if x.isnumeric() and 1 <= int(x) <= 12  and y.isnumeric() and 1 <= int(y) <= 31:
#             print(f"{z}-{x:02d}-{y:02d}")
#             break

#         elif x in month:
#             index = month.index(x) + 1
#             print(f"{z}-{index:02d}-{y:02d}")
#             break
   
#         elif x in new_list:
#             new_index = new_list.index(x) + 1 
#             print(f"{z}-{new_index:02d}-{y:02d}")
#             break
      
#    except ValueError:
#        pass
  

     
    
        
