import tkinter as tk
from tkinter import ttk
import requests

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    data = response.json()

    # Debugging: print the full API response in terminal
    print(data)

    if data.get("info") and data.get("result"):
        return data["result"]
    else:
        return None

# Function for button click
def on_convert():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        
        result = convert_currency(amount, from_curr, to_curr)
        if result:
            result_label.config(
                text=f"{amount} {from_curr} = {result:.2f} {to_curr}"
            )
        else:
            result_label.config(text="❌ Conversion failed. Check currency codes.")
    except ValueError:
        result_label.config(text="⚠️ Please enter a valid amount.")

# ---------------- UI ----------------
root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x250")

# Amount
tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, pady=5)

# Currency list
currencies = ["USD", "EUR", "GBP", "LKR", "JPY", "AUD", "CAD", "INR"]

# From Currency
tk.Label(root, text="From Currency:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
from_currency = ttk.Combobox(root, values=currencies, state="readonly")
from_currency.grid(row=1, column=1, pady=5)
from_currency.set("USD")  # default

# To Currency
tk.Label(root, text="To Currency:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
to_currency = ttk.Combobox(root, values=currencies, state="readonly")
to_currency.grid(row=2, column=1, pady=5)
to_currency.set("LKR")  # default

# Convert Button
convert_btn = tk.Button(root, text="Convert", command=on_convert)
convert_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
