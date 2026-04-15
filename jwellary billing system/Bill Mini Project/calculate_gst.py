import tkinter as tk
from tkinter import ttk

def calculate_gst(*args):
    try:
        amount = float(amount_var.get())
        gst_rate = float(gst_rate_var.get())
        gst_amount = amount * (gst_rate / 100)
        total_amount = amount + gst_amount
        
        gst_var.set(f"{gst_amount:.2f}")
        total_var.set(f"{total_amount:.2f}")
    except ValueError:
        gst_var.set("Invalid input")
        total_var.set("Invalid input")

# Set up the main application window
root = tk.Tk()
root.title("GST Calculator")

# Create StringVar instances for input and output
amount_var = tk.StringVar()
gst_rate_var = tk.StringVar()
gst_var = tk.StringVar()
total_var = tk.StringVar()

# Bind the StringVar to automatically call calculate_gst
amount_var.trace("w", calculate_gst)
gst_rate_var.trace("w", calculate_gst)

# Create and place the widgets
label_amount = ttk.Label(root, text="Enter Amount:")
label_amount.grid(column=0, row=0, padx=10, pady=10)

entry_amount = ttk.Entry(root, textvariable=amount_var)
entry_amount.grid(column=1, row=0, padx=10, pady=10)

label_gst_rate = ttk.Label(root, text="Enter GST Rate (%):")
label_gst_rate.grid(column=0, row=1, padx=10, pady=10)

entry_gst_rate = ttk.Entry(root, textvariable=gst_rate_var)
entry_gst_rate.grid(column=1, row=1, padx=10, pady=10)

label_gst_amount = ttk.Label(root, text="GST Amount:")
label_gst_amount.grid(column=0, row=2, padx=10, pady=10)

result_gst_amount = ttk.Label(root, textvariable=gst_var)
result_gst_amount.grid(column=1, row=2, padx=10, pady=10)

label_total_amount = ttk.Label(root, text="Total Amount:")
label_total_amount.grid(column=0, row=3, padx=10, pady=10)

result_total_amount = ttk.Label(root, textvariable=total_var)
result_total_amount.grid(column=1, row=3, padx=10, pady=10)

# Run the application
root.mainloop()

