# Session 11: Database Integration with Python

Welcome to Session 11! Today we will learn how to connect our Python applications to a robust backend database (MySQL). We will also learn how to integrate this database with a Tkinter Graphical User Interface (GUI) to perform CRUD (Create, Read, Update, Delete) operations.

## 📝 Learning Objectives
By the end of this session, you will be able to:
1. Explain the concept of database connectivity in Python.
2. Connect Python with a MySQL database using the `mysql-connector-python` module.
3. Create databases and tables using the MySQL Command-Line Interface (CLI).
4. Design a Tkinter GUI to insert, update, and delete database records.

---

## 1. The Concept of Database Connectivity in Python

Applications need to store data persistently. While text and CSV files are useful, they lack security, scalability, and the ability to handle complex queries. A **Relational Database Management System (RDBMS)** like MySQL solves these problems.

To allow our Python program to "talk" to a MySQL database, we use an API (Application Programming Interface) known as a **Database Connector or Driver**. In Python, the most commonly used driver for MySQL is `mysql-connector-python`.

### Pre-requisites
You need to install the connector package. Open your terminal and run:
```bash
pip install mysql-connector-python
```

---

## 2. Creating a Database and Table via MySQL CLI

Before connecting Python to MySQL, we need a database and a table.
Open your MySQL Command-Line Client and log in (typically as `root` with your password).

**Step 1: Create a Database**
```sql
CREATE DATABASE python_app_db;
```

**Step 2: Select the Database**
```sql
USE python_app_db;
```

**Step 3: Create a Table**
Let's create a table to hold user information.
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    age INT
);
```

**Step 4: Verify the Table**
```sql
DESCRIBE users;
```

---

## 3. Connecting Python to MySQL

Here are the basic steps to connect and interact with a MySQL database in Python:

1. **Import the module**: `import mysql.connector`
2. **Establish a connection**: Use `mysql.connector.connect()` with credentials (host, user, password, database).
3. **Create a Cursor**: A cursor object allows you to execute SQL queries.
4. **Execute Queries**: Use `cursor.execute(query)`.
5. **Commit Changes**: For INSERT, UPDATE, and DELETE, call `connection.commit()`.
6. **Close Connection**: Close the cursor and connection.

### Example: Connecting to the Database
```python
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password", # Replace with your MySQL password
        database="python_app_db"
    )

    if connection.is_connected():
        print("Successfully connected to the database!")
        
        cursor = connection.cursor()
        # Query to fetch all records
        cursor.execute("SELECT * FROM users")
        records = cursor.fetchall()
        print(records)
        
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
```

---

## 4. Designing a Tkinter GUI for CRUD Operations

Now, let's tie it all together by building a Tkinter application that allows a user to interact with the database visually.

### Setting Up the UI
We will create a window with:
- Labels and Entry widgets for Name, Email, and Age.
- Buttons for **Insert**, **Update**, **Delete**, and **View**.

### Code Snippet: Inserting Records via Tkinter
```python
import tkinter as tk
from tkinter import messagebox
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost", user="root", password="your_password", database="python_app_db"
    )

def insert_record():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    
    if not name or not email or not age:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
        
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
        values = (name, email, int(age))
        
        cursor.execute(query, values)
        conn.commit()
        
        messagebox.showinfo("Success", "Record inserted successfully!")
        
        # Clear fields
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# Tkinter Setup
root = tk.Tk()
root.title("User Database App")

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Age:").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Button(root, text="Insert", command=insert_record).pack(pady=10)

root.mainloop()
```

### Understanding CRUD in Tkinter:
- **CREATE**: Fetch data from `tk.Entry()`, build an `INSERT INTO` query, use `cursor.execute(query, values)`, and `conn.commit()`.
- **READ**: Execute a `SELECT * FROM` query, use `cursor.fetchall()`, and display the results in a Tkinter Text widget or Treeview.
- **UPDATE**: Require the user to specify an ID. Build an `UPDATE table SET column=val WHERE id=...` query, then `conn.commit()`.
- **DELETE**: Require the user to specify an ID. Build a `DELETE FROM table WHERE id=...` query, then `conn.commit()`.

---

## 🎥 Recommended Watch
- [Python MySQL Database Tutorial](https://www.youtube.com/watch?v=3vsC05rxZ8c) by Programming with Mosh
- [Tkinter and SQLite/MySQL Database](https://www.youtube.com/watch?v=yGCEt3N60B0) by Codemy.com
