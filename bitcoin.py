import requests
import sys
import json

try:
     if len(sys.argv)==1:
         sys.exit("Missing command-line argument")

     elif len(sys.argv)==2:
         if sys.argv[1].isalpha():
             sys.exit("Command-line argument is not a number")

         else:
             number=float(sys.argv[1])
             response=requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0df5000e7f624bd255cfca7530659ab39c5808f0110ac3f444ecf4c49b79fc32")
             response=response.json()
             current=float(response['data']['priceUsd'])
             value=(number*current)
             print(f"${value:,.4f}")

     else:
         print("invalid input")

except requests.RequestException:
    sys.exit("error")
