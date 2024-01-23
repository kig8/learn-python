import sys 

def main():
    count = 0
    py_file = comand()
    try:
        with open(py_file) as file:
            for line in file:
                if line.rstrip() and not line.startswith("#"):
                    count = count + 1
                #if line.startswith("#"):
                    #count = count - 1  

            print(count)
    except FileNotFoundError:
        sys.exit
    except TypeError:
        sys.exit
def comand():
    
    while True:
            if len(sys.argv) < 2:
                print("Too few command-line arguments  ")
                break

            elif len(sys.argv) > 2:
                print("to many command-line arguments") 
                break
            elif not sys.argv[1].endswith(".py"):
                print("Not a Python file ")
                break

            else:
                return  sys.argv[1]
if __name__ == "__main__":
    main()
        