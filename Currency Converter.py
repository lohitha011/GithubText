import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

# Function to perform currency conversion
def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    
    result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")

# Create GUI window
window = tk.Tk()
window.title("Currency Converter")

# Currency options
currencies = ["USD", "EUR", "JPY", "GBP", "INR"]

from_currency_combobox = ttk.Combobox(window, values=currencies)
from_currency_combobox.set("USD")
from_currency_combobox.pack()

to_currency_combobox = ttk.Combobox(window, values=currencies)
to_currency_combobox.set("EUR")
to_currency_combobox.pack()

amount_label = tk.Label(window, text="Amount:")
amount_label.pack()

amount_entry = tk.Entry(window)
amount_entry.pack()

convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
