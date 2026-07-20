# Assignment: Employee Management System 👨‍💼👩‍💼

## Objective
Build a fully functional Employee Management System (EMS) using Tkinter and MySQL. This system should perform full CRUD operations: Create (Insert), Read (View), Update, and Delete.

## Database Setup
1. Open your MySQL Command-Line Client.
2. Run the following commands to set up the database:
```sql
CREATE DATABASE company_db;
USE company_db;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);
```

## Requirements
Your Tkinter application must include the following UI elements and functionalities:

### 1. User Interface (UI)
- **Labels and Entries:** For `Name`, `Department`, and `Salary`.
- **Label and Entry for ID:** Needed for Update and Delete operations.
- **Buttons:** `Add Employee`, `Update Employee`, `Delete Employee`, and `View All`.
- **Text Widget / Listbox:** A dedicated area at the bottom to display the fetched records.

### 2. Core Functions
- **Add Employee:** Read Name, Department, and Salary, then insert the record into the `employees` table.
- **Update Employee:** Read the `ID` from the UI. Update the `Name`, `Department`, and `Salary` for that specific `ID`.
- **Delete Employee:** Read the `ID` and delete the corresponding record from the database.
- **View All:** Fetch all records from the `employees` table and display them in the Text widget/Listbox. (Make sure to clear the widget before inserting new text, so records don't pile up).

### 3. Error Handling
- Use `try-except` blocks around your database operations.
- Show warning message boxes if the user tries to submit an empty form.
- Show error message boxes if the database connection fails or queries crash.
- Ensure the connection is securely closed in a `finally` block after every operation.

---

## Instructions
1. Open `assignment_starter.py`. The basic UI structure has been provided.
2. Complete all the TODO functions (`add_employee`, `update_employee`, `delete_employee`, and `view_employees`).
3. Run and thoroughly test your application to make sure the database is updating correctly!

**Bonus Challenge (Optional):** Add a "Search by Name" button that allows the user to find a specific employee and displays the result in the Text widget!
