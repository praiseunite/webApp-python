# Session 13: Try It Yourself (Database Integration & Pandas)

## Objective
Welcome to the Session 13 Review! This session bridges the gap between Data Storage (MySQL) and Data Manipulation (Pandas), serving as the core of backend data engineering and data science preparation. Pick AT LEAST ONE project to complete, and then tackle the Debugging Challenge.

---

## Choose Your Project (Pick ONE)

### Option A: The Contact Book (MySQL + Tkinter)
You will build a desktop Contact Book that allows users to save and view contacts in a MySQL database.

**Instructions:**
1. Open your MySQL Command-Line Client and run:
   ```sql
   CREATE DATABASE contact_book_db;
   USE contact_book_db;
   CREATE TABLE contacts (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       phone VARCHAR(20) NOT NULL,
       email VARCHAR(100)
   );
   ```
2. Open `review_starter.py`.
3. Complete the `save_contact()` function to insert a contact into the `contacts` table.
4. Complete the `view_contacts()` function to fetch all records and display them in the Text widget.
5. Make sure you use `try-except-finally` to handle database connections safely.

### Option B: The Data Cleaner (Pandas)
You are given a messy CSV file (`messy_data.csv`) exported from a legacy HR system. Your job is to clean it up using Pandas.

**Instructions:**
1. Open `review_starter.py`.
2. Write a function `clean_hr_data(filename)` that uses `pandas` to read the CSV file.
3. Perform the following cleaning operations:
   - Drop rows where the `Name` or `Age` is missing (NaN).
   - Convert the `Name` column to Title Case (e.g., "DAVID LEE" -> "David Lee").
   - Strip leading and trailing whitespace from the `City` column.
   - Filter out any rows where the `Age` is less than 0 (invalid data).
   - Fill any missing `Salary` values with `0`.
4. Save the cleaned DataFrame to a new file called `cleaned_data.csv` using `df.to_csv(..., index=False)`.

---

## Debugging Challenge (Everyone does this!)

The code below is supposed to read data from a database and load it into a Pandas DataFrame for analysis. However, it has **5 bugs**. 

Find and fix them all in `debug_challenge.py`.

```python
import pandas as pd
import mysql.connector

def analyze_db_data():
    try
        conn = mysql.connector.connect(
            host="localhost"
            user="root",
            password="password",
            database="company_db"
        )
        
        # Query to fetch all employees
        query = "SELECT * FROM employees"
        
        # Load the SQL query directly into a DataFrame
        df = pd.read_sql(query conn)
        
        # Print the average salary
        print("Average Salary:", df['salary'].avg())
        
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn.is_connected():
            conn.close()

analyze_db_data()
```

### Bug Hints
<details>
<summary>Hint 1</summary>
Check the `try` block syntax. Is anything missing at the end of the line?
</details>
<details>
<summary>Hint 2</summary>
Look closely at the `mysql.connector.connect()` parameters. Are they separated correctly?
</details>
<details>
<summary>Hint 3</summary>
In `pd.read_sql()`, how do you separate the query and the connection arguments?
</details>
<details>
<summary>Hint 4</summary>
Pandas DataFrames use `.mean()` to calculate averages, not `.avg()`.
</details>
<details>
<summary>Hint 5</summary>
What if the connection fails and `conn` is never defined? The `finally` block will crash when checking `conn.is_connected()`. How can you safely check if the variable exists first?
</details>

---

## Answers to Debug Challenge
<details>
<summary>Click to see all 5 bugs</summary>

1. **Line 5:** Missing colon at the end of `try:`.
2. **Line 7:** Missing comma after `host="localhost",`.
3. **Line 17:** Missing comma between arguments in `pd.read_sql(query, conn)`.
4. **Line 20:** Pandas uses `.mean()`, so it should be `df['salary'].mean()`.
5. **Line 25:** Add a check to ensure `conn` is defined before checking if it's connected: `if 'conn' in locals() and conn.is_connected():`
</details>

---

*If you get stuck, try breaking the problem into smaller pieces. You can always peek at `review_solution.py` for guidance!*
