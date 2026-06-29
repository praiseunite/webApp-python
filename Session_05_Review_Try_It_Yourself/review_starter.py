# Session 5: Try It Yourself
# Choose Option A (Library System) or Option B (Grade Calculator)
# Complete the TODOs for your chosen project.

# ============================================================
# OPTION A: Library Borrowing System
# ============================================================

# TODO: Import receipt_module

# TODO: Create your library catalog as a list of dictionaries
# Each book should have: "title", "author", "available"
# library = [
#     {"title": "...", "author": "...", "available": True},
# ]


# TODO: Create function display_catalog(library)
#   - Loop through the library and print each book's title, author, and status


# TODO: Create function borrow_book(library, title, user_name, user_age)
#   - Check age (must be 12+)
#   - Find the book in the library list
#   - Check if it's available
#   - If yes, set available to False, call receipt_module.print_receipt(), return True
#   - Otherwise return False


# TODO: Main loop with menu
# while True:
#     print("\n1. View catalog")
#     print("2. Borrow a book")
#     print("3. Quit")
#     choice = input("Choose: ")
#     ... handle each choice with if/elif/else ...


# ============================================================
# OPTION B: Student Grade Calculator
# ============================================================

# TODO: Import your grade_helpers module (create grade_helpers.py first!)

# TODO: Create an empty list called all_students

# TODO: While loop to add students:
#   - Ask for name
#   - Ask for 3 scores using a for loop
#   - Calculate average and grade using your module
#   - Store as dictionary and append to all_students
#   - Ask "Add another student?"

# TODO: Print each student's report card

# TODO: Sort students by average using sorted() with lambda

# TODO: Print the class ranking

# TODO: Print class summary (class average, highest scorer, lowest scorer)
