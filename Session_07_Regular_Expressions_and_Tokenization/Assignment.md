# Assignment: Mini-Project 2 Expansion — Smart Profile Validator

## Objective
Use Regular Expressions to validate and clean user input in the Profile App before saving it to the file. This is exactly how real-world forms and sign-up pages work.

## Background
In the current `assignment_starter.py` from Session 6, the app blindly saves whatever the user types. A user could enter `"abc"` as their phone number and the app would save it without complaint. Let's fix that with regex validation!

## Instructions

### Step 1: Email Validation
1. After asking for the user's name, also ask: `"Enter your email address: "`
2. Write a regex pattern to validate that the input looks like a proper email (contains `@` and a domain like `.com`).
3. If the email is invalid, print `"Invalid email format!"` and ask again (use a `while` loop).

### Step 2: Phone Number Validation
1. Ask the user: `"Enter your phone number (e.g., 0801-234-5678): "`
2. Write a regex pattern using `re.fullmatch()` to ensure it matches the format `XXXX-XXX-XXXX` (4 digits, dash, 3 digits, dash, 4 digits).
3. If the format is wrong, print an error and ask again.

### Step 3: Clean and Save
1. Before saving to `user_profile.txt`, use `re.sub()` to strip any leading/trailing whitespace or multiple spaces from the user's name.
2. Save the validated name, email, and phone number to the file.

### Step 4: Tokenize a Bio
1. Ask the user: `"Write a short bio about yourself: "`
2. Use `re.findall(r"\w+", bio.lower())` to tokenize their bio into a list of words.
3. Print: `"Your bio contains [N] words: [list of tokens]"`
4. Save the token count to the profile file too.

## Expected Program Flow
```
Enter your name: Alice
Enter your email: not-an-email
Invalid email format! Try again.
Enter your email: alice@example.com ✓
Enter your phone (e.g., 0801-234-5678): 12345
Invalid phone format! Try again.
Enter your phone (e.g., 0801-234-5678): 0801-234-5678 ✓
Write a short bio: I love coding and solving problems
Your bio contains 6 words: ['i', 'love', 'coding', 'and', 'solving', 'problems']
Profile saved successfully!
```
