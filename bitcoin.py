import requests
import sys


try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = (response.json())
        rate = o["bpi"]["USD"]["rate"]
        rc = rate.replace(",", "")
        rate_float = float(rc)
        num = float(sys.argv[1])
        cost = num * rate_float
        print(f"${cost:,.4f}")

except requests.RequestException:
    pass
except ValueError:
    sys.exit("Command-line argument is not a number")