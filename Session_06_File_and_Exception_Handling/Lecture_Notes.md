# Session 6: File Handling and Exception Handling

## Objective & Real-World Application
Every real-world application deals with persistent data — data that survives after the program closes. When you log into a website, your profile was most likely loaded from a file or database. When you fill out a form, your data gets saved somewhere. In Python, **File Handling** is how we read from and write to files on disk, while **Exception Handling** is how we gracefully deal with errors when things go wrong (and in real software, they *always* go wrong at some point!).

**Real-World Examples:**
- A school system saves student results to a `.txt` file at the end of each term.
- A banking app logs every failed login attempt to an error log file.
- An e-commerce site catches payment errors and shows the customer a friendly message instead of crashing.

---

## 1. File Access Modes and Operations

Before Python can read or write a file, you must tell it **how** you want to open it. These are called **file access modes**.

![File Access Modes](../assets/images/python_file_modes.png)

Think of it like opening a physical filing cabinet. You need to decide: are you just **reading** a document, **replacing** it entirely, or **adding** notes to the bottom of an existing one?

| Mode | Symbol | Description | What Happens if File Doesn't Exist? |
|------|--------|-------------|--------------------------------------|
| Read | `r` | Opens file for **reading only**. | Raises an error ❌ |
| Write | `w` | Opens file for **writing**. Overwrites existing content. | Creates a new file ✅ |
| Append | `a` | Opens file for **appending**. Adds to the end without deleting existing content. | Creates a new file ✅ |
| Read & Write | `r+` | Opens file for both **reading and writing**. | Raises an error ❌ |

---

## 2. File Handling Methods

### Opening and Closing a File
The basic way to work with a file is to `open()` it, do your work, then `close()` it. Forgetting to close is like leaving a tap running!

```python
# Open a file in write mode
my_file = open("student_data.txt", "w")

# Write a line to the file
my_file.write("Name: Alice\n")
my_file.write("Score: 95\n")

# Always close the file when done!
my_file.close()
```

### The Better Way: `with` Statement ✅
Python provides a smarter way to open files using the `with` keyword. It **automatically closes the file** for you when the block ends, even if an error occurs. This is considered best practice and is what you should use in real projects.

```python
# The 'with' block handles opening and closing automatically
with open("student_data.txt", "w") as my_file:
    my_file.write("Name: Alice\n")
    my_file.write("Score: 95\n")
# File is now automatically closed here — no need to call close()!
```

### Reading from a File
There are three main ways to read content from a file:

```python
# Method 1: read() — Reads the ENTIRE file as one big string
with open("student_data.txt", "r") as my_file:
    content = my_file.read()
    print(content)

# Method 2: readline() — Reads ONE line at a time
with open("student_data.txt", "r") as my_file:
    first_line = my_file.readline()
    print(first_line)  # Output: "Name: Alice"

# Method 3: readlines() — Reads ALL lines and returns them as a LIST
with open("student_data.txt", "r") as my_file:
    all_lines = my_file.readlines()
    for line in all_lines:
        print(line, end="")
```

### Appending to a File
Appending is crucial when you want to **add** new data without erasing old data — think of it like adding a new entry to a diary.

```python
# 'a' mode adds new data to the END of the file
with open("student_data.txt", "a") as my_file:
    my_file.write("Name: Bob\n")
    my_file.write("Score: 88\n")
```

---

## 3. Exception Handling Mechanisms

No matter how carefully you write your code, things can go wrong. A user might type letters when you expect numbers. A file might not exist. The internet might be down. Without proper handling, these situations cause your program to **crash with an ugly error message**.

Exception Handling allows your program to **detect the problem, handle it gracefully, and continue running**.

![Exception Handling Safety Net](../assets/images/python_exception_handling.png)

### The `try/except` Block
The `try` block contains code that might cause an error. The `except` block runs only if an error actually occurs — it catches the crash, just like a safety net.

```python
# Without exception handling — This will CRASH if the file doesn't exist
my_file = open("grades.txt", "r")  # FileNotFoundError!
```

```python
# With exception handling — This handles the error gracefully
try:
    my_file = open("grades.txt", "r")
    content = my_file.read()
    print(content)
except FileNotFoundError:
    print("Oops! The file 'grades.txt' does not exist yet.")
```

### Handling Multiple Exceptions
You can have multiple `except` blocks to handle different types of errors differently — just like how a hospital has different wards for different medical emergencies.

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)
except ValueError:
    # Runs if the user types text instead of a number
    print("That's not a valid number! Please enter digits only.")
except ZeroDivisionError:
    # Runs if the user types 0 (you can't divide by zero!)
    print("You can't divide by zero!")
```

### The `else` and `finally` Clauses
These two optional clauses give you even more control:
- **`else`:** Runs only if the `try` block succeeded with **no errors**.
- **`finally`:** Runs **always**, whether an error happened or not. Perfect for cleanup tasks like closing files or database connections.

```python
try:
    with open("student_data.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File read successfully!")
    print(data)
finally:
    print("File operation attempted. Program continues...")
```

### Common Python Exceptions to Know

| Exception | When it Occurs |
|-----------|----------------|
| `FileNotFoundError` | Opening a file that doesn't exist |
| `ValueError` | Passing a wrong type of value (e.g., `int("hello")`) |
| `ZeroDivisionError` | Dividing a number by zero |
| `TypeError` | Performing an operation on incompatible types |
| `IndexError` | Accessing a list position that doesn't exist |
| `KeyError` | Accessing a dictionary key that doesn't exist |

---

## 📺 Further Reading & Video Suggestions
- **"Python File Handling | Reading and Writing Files"** by Programming with Mosh
- **"Python Tutorial: File Objects - Reading and Writing to Files"** by Corey Schafer
- **"Python Exception Handling - Try, Except, Else, Finally"** by Tech With Tim
- **"Python Errors and Exceptions for Beginners"** by CS Dojo
