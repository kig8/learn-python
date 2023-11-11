import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")

try:
    arg_usd = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.RequestException:
    sys.exit("something went wrong")

btc_usd = r["bpi"]["USD"]["rate_float"]
result = arg_usd * float(btc_usd)
print(f"{result:,.4f}")
