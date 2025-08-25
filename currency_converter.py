import tkinter as tk
import requests

def on_convert():
    try:
        amount = float(amount_entry.get())
        from_curr = from_entry.get().upper()
        to_curr = to_entry.get().upper()
        
        result = convert_currency(amount, from_curr, to_curr)
        if result:
            result_label.config(text=f"{amount} {from_curr} = {result:.2f} {to_curr}")
        else:
            result_label.config(text="Conversion failed. Check currency codes.")
    except ValueError:
        result_label.config(text="Please enter a valid amount.")


# Function called when button is clicked
def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    data = response.json()

    # Debugging: print the API response
    print(data)

    if data.get("info") and data.get("result"):
        return data["result"]
    else:
        return None


# Tkinter UI
root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="From Currency:").grid(row=1, column=0)
from_entry = tk.Entry(root)
from_entry.grid(row=1, column=1)

tk.Label(root, text="To Currency:").grid(row=2, column=0)
to_entry = tk.Entry(root)
to_entry.grid(row=2, column=1)

convert_btn = tk.Button(root, text="Convert", command=on_convert)
convert_btn.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
