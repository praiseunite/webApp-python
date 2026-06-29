# Session 4: Functions, Modules, and Packages

## What We'll Build Today
By the end of this session, you'll organize your code like a professional — splitting it into **modules** (separate files) and using **advanced function techniques** like recursion and lambda. You'll build a reusable `math_helpers` module that you can import into any future project.

## Objective & Real-World Application
As your programs grow, keeping everything in one file becomes a nightmare. Imagine writing a 5,000-line file — good luck finding anything!

**Real-World Example:** Django (the framework that powers Instagram's backend) has hundreds of files organized into packages. Every feature lives in its own module: `auth.py` for login, `models.py` for database, `views.py` for pages. That's what we're learning today.

---

## 1. Recursive Functions

A recursive function is a function that **calls itself**. It breaks a big problem into smaller versions of the same problem.

### Starting Simple: Countdown Timer
Before we get to math, let's see recursion with something visual:

```python
def countdown(n):
    if n == 0:          # BASE CASE: when to stop
        print("GO!")
        return
    print(n, "...")
    countdown(n - 1)    # Call itself with a smaller number

countdown(5)
```
Output:
```
5 ...
4 ...
3 ...
2 ...
1 ...
GO!
```

**How it works:**
1. `countdown(5)` prints "5..." then calls `countdown(4)`
2. `countdown(4)` prints "4..." then calls `countdown(3)`
3. ... this continues until `countdown(0)` hits the base case and stops

**The Golden Rule:** Every recursive function MUST have a **base case** — a condition that stops it from calling itself forever. Without it, your program crashes.

### Classic Example: Factorial
Factorial means multiplying a number by every number below it: `5! = 5 x 4 x 3 x 2 x 1 = 120`

```python
def factorial(n):
    if n == 1:        # Base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
print(factorial(3))   # 6 (3 x 2 x 1)
```

### When to Use Recursion?
Honestly? **Rarely in everyday coding.** Most things recursion does, a `for` or `while` loop can also do (and often more clearly). But recursion is essential for:
- Navigating folder structures (folders inside folders inside folders...)
- Some algorithms in interviews and computer science
- Understanding how Python works under the hood

### Try It Yourself #1
```
1. Create a recursive function called sum_to(n) that adds all numbers from 1 to n.
   Example: sum_to(5) should return 15 (1+2+3+4+5)
   - Base case: if n == 1, return 1
   - Recursive case: return n + sum_to(n - 1)
2. Test it: print(sum_to(10)) should print 55
```

---

## 2. Lambda Functions (Mini Functions)

Sometimes you need a tiny, one-use function. Writing a full `def` feels like overkill. That's where **lambda** comes in — a one-line anonymous function.

```python
# Regular function
def double(x):
    return x * 2

# Same thing as a lambda
double = lambda x: x * 2

print(double(5))   # 10
```

### When Lambdas Actually Shine
Assigning a lambda to a variable (like above) isn't very useful — you might as well use `def`. Lambdas shine when used **inside other functions**, especially `sorted()`, `filter()`, and `map()`.

#### Sorting with Custom Rules
```python
students = [
    {"name": "Zara", "score": 85},
    {"name": "Amina", "score": 92},
    {"name": "Bola", "score": 78}
]

# Sort by score (highest first)
ranked = sorted(students, key=lambda s: s["score"], reverse=True)

for student in ranked:
    print(f"{student['name']}: {student['score']}")

# Output:
# Amina: 92
# Zara: 85
# Bola: 78
```

#### Filtering a List
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get only even numbers
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8, 10]
```

#### Transforming a List
```python
prices_usd = [10, 25, 50, 100]

# Convert to Naira (1 USD = ~1600 NGN)
prices_ngn = list(map(lambda p: p * 1600, prices_usd))
print(prices_ngn)   # [16000, 40000, 80000, 160000]
```

### Try It Yourself #2
```
1. You have a list of words: words = ["Python", "is", "absolutely", "amazing", "today"]
2. Use sorted() with a lambda to sort them by LENGTH (shortest first)
   Hint: key=lambda w: len(w)
3. Use filter() with a lambda to keep only words longer than 3 characters
4. Print both results
```

---

## 3. Modules — Organizing Code into Files

A **module** is just a `.py` file that contains functions and variables you want to reuse.

### Why Use Modules?
- **Reusability:** Write a function once, use it in 10 different projects
- **Organization:** Keep related functions together in one file
- **Readability:** Your main file stays clean and short

### Creating Your First Module

**Step 1:** Create a file called `math_helpers.py`:
```python
# math_helpers.py — A reusable math utilities module

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def percentage(part, whole):
    return (part / whole) * 100

def is_even(number):
    return number % 2 == 0
```

**Step 2:** In your main file, import and use it:
```python
# main.py
import math_helpers

