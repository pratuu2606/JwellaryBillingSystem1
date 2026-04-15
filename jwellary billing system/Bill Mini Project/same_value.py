import tkinter as tk

def update_entry2(*args):
    # Update the second entry with the value of the first entry
    entry2_var.set(entry1_var.get())

# Create the main application window
root = tk.Tk()
root.title("Entry Synchronization Example")

# Create StringVar objects to hold the values of the entries
entry1_var = tk.StringVar()
entry2_var = tk.StringVar()

# Create the first entry widget
entry1 = tk.Entry(root, textvariable=entry1_var)
entry1.pack(padx=10, pady=10)

# Create the second entry widget
entry2 = tk.Entry(root, textvariable=entry2_var)
entry2.pack(padx=10, pady=10)

# Bind the update function to the first entry's content change
entry1_var.trace_add("write", update_entry2)

# Start the Tkinter event loop
root.mainloop()
