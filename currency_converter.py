import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    data = response.json()

    print(data)
    
    if data.get("result"):
        return data["result"]
    
    else:
        return "Error fetching data."
    

    


