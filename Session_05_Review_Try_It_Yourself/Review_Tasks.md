# Session 5: Try It Yourself (Review of Sessions 1-4)

## Objective
Congratulations on completing the first phase of the course! In this session, you will put everything you've learned from Sessions 1 through 4 into practice by building a **Library Management CLI**.

You will need to use:
- Variables & Data Types (Session 1)
- Operators & Control Flow (Session 2)
- Functions (Session 3)
- Custom Modules (Session 4)

---

## The Challenge: Library Borrowing System

### Part 1: Setup & Variables
1. Open the provided `review_starter.py` file.
2. Create variables to represent a library book: `book_title`, `author`, `year_published`, and `is_available` (set this to `True`).

### Part 2: Functions & Control Flow
1. Create a function called `borrow_book(user_age)`.
2. Inside the function, use an `if/else` statement:
   - If the `user_age` is less than 12, print `"Sorry, you need an adult to borrow this book."`
   - If the `user_age` is 12 or older, change the `is_available` variable to `False` and print `"You have successfully borrowed [book_title]!"`

### Part 3: Modules
1. Open the `receipt_module.py` file.
2. Inside it, write a function called `print_receipt(book, name)` that prints a formatted receipt showing the user's name and the book they borrowed.
3. Go back to `review_starter.py`, **import** your `receipt_module`, and call the `print_receipt()` function if the user successfully borrows the book.

### Part 4: Tying it Together (Input & Loops)
At the bottom of your script:
1. Use a `while` loop that asks the user `"Do you want to borrow a book? (yes/no): "`.
2. If they type `"no"`, `break` the loop.
3. If they type `"yes"`, ask for their name and age using `input()`, then pass their age to the `borrow_book()` function!

---
*If you get stuck, try breaking the problem down into smaller pieces. You can always peek at `review_solution.py` for a hint!*