result = math_helpers.add(10, 20)
print(result)   # 30

print(math_helpers.percentage(75, 100))   # 75.0
print(math_helpers.is_even(7))            # False
```

### Different Ways to Import

```python
# Import the entire module (recommended — clear where each function comes from)
import math_helpers
math_helpers.add(5, 3)

# Import specific functions (good when you only need one or two)
from math_helpers import add, multiply
add(5, 3)          # No need for math_helpers. prefix
multiply(4, 5)

# Import with a nickname (useful for long module names)
import math_helpers as mh
mh.add(5, 3)
```

### Using Python's Built-in Modules
Python comes with hundreds of useful modules you can import right away:

```python
import random
print(random.randint(1, 100))       # Random number between 1 and 100
print(random.choice(["a", "b"]))    # Random pick from a list

import math
print(math.sqrt(144))    # 12.0 (square root)
print(math.pi)           # 3.14159...

import datetime
today = datetime.date.today()
print(today)   # 2026-06-29
```

### Try It Yourself #3
```
1. Create a file called string_helpers.py with two functions:
   - shout(text): returns the text in ALL CAPS (hint: .upper())
   - whisper(text): returns the text in all lowercase (hint: .lower())
2. In your main script, import string_helpers
3. Test: print(string_helpers.shout("hello world"))  -> "HELLO WORLD"
4. Test: print(string_helpers.whisper("STOP YELLING")) -> "stop yelling"
```

---

## 4. Packages — Folders of Modules

If a module is a single file, a **package** is a folder containing multiple related modules.

```
my_project/
    main.py
    utils/                  <-- This is a package (folder)
        __init__.py         <-- Makes Python treat this folder as a package
        math_helpers.py     <-- Module 1
        string_helpers.py   <-- Module 2
```

### Using a Package
```python
# From your main.py
from utils import math_helpers
from utils import string_helpers

print(math_helpers.add(5, 3))
print(string_helpers.shout("hello"))
```

**Note:** The `__init__.py` file can be empty — it just tells Python "this folder is a package." In modern Python (3.3+), it's technically optional, but it's still good practice to include it.

### When Do You Need Packages?
- When your project has **more than 5-10 modules**, grouping them into folders keeps things tidy
- For now, single modules are perfectly fine for our projects

---

## 5. Putting It All Together: Mini Example

Here's a practical example combining everything from today:

```python
# discount_calculator.py — a reusable module

def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    return price - discount

def apply_bulk_discount(prices):
    """Apply 10% discount if buying 3+ items"""
    if len(prices) >= 3:
        return list(map(lambda p: calculate_discount(p, 10), prices))
    return prices
```

```python
# main.py — uses the module
import discount_calculator as dc

cart_prices = [1500, 2000, 800, 3000]

print("Original prices:", cart_prices)

discounted = dc.apply_bulk_discount(cart_prices)
print("After bulk discount:", discounted)

total = sum(discounted)
print(f"Total: N{total}")
```

---

## Common Mistakes (Watch Out!)

| Mistake | Wrong | Right |
|---------|-------|-------|
| No base case in recursion | Function calls itself forever -> crash | Always have an `if` that returns without calling itself |
| Module not in same folder | `import my_module` -> ModuleNotFoundError | Make sure both files are in the same directory |
| Circular imports | `a.py` imports `b.py` which imports `a.py` | Restructure so imports go one direction |
| Lambda with multiple lines | `lambda x: if x > 0: x` | Lambdas are ONE expression only — use `def` for complex logic |
| Forgetting `.py` in filename | Creating `math_helpers` (no extension) | File must be named `math_helpers.py` |
| Naming your file same as a built-in | `random.py` shadows Python's `random` module | Never name your files `math.py`, `random.py`, `string.py`, etc. |

---

## Quick Reference Card

```
RECURSION:
  def func(n):
      if n == base:     # Base case — MUST have this!
          return value
      return func(n-1)  # Recursive case

LAMBDA:
  lambda x: x * 2                           # One-line function
  sorted(list, key=lambda x: x["score"])     # Sort by custom key
  filter(lambda x: x > 5, numbers)           # Keep items matching condition
  map(lambda x: x * 2, numbers)             # Transform each item

MODULES:
  import module_name                     # Import entire module
  from module_name import function       # Import specific function
  import module_name as alias            # Import with nickname

PACKAGES:
  my_package/
      __init__.py
      my_module.py
  from my_package import my_module
```

---

## Further Reading & Video Suggestions
- **"Python Recursion for Beginners"** by Computer Science
- **"Python Lambda Functions"** by Corey Schafer
- **"Python Tutorial: Modules and Packages"** by Programming with Mosh
- **"Sorting with Lambda"** by Tech With Tim
