# Session 2: Programming Language Construct

## What We'll Build Today
By the end of this session, you'll build a **Quiz Game** that stores questions in a list, checks answers with operators, keeps score with control flow, and announces the winner. But first, let's learn the building blocks.

## Objective & Real-World Application
In Session 1, we learned how to store single pieces of data in variables. But what if you need to store 50 student names? 50 separate variables? No way. Today, we learn:
- **Data Types & Collections** — how to store and organize groups of data
- **Operators** — how to do math, compare things, and combine conditions
- **Control Flow** — how to make your program think, decide, and repeat

**Real-World Example:** When you open your Instagram feed, the app loads a **list** of posts, **checks** if you've liked each one (comparison), and **loops** through them to display one after another. That's everything we're learning today!

---

## 1. Data Types in Python

Every value in Python has a "type" that tells Python what you can do with it.

### Basic Types (Quick Review)
| Type | Example | Real-World Use |
|------|---------|----------------|
| `int` | `42` | Number of lives in a game |
| `float` | `105.50` | Bank account balance |
| `str` | `"Hello"` | A username or tweet |
| `bool` | `True` / `False` | Is the user logged in? |

You can always check a value's type:
```python
print(type(42))        # <class 'int'>
print(type("Hello"))   # <class 'str'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
```

### Type Conversion (Casting)
Sometimes you need to convert between types — especially when using `input()`, which always returns a string.

```python
age_text = input("Enter your age: ")   # This is a string like "20"
age_number = int(age_text)             # Now it's the integer 20

price = 49.99
price_text = str(price)               # Now it's the string "49.99"
```

---

## 2. Collections: Lists, Tuples, and Dictionaries

Single variables are great, but real programs need to store **groups** of related data. Think of it this way:

- A **variable** is a single sticky note
- A **list** is a notebook with numbered pages
- A **dictionary** is a phone book with names and numbers

### Lists — Ordered, Changeable Collections
A list stores multiple items in a specific order. You can add, remove, and change items.

```python
# A list of your favorite foods
foods = ["jollof rice", "pizza", "shawarma", "suya"]

# Access items by their position (index) — counting starts at 0!
print(foods[0])   # "jollof rice" (first item)
print(foods[2])   # "shawarma" (third item)

# How many items?
print(len(foods))  # 4

# Add an item to the end
foods.append("amala")
print(foods)  # ["jollof rice", "pizza", "shawarma", "suya", "amala"]

# Change an item
foods[1] = "fried rice"
print(foods)  # ["jollof rice", "fried rice", "shawarma", "suya", "amala"]

# Remove an item
foods.remove("suya")
print(foods)  # ["jollof rice", "fried rice", "shawarma", "amala"]
```

**Real-World Example:** A playlist on Spotify is a list. You can add songs, remove songs, reorder them, and skip to song number 5.

### Try It Yourself #1
Pause and try this in your Python editor:
```
1. Create a list called `my_hobbies` with 4 of your hobbies
2. Print the SECOND hobby (remember, indexing starts at 0!)
3. Add a 5th hobby using .append()
4. Print the entire list
5. Print how many hobbies you have using len()
```

### Tuples — Ordered but CANNOT Be Changed
A tuple is like a list, but once created, you **cannot** modify it. Use tuples for data that should never change.

```python
# Days of the week should never change
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

print(days[0])    # "Monday"
print(len(days))  # 5

# days[0] = "Funday"  # ERROR! Tuples cannot be changed
```

**When to use tuples vs lists?**
- Use a **list** when items might change (shopping cart, to-do list)
- Use a **tuple** when items should stay fixed (months of the year, GPS coordinates)

### Dictionaries — Key-Value Pairs
A dictionary stores data as **key: value** pairs. Instead of accessing items by number, you access them by name.

