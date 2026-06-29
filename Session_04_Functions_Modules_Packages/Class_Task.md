# Class Task: Build a Reusable Utilities Module

## What You'll Build
You'll create a **`math_helpers.py`** module with useful functions, then import and use it from a main script. This is the exact workflow professional developers use every day.

---

## Part 1: Create the Module (Do this in class together)

### Instructions

1. **Create a new file** called `math_helpers.py` in the Session 4 folder.

2. Inside `math_helpers.py`, write these functions:

   **Function 1: `calculate_average(numbers)`**
   - Takes a list of numbers
   - Returns the average (sum / count)

   **Function 2: `find_max(numbers)`**
   - Takes a list of numbers
   - Returns the largest number (without using Python's built-in `max()` — write the logic yourself using a loop!)

   **Function 3: `is_even(number)`**
   - Takes a single number
   - Returns `True` if even, `False` if odd

   **Function 4: `percentage(part, whole)`**
   - Takes two numbers
   - Returns what percentage `part` is of `whole`

3. **Open `class_task_solution.py`** (or create a new file) and write:
   ```python
   import math_helpers

   scores = [85, 92, 78, 95, 63]

   avg = math_helpers.calculate_average(scores)
   print(f"Average score: {avg}")

   highest = math_helpers.find_max(scores)
   print(f"Highest score: {highest}")

   print(f"Is 42 even? {math_helpers.is_even(42)}")
   print(f"Is 7 even? {math_helpers.is_even(7)}")

   print(f"75 out of 100 = {math_helpers.percentage(75, 100)}%")
   ```

4. Run the main script and verify the output matches:
   ```
   Average score: 82.6
   Highest score: 95
   Is 42 even? True
   Is 7 even? False
   75 out of 100 = 75.0%
   ```

---

## Part 2: Add Lambda & Sorting (Try on your own, 10-15 minutes)

### Upgrade A: Sort Students by Score
Add this to your main script (not the module):
```python
students = [
    {"name": "Zara", "score": 85},
    {"name": "Amina", "score": 92},
    {"name": "Bola", "score": 78},
    {"name": "Chidi", "score": 95},
    {"name": "Dayo", "score": 63}
]
```
Use `sorted()` with a **lambda** to:
1. Sort students by score (highest first) and print the ranking
2. Sort students by name (A-Z) and print the list

### Upgrade B: Add a Recursive Countdown
Add a `countdown(n)` function to your `math_helpers.py` module:
- Prints numbers from `n` down to 1, then prints "GO!"
- Uses recursion (the function calls itself)
- Import and test it from your main script

### Upgrade C: Use a Built-in Module
Import Python's `random` module and:
1. Generate a random list of 10 scores between 50-100
2. Pass that list to your `math_helpers.calculate_average()` function
3. Print both the random scores and their average

---

## Expected Output (Part 2A)
```
=== STUDENT RANKING (by score) ===
1. Chidi - 95
2. Amina - 92
3. Zara - 85
4. Bola - 78
5. Dayo - 63

=== ALPHABETICAL ORDER ===
Amina, Bola, Chidi, Dayo, Zara
```

---

You can view the solutions in `class_task_solution.py` and `math_helpers.py`.
