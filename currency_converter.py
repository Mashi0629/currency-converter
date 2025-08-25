import tkinter as tk
from tkinter import ttk
import requests

# Function to fetch rates
def get_rates(base="USD"):
    try:
        url = f"https://open.er-api.com/v6/latest/{base}"
        response = requests.get(url)
        data = response.json()
        if data.get("result") == "success":
            return data["rates"]
    except Exception as e:
        print("Error fetching rates:", e)
    return {}

# Conversion function
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return None
    usd_amount = amount / rates[from_currency]
    return usd_amount * rates[to_currency]

# On Convert button click
def on_convert():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        result = convert_currency(amount, from_curr, to_curr, rates)
        if result:
            result_label.config(
                text=f"{amount} {from_curr} = {result:.2f} {to_curr}", fg="#1a73e8"
            )
        else:
            result_label.config(text="❌ Conversion failed. Check codes.", fg="red")
    except ValueError:
        result_label.config(text="⚠️ Please enter a valid number.", fg="red")

# Swap button
def swap_currencies():
    f = from_currency.get()
    t = to_currency.get()
    from_currency.set(t)
    to_currency.set(f)

# ---------------- UI ----------------
root = tk.Tk()
root.title("💱 Currency Converter")
root.geometry("400x350")
root.configure(bg="#f4f6f9")

# Fetch rates
rates = get_rates("USD")
currencies = sorted(rates.keys()) if rates else ["USD", "LKR", "INR", "EUR"]

# Title/Header
header = tk.Label(
    root, text="Currency Converter", font=("Helvetica", 18, "bold"), bg="#1a73e8", fg="white", pady=10
)
header.pack(fill="x")

# Main frame
frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.55, anchor="center", width=350, height=230)

# Amount
tk.Label(frame, text="Amount:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
amount_entry = tk.Entry(frame, font=("Arial", 12), width=15, bd=2, relief="solid")
amount_entry.grid(row=0, column=1, pady=10)

# From Currency
tk.Label(frame, text="From:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
from_currency = ttk.Combobox(frame, values=currencies, state="readonly", font=("Arial", 11))
from_currency.grid(row=1, column=1, pady=10)
from_currency.set("USD")

# To Currency
tk.Label(frame, text="To:", font=("Arial", 12), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
to_currency = ttk.Combobox(frame, values=currencies, state="readonly", font=("Arial", 11))
to_currency.grid(row=2, column=1, pady=10)
to_currency.set("LKR")

# Swap Button
swap_btn = tk.Button(frame, text="🔄 Swap", command=swap_currencies, bg="#fbbc05", fg="black",
                     font=("Arial", 11, "bold"), relief="flat", padx=10, pady=2, cursor="hand2")
swap_btn.grid(row=1, column=2, padx=5)

# Convert Button
convert_btn = tk.Button(frame, text="Convert", command=on_convert, bg="#1a73e8", fg="white",
                        font=("Arial", 12, "bold"), relief="flat", padx=10, pady=5, cursor="hand2")
convert_btn.grid(row=3, column=0, columnspan=3, pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f4f6f9")
result_label.pack(pady=15)

root.mainloop()