```python
# A student's profile
student = {
    "name": "Amina",
    "age": 22,
    "course": "Python Programming",
    "is_enrolled": True
}

# Access values by their key
print(student["name"])       # "Amina"
print(student["course"])     # "Python Programming"

# Add a new key-value pair
student["grade"] = "A"

# Change a value
student["age"] = 23

# Print all keys
print(student.keys())   # dict_keys(["name", "age", "course", "is_enrolled", "grade"])

# Print all values
print(student.values()) # dict_values(["Amina", 23, "Python Programming", True, "A"])
```

**Real-World Example:** When you look up a contact on your phone, you search by **name** (key) and get their **number** (value). That's exactly how a dictionary works.

### Try It Yourself #2
Pause and try this:
```
1. Create a dictionary called `my_phone` with keys: "brand", "color", "storage_gb", "is_new"
2. Fill in the values with your actual phone's info
3. Print just the brand
4. Change "is_new" to False
5. Add a new key "os" with value "Android" or "iOS"
6. Print the entire dictionary
```

---

## 3. Python Operators

Operators are symbols that perform calculations or comparisons.

### Arithmetic Operators (Math)
```python
a = 15
b = 4

print(a + b)    # 19   Addition
print(a - b)    # 11   Subtraction
print(a * b)    # 60   Multiplication
print(a / b)    # 3.75 Division (always returns a float)
print(a // b)   # 3    Floor division (drops the decimal)
print(a % b)    # 3    Modulus (remainder after division)
print(a ** b)   # 50625  Exponent (15 to the power of 4)
```

**Practical Use of Modulus (`%`):** Check if a number is even or odd:
```python
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Comparison Operators (Asking Questions)
These compare two values and always give back `True` or `False`.
```python
x = 10
y = 20

print(x == y)   # False  (Is x equal to y?)
print(x != y)   # True   (Is x NOT equal to y?)
print(x > y)    # False  (Is x greater than y?)
print(x < y)    # True   (Is x less than y?)
print(x >= 10)  # True   (Is x greater than OR equal to 10?)
print(x <= 5)   # False  (Is x less than OR equal to 5?)
```

### Logical Operators (Combining Questions)
Combine multiple conditions into one.

```python
age = 25
has_id = True

# AND — Both must be True
if age >= 18 and has_id:
    print("You can enter the venue")

# OR — At least one must be True
has_ticket = False
is_vip = True
if has_ticket or is_vip:
    print("You can watch the show")

# NOT — Flips True to False (and vice versa)
is_banned = False
if not is_banned:
    print("Welcome!")
```

### Try It Yourself #3
Pause and try this:
```
1. Create two variables: price = 2500 and discount = 15
2. Calculate the discount amount (price * discount / 100)
3. Calculate the final price (price - discount amount)
4. Print: "Original: ₦2500, Discount: ₦375, Final: ₦2125"
5. BONUS: Check if the final price is above or below ₦2000 and print a message
```

---

## 4. Control Flow Statements

Programs normally run top to bottom, one line at a time. Control flow lets your program **make decisions** and **repeat actions**.

### Conditional Statements (if / elif / else)
Think of this like a security guard at a gate — they check your credentials and decide what to do.

```python
score = 75

if score >= 90:
    print("Grade: A - Excellent!")
elif score >= 70:
    print("Grade: B - Good job!")
elif score >= 50:
    print("Grade: C - You passed.")
else:
    print("Grade: F - Try again next time.")
```

**How it works:** Python checks conditions from top to bottom. The moment it finds one that is `True`, it runs that block and **skips the rest**.

### Combining Conditions
You can combine conditions using `and`, `or`, and `not`:
```python
temperature = 32
is_weekend = True

if temperature > 30 and is_weekend:
    print("Perfect day for the beach!")
elif temperature > 30 and not is_weekend:
    print("Hot day, but you have work...")
else:
    print("Maybe stay indoors.")
```

### The `for` Loop — Repeat a Known Number of Times
Use `for` when you know how many times to repeat, or when you want to go through each item in a list.

```python
# Loop through a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("I like", fruit)

# Output:
# I like apple
# I like banana
# I like mango
```

```python
# Loop a specific number of times using range()
for i in range(5):
    print("Clap!", i)

