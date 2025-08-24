import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    print(data)
    
    if data.get("result") == "success":
        rates = data["rates"]
        if to_currency in rates:
            return amount * rates[to_currency]
        else:
            return f"Error: Currency {to_currency} not found."
    else:
        return "Error fetching data."
    
    
amount =float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD): ").upper()
to_currency = input("To currency (e.g., LKR): ").upper()

result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {result} {to_currency}")    

    


