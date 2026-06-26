# Session 1: Basics of Python

Welcome to **Application Based Programming in Python**! In this course, we won't just be learning theory—we will be building practical, real-world projects. By the end of this module, you will have built web apps, scraped data from the internet, and even trained a machine learning model.

## 1. What is Python?
**Python** is a high-level, interpreted programming language known for its simplicity and readability. 
Imagine Python as plain English; it focuses on *what* you want to do rather than the complex syntax of *how* to do it.

**Why Python?**
- **Beginner-Friendly:** Its syntax is clean and easy to understand.
- **Versatile:** Used for Web Development, Data Science, AI/Machine Learning, and Automation.

## 2. Keywords, Identifiers, and Naming Rules

### Keywords
Keywords are reserved words in Python that have special meanings. You cannot use them as names for your own data.
*Examples:* `True`, `False`, `if`, `else`, `for`, `while`, `def`, `return`.

### Identifiers
An **identifier** is a name you give to entities like variables, functions, or classes.

**Rules for Naming Identifiers:**
1. Can only contain letters (a-z, A-Z), numbers (0-9), and underscores (`_`).
2. **Cannot start with a number.** (`1name` is invalid, `name1` is valid).
3. **Case-Sensitive:** `Age`, `age`, and `AGE` are three different identifiers.
4. Cannot be a Python keyword.

## 3. Statements, Comments, and Indentation

### Statements
A statement is an instruction that the Python interpreter can execute.
```python
print("Hello, World!")
```

### Comments
Comments are notes written in the code for humans to read. Python completely ignores them.
```python
# This is a single-line comment
print("Welcome to Python!") 

"""
This is a multi-line comment.
We use it to write longer explanations or document our code.
"""
```

### Indentation: Python's Superpower
Python uses **indentation** (spaces at the beginning of a line) to group code.
```python
if True:
    print("This line is indented!")
```

## 4. Variables and Assigning Values
Think of a **variable** as a labeled storage box.
```python
# Assigning values to variables
player_name = "Alice"  # Storing text (String)
score = 150            # Storing a whole number (Integer)

print("Player:", player_name)
print("Score:", score)
```
