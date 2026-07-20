import tkinter as tk
from tkinter import messagebox
# TODO: Import the MySQL connector

def connect_db():
    # TODO: Connect to the company_db database
    # Return the connection object
    pass

def add_employee():
    # TODO: Read Name, Department, and Salary from entries
    # TODO: Connect to the DB, insert record, commit, and close connection
    # TODO: Show a success message
    pass

def update_employee():
    # TODO: Read ID, Name, Department, and Salary from entries
    # TODO: Connect to the DB, update record where id = entered_id
    # TODO: Commit, close connection, show success message
    pass

def delete_employee():
    # TODO: Read ID from the entry
    # TODO: Connect to the DB, delete record where id = entered_id
    # TODO: Commit, close connection, show success message
    pass

def view_employees():
    # TODO: Connect to the DB, fetch all records from the employees table
    # TODO: Clear the text_area widget
    # TODO: Insert formatted fetched records into text_area
    pass

# --- UI Setup ---
root = tk.Tk()
root.title("Employee Management System")
root.geometry("400x550")

# Entries
tk.Label(root, text="Employee ID (For Update/Delete):").pack(pady=(10, 0))
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Department:").pack()
entry_dept = tk.Entry(root)
entry_dept.pack()

tk.Label(root, text="Salary:").pack()
entry_salary = tk.Entry(root)
entry_salary.pack()

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Add", width=10, command=add_employee).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Update", width=10, command=update_employee).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_employee).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="View All", width=10, command=view_employees).grid(row=1, column=1, padx=5, pady=5)

# Text Area for displaying records
text_area = tk.Text(root, height=12, width=45)
text_area.pack(pady=10)

root.mainloop()
