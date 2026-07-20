# Class Task: Simple Tkinter Data Entry 📝

## Objective
Your task is to create a simple Tkinter window that allows a user to enter product details and save them to a MySQL database.

## Prerequisites
1. Open your MySQL Command-Line Client.
2. Create a database called `shop_db`.
3. Inside `shop_db`, create a table called `products` with three columns:
   - `id` (INT, AUTO_INCREMENT, PRIMARY KEY)
   - `product_name` (VARCHAR)
   - `price` (DECIMAL or FLOAT)

```sql
CREATE DATABASE shop_db;
USE shop_db;
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL
);
```

## Instructions

1. Open `class_task_starter.py`.
2. The UI code for Name and Price input fields has been provided.
3. Complete the `save_product()` function so that it connects to your MySQL database, inserts the values from the Tkinter Entry widgets into the `products` table, and then clears the entry fields.
4. Show a Success messagebox when the data is inserted, or an Error messagebox if the database connection fails.

### Expected Output
A small window with two text fields. Clicking "Save Product" will write the item to the MySQL database and notify the user of success.
