# Assignment: Mini-Project 2 Kickoff — Persistent Profile App

## Objective
Level up your CLI Profile App from Phase 1! Instead of losing the user's data when the program closes, we will now **save it to a file** and **reload it** the next time the program runs. We will also use exception handling to make the app bulletproof.

## Background
Right now, every time a student runs `profile_setup.py`, they have to re-enter all their information. Real applications persist data. Let's fix that!

## Instructions

### Step 1: Save to File
1. Open `assignment_starter.py` and modify the `get_user_info()` function.
2. After collecting the user's name and age, open a file called `user_profile.txt` in **write mode**.
3. Write the user's name and age to the file, each on its own line.
4. Print: `"Profile saved to user_profile.txt!"`

### Step 2: Load from File
1. Create a new function called `load_profile()`.
2. Inside, use a `try/except` block:
   - In the `try` section, open `user_profile.txt` in **read mode** and print its contents.
   - In the `except FileNotFoundError` section, print: `"No saved profile found. Please create one first."`

### Step 3: A Simple Menu
1. At the bottom of your script, instead of running the profile directly, show the user a simple menu:
   ```
   1. Create new profile
   2. Load existing profile
   3. Exit
   ```
2. Use `input()` to get their choice and an `if/elif/else` statement to call the right function.
3. Wrap the age `input()` conversion in a `try/except ValueError` block so that if the user accidentally types letters instead of a number, the app prints a helpful message instead of crashing.

## Expected Program Flow
```
Welcome to the Profile App!
1. Create new profile
2. Load existing profile
3. Exit
Enter choice: 2
No saved profile found. Please create one first.

Enter choice: 1
Enter your name: Alice
Enter your age: twenty     <-- User makes a mistake
Invalid! Please enter a number for age.
Enter your age: 20
Profile saved to user_profile.txt!

Enter choice: 2
Name: Alice
Age: 20
```
