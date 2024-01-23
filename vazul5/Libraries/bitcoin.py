import sys 
import requests
 
try:
    json_b = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bit =  json_b.json()
except requests.RequestException:
    print("nem tudom mien hiba történhet de nek kérte le rendesen az adatokat")
    sys.exit()


def main():
    flo = bit["bpi"]["USD"]["rate_float"]
    valuta_USD = valuta()
    b_valu =  valuta_USD * flo
    
    
    print(f"${b_valu:,.4f}")


def valuta():

    while True:
       
        if len(sys.argv) < 2:
            print("Missing command-line argument ")
            sys.exit()
        elif len(sys.argv) > 2:
            print("too many command-line argument ")
            sys.exit()

        else:   
            try:
                dolar = float(sys.argv[1])
                return dolar
        
            except ValueError:
                print("Command-line argument is not a number")
                sys.exit()

        



main()