
from tabulate import tabulate
import csv
import sys

def main():
    konak = open_csv()
    headors = konak[0].keys()
    konak_fin = [list(row.values()) for row in konak]
    print(tabulate(konak_fin, headers=headors,tablefmt="grid"))
   
   
    
def open_csv():
    comand_line = comand()
    with open(comand_line, 'r', newline='', encoding='utf-8') as file:
       read  = csv.DictReader(file)
       list_dict = []
       for row in read:
           list_dict.append(row)
    return list_dict   
  

def comand():
        
    if len(sys.argv) < 2:
        print("Too few command-line arguments  ")
        sys.exit()

    elif len(sys.argv) > 2:
        print("to many command-line arguments") 
        sys.exit()
    elif not sys.argv[1].endswith(".csv"):
        print("Not a csv file ")
        sys.exit()

    else:
        return  sys.argv[1]


if __name__ == "__main__":
    main()