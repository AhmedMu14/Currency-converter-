import tkinter as tk
import requests

def convert_currency():
    amount = entry_amount.get()
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()

    if amount:
        try:
            amount = float(amount)
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                exchange_rate = data['rates'][to_currency]
                converted_amount = amount * exchange_rate
                result_label.config(text=f"{converted_amount:.2f} {to_currency}")
            else:
                result_label.config(text="Error fetching data. Please try again.")
        except (ValueError, KeyError):
            result_label.config(text="Invalid input or currency.")
    else:
        result_label.config(text="Please enter an amount.")

root = tk.Tk()
root.title("Real-Time Currency Converter")

from_currency_var = tk.StringVar()
to_currency_var = tk.StringVar()
from_currency_var.set("USD")
to_currency_var.set("PKR")

# List of currencies including PKR
currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "PKR"]

label_amount = tk.Label(root, text="Enter Amount:")
label_amount.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=10, pady=10)

label_from = tk.Label(root, text="From Currency:")
label_from.grid(row=1, column=0, padx=10, pady=10, sticky="w")

from_currency_menu = tk.OptionMenu(root, from_currency_var, *currencies)
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

label_to = tk.Label(root, text="To Currency:")
label_to.grid(row=2, column=0, padx=10, pady=10, sticky="w")

to_currency_menu = tk.OptionMenu(root, to_currency_var, *currencies)
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", bd=2, relief="sunken", width=30, height=2, anchor="w", padx=10, pady=10)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

