# Assignment: Mini-Project 1 Refactor (Organizing the Profile)

## Objective
Take the messy code from Session 2 and organize it into clean, reusable functions.

## Instructions
Open `assignment_starter.py` and complete the following:
1. Define a function called `get_user_info()`:
   - Inside it, ask the user for their name and age using `input()`.
   - `return` both the name and age (e.g., `return name, age`).
2. Define a function called `check_age(age)`:
   - It should take `age` as a parameter.
   - If the age is >= 18, `print` that the profile is for an adult.
   - Else, `print` that the profile is for a minor.
3. At the bottom of the script, call `get_user_info()` and store the results in variables.
4. Then, pass the stored age into the `check_age()` function.
