import tkinter as tk
from tkinter import messagebox
# TODO: Import the MySQL connector package here

def save_product():
    product_name = entry_name.get()
    price = entry_price.get()
    
    # Basic validation
    if not product_name or not price:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return
        
    # TODO: Step 1 - Try connecting to the MySQL database (shop_db)
    # TODO: Step 2 - Create a cursor object
    # TODO: Step 3 - Write the INSERT query and execute it with product_name and price
    # TODO: Step 4 - Commit the transaction
    # TODO: Step 5 - Show a success message box
    # TODO: Step 6 - Clear the entry widgets
    # TODO: Step 7 - Handle exceptions and close the connection in the finally block
    
    pass

# Setting up the Tkinter window
root = tk.Tk()
root.title("Add Product")
root.geometry("300x200")

tk.Label(root, text="Product Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Price:").pack(pady=5)
entry_price = tk.Entry(root)
entry_price.pack()

tk.Button(root, text="Save Product", command=save_product).pack(pady=20)

root.mainloop()
