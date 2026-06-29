# Class Task: Password Strength Checker

## What You'll Build
A function that analyzes a password and tells the user if it's **Weak**, **Medium**, or **Strong** based on its length and content. This is a real feature found in every sign-up form on the internet!

---

## Part 1: Basic Strength Checker (Do this in class together)

### Instructions
Open your Python editor and build this step by step:

1. Create a function called `check_password_strength(password)` that takes one parameter: the password string.

2. Inside the function, check the password's strength using these rules:
   - **Strong:** Length is 8 or more AND contains at least one number
   - **Medium:** Length is 6 or more (but didn't qualify as Strong)
   - **Weak:** Anything shorter than 6 characters

3. The function should **return** the strength as a string: `"Strong"`, `"Medium"`, or `"Weak"`.

4. **Hint for checking if password contains a number:**
   ```python
   has_number = False
   for char in password:
       if char.isdigit():
           has_number = True
   ```

5. Outside the function, test it with these passwords:
   ```python
   print(check_password_strength("abc"))           # Should print: Weak
   print(check_password_strength("abcdef"))         # Should print: Medium
   print(check_password_strength("python2024"))     # Should print: Strong
   print(check_password_strength("12345678"))        # Should print: Strong
   print(check_password_strength("short1"))          # Should print: Medium (6 chars with number, but we only check len >= 8 for strong)
   ```

6. Now make it interactive: ask the user to type a password using `input()`, pass it to your function, and display the result.

---

## Part 2: Upgrade It (Try on your own, 10-15 minutes)

### Upgrade A: Visual Feedback
Add a function called `display_strength(password)` that calls `check_password_strength()` and prints a visual bar:
```
Password: python2024
Strength: Strong
[##########] Your password is strong!

Password: hello
Strength: Weak
[###-------] Your password is weak. Try adding numbers and more characters.
```

### Upgrade B: Password Suggestions
If the password is Weak or Medium, print a helpful tip:
- Weak: "Tip: Make your password at least 6 characters long."
- Medium: "Tip: Add numbers to make your password stronger."

### Upgrade C: Multiple Password Checker
Create a **list** of passwords and use a **for loop** to check each one:
```python
test_passwords = ["cat", "python", "Secure2024", "ab", "hello123"]
for pw in test_passwords:
    strength = check_password_strength(pw)
    print(f"'{pw}' -> {strength}")
```

---

## Expected Output (Part 1)
```
=== PASSWORD STRENGTH CHECKER ===

Testing passwords...
"abc" -> Weak
"abcdef" -> Medium
"python2024" -> Strong
"12345678" -> Strong

Now try your own!
Enter a password: mypassword
Your password strength: Medium
```

---

You can view the solution in `class_task_solution.py`.