# Output: Clap! 0, Clap! 1, Clap! 2, Clap! 3, Clap! 4
```

```python
# Loop through a dictionary
student = {"name": "Amina", "age": 22, "course": "Python"}
for key, value in student.items():
    print(key, ":", value)
```

### The `while` Loop — Repeat Until a Condition Changes
Use `while` when you don't know how many times to repeat — you just keep going until something changes.

```python
# ATM: Keep asking for PIN until they get it right (max 3 attempts)
correct_pin = "1234"
attempts = 0

while attempts < 3:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == correct_pin:
        print("Access Granted!")
        break  # Exit the loop immediately
    else:
        attempts = attempts + 1
        print("Wrong PIN. Attempts left:", 3 - attempts)

if attempts == 3:
    print("Card blocked. Visit your bank.")
```

**`break`** — Immediately exits the loop.
**`continue`** — Skips the current iteration and moves to the next one.

```python
# Skip the number 3
for i in range(6):
    if i == 3:
        continue
    print(i)
# Output: 0, 1, 2, 4, 5 (3 is skipped!)
```

### Try It Yourself #4
Pause and try this:
```
1. Create a list of 5 Nigerian cities (or any cities you know)
2. Use a for loop to print each city with its position number:
   "City 1: Lagos"
   "City 2: Abuja"
   ... etc.
   (Hint: use enumerate() or a counter variable)
3. BONUS: Use an if statement inside the loop to print
   "*** This is the capital!" next to Abuja
```

---

## 5. Putting It All Together: Mini Example

Here's a small program that combines everything from today:

```python
# A simple menu system for a food ordering app
menu = {
    "Jollof Rice": 1500,
    "Fried Rice": 1800,
    "Shawarma": 2000,
    "Suya": 800
}

print("=== Welcome to Python Eats! ===")
print("Here's our menu:")

# Loop through the menu and display it
for item, price in menu.items():
    print(f"  {item} - N{price}")

# Ask the user what they want
choice = input("\nWhat would you like to order? ")

# Check if the item exists
if choice in menu:
    print(f"Great choice! {choice} costs N{menu[choice]}")
    
    quantity = int(input("How many? "))
    total = menu[choice] * quantity
    print(f"Your total is N{total}")
    
    if total > 3000:
        print("Big order! You get free delivery!")
else:
    print("Sorry, we don't have that on the menu.")
```

---

## Common Mistakes (Watch Out!)

| Mistake | Wrong | Right |
|---------|-------|-------|
| Using `=` instead of `==` for comparison | `if x = 5:` | `if x == 5:` |
| Forgetting to convert `input()` to int | `age = input("Age: ")` then `age > 18` | `age = int(input("Age: "))` |
| Index out of range | `fruits = ["a","b"]` then `fruits[2]` | Index 2 doesn't exist — max is `fruits[1]` |
| Forgetting the colon `:` after if/for/while | `if x == 5` | `if x == 5:` |
| Infinite while loop (no exit condition) | `while True:` with no `break` | Always have a way to stop! |
| Modifying a list while looping through it | Causes skipped items | Loop through a copy instead |

---

## Quick Reference Card

```
LISTS:    my_list = [1, 2, 3]       → ordered, changeable
TUPLES:   my_tuple = (1, 2, 3)      → ordered, NOT changeable
DICTS:    my_dict = {"a": 1}        → key-value pairs

OPERATORS:
  Math:       +  -  *  /  //  %  **
  Compare:    ==  !=  >  <  >=  <=
  Logic:      and  or  not

CONTROL FLOW:
  if / elif / else    → make decisions
  for x in list:      → loop through items
  while condition:    → repeat until condition is False
  break               → exit a loop early
  continue            → skip to next iteration
```

---

## Further Reading & Video Suggestions
- **"Python Lists, Tuples, and Dictionaries"** by Programming with Mosh
- **"Python If Else, For Loops, While Loops"** by Programming with Mosh
- **"Python Tutorial: Conditionals and Booleans"** by Corey Schafer
- **"Python Tutorial: Slicing Lists and Strings"** by Corey Schafer
