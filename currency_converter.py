import tkinter as tk
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


#GUI setup#

root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)


tk.Label(root, text="From:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1)


tk.Label(root, text="To:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1)

convert_btn = tk.Button(root, text="Convert" , command=convert_currency)
convert_btn.grid(row=3, column=0, columnspan=2)
    

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.grid(row=4, column=0, columnspan=2, pady=10)
    
root.mainloop()

