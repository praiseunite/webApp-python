# Session 5: Try It Yourself (Review of Sessions 1-4)

## Objective
Congratulations on completing Phase 1! This session is all about **practice**. You'll put everything from Sessions 1-4 together by building a real project AND by debugging broken code. Pick ONE of the two projects below, then complete the Debugging Challenge.

You will use:
- Variables & Data Types (Session 1)
- Lists, Dictionaries, Operators & Control Flow (Session 2)
- Functions with Parameters & Return Values (Session 3)
- Modules & Lambda (Session 4)

---

## Choose Your Project (Pick ONE)

---

### Option A: Library Borrowing System

Build a command-line app that lets users browse and borrow books from a library.

#### Part 1: Setup & Data
1. Open `review_starter.py`.
2. Create a **list of dictionaries** to represent your library catalog:
   ```python
   library = [
       {"title": "Things Fall Apart", "author": "Chinua Achebe", "available": True},
       {"title": "Half of a Yellow Sun", "author": "Chimamanda Adichie", "available": True},
       {"title": "Purple Hibiscus", "author": "Chimamanda Adichie", "available": True},
   ]
   ```

#### Part 2: Functions
1. Create a function `display_catalog(library)` that loops through the library and prints each book with its availability status.
2. Create a function `borrow_book(library, title, user_name, user_age)`:
   - If `user_age` < 12: print a message saying they need an adult.
   - Find the book by title. If not found, print "Book not found."
   - If found but not available, print "Sorry, that book is already borrowed."
   - If found and available, set `available` to `False` and print a success message.
   - Return `True` if borrowed successfully, `False` otherwise.

#### Part 3: Module
1. Open `receipt_module.py` and write a function `print_receipt(book_title, borrower_name)` that prints a formatted receipt:
   ```
   ================================
        LIBRARY RECEIPT
   ================================
   Book:      Things Fall Apart
   Borrower:  Amina
   Date:      2026-06-29
   Status:    BORROWED
   ================================
   ```
   (Hint: use `import datetime` and `datetime.date.today()` for the date)

2. Import `receipt_module` in your main script and call it after a successful borrow.

#### Part 4: Main Loop
1. Use a `while` loop that shows the menu and asks the user what to do:
   - `"1"` = View catalog
   - `"2"` = Borrow a book
   - `"3"` = Quit
2. Use `if/elif/else` to handle each choice.

---

### Option B: Student Grade Calculator

Build a grade processing tool that handles multiple students, calculates averages, and ranks them.

#### Part 1: Setup & Module
1. Create a file called `grade_helpers.py` with these functions:
   - `calculate_average(scores)` — returns the average of a list of numbers
   - `get_grade(average)` — returns "A"/"B"/"C"/"D"/"F" based on the average
   - `get_remark(grade)` — returns a motivational message for the grade

2. In `review_starter.py`, import your module.

#### Part 2: Data Collection
1. Create an empty list called `all_students`.
2. Use a `while` loop to keep adding students:
   - Ask for the student's name
   - Ask for 3 subject scores (use a `for` loop)
   - Calculate their average using your module
   - Get their grade using your module
   - Store the student as a dictionary: `{"name": name, "scores": scores, "average": avg, "grade": grade}`
   - Append to `all_students`
   - Ask "Add another student? (yes/no)" — break if "no"

#### Part 3: Display & Ranking
1. Create a function `print_report_card(student)` that prints a formatted card for one student.
2. Loop through `all_students` and print each report card.
3. Use `sorted()` with a **lambda** to rank students by average (highest first).
4. Print the ranking:
   ```
   === CLASS RANKING ===
   1. Amina - Average: 85.0 (A)
   2. Bola  - Average: 72.3 (B)
   3. Chidi - Average: 58.7 (C)
   ```

#### Part 4: Class Summary
1. Calculate the **class average** (average of all students' averages).
2. Find the **highest scorer** and **lowest scorer**.
3. Print a summary at the end.

---

## Debugging Challenge (Everyone does this!)

The code below has **6 bugs**. Find and fix them all. Write your corrected version in a new file called `debug_challenge.py` or fix them on paper and discuss with the class.

```python
# BUG HUNT: This program should calculate the total price of items in a cart
# with a 10% discount if the total is over 5000. It has 6 bugs. Find them all!

menu = {
    "Burger" = 1500,
    "Fries": 500,
    "Drink": 400,
}

cart = ["Burger", "Fries", "Drink", "Fries"]

total = 0
for item in cart
    price = menu(item)
    total = total + price

print("Subtotal: N" + total)

if total >= 5000:
    discount = total * 10 / 100
    total = total - discount
    print("Discount applied!")

print(f"Total: N{total}")

def apply_discount(amount, percent)
    discounted = amount - (amount * percent / 100)
    return discounted
```

### Bug Hints (only peek if stuck!)
<details>
<summary>Hint 1</summary>
Look at how the dictionary is defined. Is the syntax correct for every key-value pair?
</details>

<details>
<summary>Hint 2</summary>
The for loop is missing something at the end of the line.
</details>

<details>
<summary>Hint 3</summary>
How do you access a dictionary value — with parentheses or square brackets?
</details>

<details>
<summary>Hint 4</summary>
Can you concatenate a string and an integer with `+`?
</details>

<details>
<summary>Hint 5</summary>
The discount condition says >= 5000, but the cart total is only 3900. Is the logic wrong, or is this actually correct behavior? (Trick question — this one might not be a bug!)
</details>

<details>
<summary>Hint 6</summary>
The function definition at the bottom is missing something AND it's defined after it would be needed. Does placement matter?
</details>

---

## Answers to Debug Challenge
<details>
<summary>Click to see all 6 bugs</summary>

1. **Line 4:** `"Burger" = 1500` should be `"Burger": 1500` (colon, not equals)
2. **Line 10:** `for item in cart` is missing the colon: `for item in cart:`
3. **Line 11:** `menu(item)` should be `menu[item]` (square brackets for dictionaries)
4. **Line 14:** `"Subtotal: N" + total` — can't concatenate string + int. Use `f"Subtotal: N{total}"` or `str(total)`
5. **Line 21:** `def apply_discount(amount, percent)` is missing the colon: `def apply_discount(amount, percent):`
6. **Line 21-23:** The function is defined but never called, and it's defined at the bottom after it could have been useful. Move it above and use it instead of the inline discount calculation.
</details>

---

*If you get stuck on the project, try breaking the problem into smaller pieces. Build one function at a time, test it, then move on. You can always peek at `review_solution.py` for guidance!*
