import tkinter as tk
from tkinter import messagebox
import mysql.connector
import pandas as pd

# ==========================================
# OPTION A: The Contact Book (MySQL + Tkinter)
# ==========================================

def get_db_connection():
    """Helper function to establish DB connection. Update with your password."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password", # Update this
        database="contact_book_db"
    )

def save_contact():
    """TODO: Read data from entries, connect to DB, insert data, and clear entries."""
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    
    # 1. Check if name and phone are empty. If so, show a warning.
    # 2. Use a try-except block to connect to the DB and insert the record.
    # 3. Show a success message and clear the Entry widgets.
    pass

def view_contacts():
    """TODO: Fetch all contacts from DB and display in the Text widget."""
    # 1. Clear the text_area widget.
    # 2. Use a try-except block to connect to the DB and execute 'SELECT * FROM contacts'.
    # 3. Loop through the records and insert them into the text_area.
    pass

# ---- Tkinter GUI Setup for Option A ----
# root = tk.Tk()
# root.title("Contact Book")
# 
# tk.Label(root, text="Name:").pack()
# entry_name = tk.Entry(root)
# entry_name.pack()
# 
# tk.Label(root, text="Phone:").pack()
# entry_phone = tk.Entry(root)
# entry_phone.pack()
# 
# tk.Label(root, text="Email:").pack()
# entry_email = tk.Entry(root)
# entry_email.pack()
# 
# tk.Button(root, text="Save Contact", command=save_contact).pack(pady=5)
# tk.Button(root, text="View Contacts", command=view_contacts).pack(pady=5)
# 
# text_area = tk.Text(root, height=10, width=40)
# text_area.pack(pady=10)
# 
# root.mainloop()


# ==========================================
# OPTION B: The Data Cleaner (Pandas)
# ==========================================

def clean_hr_data(filename):
    """TODO: Clean the messy HR data using Pandas."""
    print(f"Reading from {filename}...")
    
    # 1. Read the CSV using pd.read_csv()
    
    # 2. Drop rows with missing Name or Age using dropna()
    
    # 3. Fix strings: Title case for Name, strip whitespace for City
    
    # 4. Filter out negative ages (keep rows where Age >= 0)
    
    # 5. Fill missing Salaries with 0 using fillna()
    
    # 6. Save to 'cleaned_data.csv' using to_csv(index=False)
    
    print("Data cleaning complete. Check cleaned_data.csv!")

# Uncomment to test Option B:
# clean_hr_data("messy_data.csv")
