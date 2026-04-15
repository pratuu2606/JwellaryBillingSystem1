import tkinter as tk
from tkinter import messagebox
import random

class BillNumberGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing System")
        
        # Create GUI elements
        self.label = tk.Label(root, text="Current Bill Number:")
        self.label.pack(pady=10)
        
        # Entry widget to display the bill number
        self.bill_number_entry = tk.Entry(root, font=("Helvetica", 24), width=20)
        self.bill_number_entry.pack(pady=20)
        
        # Button to generate a new bill number
        self.generate_button = tk.Button(root, text="Generate New Bill Number", command=self.generate_random_bill_number)
        self.generate_button.pack(pady=20)
        
        # Button to exit the application
        self.exit_button = tk.Button(root, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=10)
    
    def generate_random_bill_number(self):
        # Generate a random bill number
        random_bill_number = random.randint(100000, 999999)  # Adjust range as needed
        # Update the entry box
        self.bill_number_entry.delete(0, tk.END)  # Clear the current entry
        self.bill_number_entry.insert(0, str(random_bill_number))  # Insert the new bill number

    def exit_app(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = BillNumberGenerator(root)
    root.mainloop()
