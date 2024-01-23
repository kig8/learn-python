import sys
import csv 

def main():
    arg = comand()
    konak = open_csv()
       
    with open(sys.argv[2], 'w', newline='', encoding='utf-8') as file:
        csv_file = csv.writer(file)
        keys = ["first","last","hause"]
        csv_file.writerow(keys)
       
        for row in konak:
            last_name , first_name = row[0].split(", ")            
            hause = row[1]
            values = [first_name,last_name,hause]
            csv_file.writerow(values)
    

def open_csv():   
    with open(sys.argv[1], 'r', newline='', encoding='utf-8') as file:
       read  = csv.reader(file)
       list_dict = []
       for row in read:
           list_dict.append(row)
    return list_dict[1:] 

def comand():
    if len(sys.argv) < 3:
        print
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
     
        sys.exit("to many command-line arguments") 
    else:
        return  sys.argv
if __name__ == "__main__":
    main()