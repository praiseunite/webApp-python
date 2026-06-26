# Assignment: Mini-Project 1 Refactor (Modules & Lambda)

## Objective
Move the core logic of our Profile App into a separate module to keep the main file clean.

## Instructions
Open `assignment_starter.py` and complete the following:
1. Create a new file named `profile_tools.py`.
2. Move your `check_age(age)` function from Session 3 into `profile_tools.py`.
3. In `profile_tools.py`, create a Lambda function called `get_birth_year` that takes `age` and returns `2024 - age`.
4. In your `assignment_starter.py`, import `profile_tools`.
5. Call `profile_tools.check_age()` and `profile_tools.get_birth_year()` to print the user's birth year.
