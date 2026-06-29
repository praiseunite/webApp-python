# Assignment: Build a Grade Processing System with Modules

## What You'll Build
Take the Report Card Generator from Session 3 and **refactor it into modules**. You'll also add lambda-powered sorting to rank students. This mirrors how real projects evolve — you start with everything in one file, then organize as it grows.

---

## Base Level (Everyone should complete this)

Open `assignment_starter.py` and complete the TODOs:

1. **Create a new file** called `grade_tools.py` with these functions:

   **`calculate_average(scores)`** — Takes a list of scores, returns the average.

   **`get_grade(average)`** — Takes an average, returns the grade string:
   - 70+: "A - Excellent"
   - 60-69: "B - Very Good"
   - 50-59: "C - Good"
   - 40-49: "D - Pass"
   - Below 40: "F - Fail"

   **`get_remark(grade)`** — Takes a grade letter (just "A", "B", etc.), returns a motivational remark.

2. **In `assignment_starter.py`:**
   - Import your `grade_tools` module
   - Ask the user for their name and 3 subject scores
   - Use `grade_tools.calculate_average()` to get the average
   - Use `grade_tools.get_grade()` to get the grade
   - Print a formatted report card

### Expected Output
```
=== STUDENT REPORT CARD ===

Enter your name: Amina
Enter score for Subject 1: 75
Enter score for Subject 2: 82
Enter score for Subject 3: 68

================================
     REPORT CARD: Amina
================================
Subject 1:  75
Subject 2:  82
Subject 3:  68

Average:    75.0
Grade:      A - Excellent
Remark:     Outstanding performance!
================================
```

---

## Stretch Level

1. **Add a lambda sort:** Create a list of 3-5 students (each as a dictionary with "name" and "scores"). Use `sorted()` with a lambda to rank them by average score, highest first.

2. **Birth year calculator:** Add a lambda to `grade_tools.py`:
   ```python
   get_birth_year = lambda age: 2026 - age
   ```
   Import and use it to show the student's birth year on the report card.

3. **Use Python's `statistics` module:** Replace your average calculation with `statistics.mean()` — show that Python has built-in tools and you don't always need to write everything from scratch.

---

## Boss Level

1. **Create a package:** Create a folder called `school_utils/` with:
   - `__init__.py` (can be empty)
   - `grade_tools.py` (move your module here)
   - `display_tools.py` (a new module with a `print_report()` function)

   Import from the package: `from school_utils import grade_tools`

2. **Recursive GPA calculator:** Write a recursive function that calculates the cumulative GPA across multiple semesters (each semester is a list of scores).

---

## Submission
Complete your work in `assignment_starter.py` and `grade_tools.py`. Be ready to walk through your code in the review session.
