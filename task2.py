import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showwarning("Warning", "Length should be a positive integer.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        password_var.set(password)
    except ValueError:
        messagebox.showwarning("Warning", "Invalid input. Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root)
frame.pack(pady=20)

length_label = tk.Label(frame, text="Enter the desired length for the password:")
length_label.pack(side=tk.LEFT, padx=10)

length_entry = tk.Entry(frame, width=5)
length_entry.pack(side=tk.LEFT, padx=10)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.pack(side=tk.LEFT, padx=10)

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Helvetica", 12))
password_label.pack(pady=20)

root.mainloop()