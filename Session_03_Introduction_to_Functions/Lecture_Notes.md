# Session 3: Introduction to Functions

## What We'll Build Today
By the end of this session, you'll build a **Password Strength Checker** — a function that takes a password, analyzes it, and tells the user if it's Weak, Medium, or Strong. But first, let's understand why functions exist.

## Objective & Real-World Application

### Why Do We Need Functions?
Look at this code that greets three users:

```python
# WITHOUT functions — repeated code everywhere
print("=============================")
print("Welcome, Alice!")
print("Your account has been created.")
print("=============================")

print("=============================")
print("Welcome, Bob!")
print("Your account has been created.")
print("=============================")

print("=============================")
print("Welcome, Charlie!")
print("Your account has been created.")
print("=============================")
```

Now look at the same thing WITH a function:

```python
# WITH a function — write once, use everywhere
def welcome_user(name):
    print("=============================")
    print(f"Welcome, {name}!")
    print("Your account has been created.")
    print("=============================")

welcome_user("Alice")
welcome_user("Bob")
welcome_user("Charlie")
```

**3 lines vs 15 lines.** And if you need to change the welcome message? Change it in ONE place, not three. That's the power of functions.

---

## 1. What is a Function?

A function is a reusable block of code that performs a specific task. Think of it like a **vending machine**:

1. You **put something in** (money + selection) — these are the **arguments**
2. The machine **does its work** (processes your request) — this is the **function body**
3. You **get something out** (your snack) — this is the **return value**

### Types of Functions
1. **Built-in Functions** — Python gives you these for free:
   ```python
   print("Hello")          # Displays text
   len([1, 2, 3])          # Returns 3 (length of list)
   type(42)                # Returns <class 'int'>
   input("Name: ")         # Gets user input
   int("25")               # Converts string to integer
   max(10, 20, 5)          # Returns 20 (largest value)
   min(10, 20, 5)          # Returns 5 (smallest value)
   ```

2. **User-Defined Functions** — Functions YOU create to solve YOUR specific problems.

---

## 2. Creating and Calling a Function

Use the `def` keyword (short for "define") to create a function.

```python
# DEFINING the function (creating the vending machine)
def say_hello():
    print("Hello from inside the function!")
    print("Welcome to Python Course.")

# CALLING the function (using the vending machine)
say_hello()
say_hello()  # You can call it as many times as you want!
```

**Key rule:** The code inside a function does NOT run until you call it. Defining is building the machine. Calling is pressing the button.

### Try It Yourself #1
```
1. Create a function called display_menu() that prints:
   "=== MAIN MENU ==="
   "1. Start Game"
   "2. Settings"
   "3. Quit"
2. Call the function twice
3. Notice how you wrote the menu once but displayed it twice!
```

---

## 3. Parameters and Arguments

Parameters let you pass data INTO a function so it can work with different inputs each time.

- **Parameter** = the variable name in the function definition (the label on the slot)
- **Argument** = the actual value you pass when calling (the coin you insert)

```python
# 'name' is the PARAMETER
def greet(name):
    print(f"Hello, {name}! Nice to meet you.")

# "Alice" and "Bob" are ARGUMENTS
greet("Alice")   # Output: Hello, Alice! Nice to meet you.
greet("Bob")     # Output: Hello, Bob! Nice to meet you.
```

### Multiple Parameters
```python
def calculate_total(price, quantity):
    total = price * quantity
    print(f"Total: N{total}")

calculate_total(1500, 3)   # Total: N4500
calculate_total(200, 10)   # Total: N2000
```

### Default Parameters
You can give parameters a default value. If no argument is passed, the default is used.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                  # Hello, Alice!
greet("Bob", "Good morning")    # Good morning, Bob!
```

### Try It Yourself #2
```
1. Create a function called introduce(name, age, city)
   that prints: "My name is [name], I'm [age] years old, from [city]."
2. Call it with YOUR details
3. Call it with a friend's details
4. BONUS: Add a default value for city (your hometown)
   so you can call introduce("Alice", 20) without the city
```

---

## 4. Return Values — Getting Data OUT of a Function

So far, our functions just `print` things. But what if you want the function to **give you back a value** that you can use later? That's what `return` does.

```python
def add(a, b):
    result = a + b
    return result   # Sends the answer BACK to whoever called this function

# The returned value gets stored in 'total'
total = add(10, 20)
print(f"The sum is: {total}")   # The sum is: 30

