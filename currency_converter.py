import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    data = response.json()
    if data.get("result"):
        return data["result"]
    
    else:
        return "Error fetching data."
    

    
amount =float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD): ").upper()
to_currency = input("To currency (e.g., LKR): ").upper()

result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {result} {to_currency}")