# You can even use it directly
print(add(5, 3))   # 8
```

### `print` vs `return` — What's the Difference?
```python
def print_sum(a, b):
    print(a + b)      # Shows the answer on screen, but that's it

def return_sum(a, b):
    return a + b       # Gives the answer BACK so you can use it

# With print: you can see it, but can't use it
result1 = print_sum(5, 3)   # Prints "8" on screen
print(result1)               # None! print doesn't give anything back

# With return: you can use it in other calculations
result2 = return_sum(5, 3)   # Nothing prints yet
double = result2 * 2          # But you can do math with it!
print(double)                 # 16
```

**Rule of thumb:** Use `return` when you need to USE the result. Use `print` when you just need to DISPLAY something.

### Returning Multiple Values
Python functions can return more than one value using commas:
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = get_min_max([45, 12, 89, 34, 67])
print(f"Lowest: {lowest}, Highest: {highest}")
# Output: Lowest: 12, Highest: 89
```

### Try It Yourself #3
```
1. Create a function called convert_temperature(celsius)
   that converts Celsius to Fahrenheit using: fahrenheit = (celsius * 9/5) + 32
2. The function should RETURN the result (not print it)
3. Call it with 0, 100, and 37 — store each result in a variable
4. Print: "0°C = 32.0°F", "100°C = 212.0°F", "37°C = 98.6°F"
```

---

## 5. Variable Scope — Where Variables Live

Where you create a variable determines where you can use it.

### Local Scope (Inside a Function)
Variables created inside a function **only exist inside that function**. They're born when the function runs and die when it finishes.

```python
def my_function():
    secret = "I only exist in here"
    print(secret)   # This works

my_function()
# print(secret)  # ERROR! 'secret' doesn't exist out here
```

### Global Scope (Outside All Functions)
Variables created outside any function can be **read** from anywhere.

```python
app_name = "Python Bites"   # Global variable

def show_header():
    print(f"Welcome to {app_name}")   # Reading global — this works!

show_header()
```

### The Scope Rule
```
GLOBAL variables:  Can be READ inside functions, but not changed
LOCAL variables:   Can ONLY be used inside the function that created them
```

```python
counter = 0   # Global

def increment():
    # counter = counter + 1   # ERROR! Can't modify a global directly
    local_counter = counter + 1   # This works — creates a new local variable
    return local_counter

counter = increment()   # Update the global with the returned value
print(counter)   # 1
```

---

## 6. Putting It All Together: Mini Example

```python
# A simple tip calculator using functions

def calculate_tip(bill_amount, tip_percent):
    tip = bill_amount * tip_percent / 100
    total = bill_amount + tip
    return tip, total

def display_bill(bill, tip_percent):
    tip_amount, total = calculate_tip(bill, tip_percent)
    print("=========================")
    print(f"  Bill:    N{bill}")
    print(f"  Tip({tip_percent}%): N{tip_amount}")
    print(f"  Total:   N{total}")
    print("=========================")

# Use the functions
display_bill(5000, 10)
display_bill(12000, 15)
```

---

## Common Mistakes (Watch Out!)

| Mistake | Wrong | Right |
|---------|-------|-------|
| Calling before defining | Call `greet()` before `def greet():` | Define the function ABOVE where you call it |
| Forgetting parentheses when calling | `greet` (just references the function) | `greet()` (actually CALLS it) |
| Forgetting `return` | Function returns `None` by default | Add `return value` if you need the result |
| Wrong number of arguments | `def add(a, b)` called as `add(1)` | Pass the same number of arguments as parameters |
| Modifying a global variable inside a function | `counter = counter + 1` inside function | Use `return` to send the new value back |
| Indentation errors | Code outside the `def` block | Everything inside the function must be indented |

---

## Quick Reference Card

```
DEFINE:      def function_name(param1, param2):
CALL:        function_name(arg1, arg2)
RETURN:      return value
MULTIPLE:    return val1, val2
DEFAULT:     def greet(name, msg="Hello"):
SCOPE:       Local = inside function only
             Global = everywhere (read-only inside functions)

BUILT-IN FAVORITES:
  print()  input()  len()  type()  int()  str()
  float()  max()  min()  range()  round()  abs()
```

---

## Further Reading & Video Suggestions
- **"Python Tutorial: Functions"** by Corey Schafer
- **"Python Functions | Python Tutorial for Absolute Beginners"** by CS Dojo
- **"Python Tutorial for Beginners - Functions"** by Programming with Mosh
