# Class Task: Build a Quiz Game

## What You'll Build
A fun quiz game that asks the player 5 questions, checks their answers, tracks their score, and announces how they did at the end. This uses **lists**, **loops**, **if/else**, and **operators** — everything from today's session.

---

## Part 1: The Quick Quiz (Do this in class together)

### Instructions
Open your Python editor and build this step by step:

1. Create a **list** of 5 quiz questions (strings):
   ```python
   questions = [
       "What is the capital of Nigeria?",
       "How many continents are there?",
       "What does CPU stand for?",
       "In what year did Nigeria gain independence?",
       "What planet is closest to the sun?"
   ]
   ```

2. Create a matching **list** of correct answers:
   ```python
   answers = ["abuja", "7", "central processing unit", "1960", "mercury"]
   ```

3. Create a variable `score` and set it to `0`.

4. Use a **`for` loop** to go through each question:
   - Print the question
   - Take the player's answer using `input()`
   - Convert their answer to lowercase using `.lower()` (so "Abuja" matches "abuja")
   - Use an **`if` statement** to check if their answer matches the correct answer
   - If correct: add 1 to score and print "Correct!"
   - If wrong: print the right answer so they learn

5. After the loop, print the final score out of 5.

6. Use **`if/elif/else`** to give a rating:
   - 5 out of 5: "Perfect score! You're a genius!"
   - 3 or 4: "Good job! Almost there!"
   - 1 or 2: "Keep studying, you'll get there!"
   - 0: "Oops! Better luck next time!"

---

## Part 2: Upgrade It (Try on your own, 10-15 minutes)

Pick **one or more** upgrades to add:

### Upgrade A: Use a Dictionary Instead
Rewrite the quiz using a **dictionary** where the key is the question and the value is the answer. This is cleaner than having two separate lists:
```python
quiz = {
    "What is the capital of Nigeria?": "abuja",
    "How many continents are there?": "7",
    # ... add more
}
```
Then loop through it with `for question, correct_answer in quiz.items():`

### Upgrade B: Add a Timer Message
After the quiz, tell the player how they compare:
```python
percentage = (score / total_questions) * 100
print(f"You scored {percentage}%")
```

### Upgrade C: Ask "Play Again?"
Wrap the whole quiz in a `while` loop. After showing the score, ask the player if they want to play again. If they type "no", `break` out of the loop.

---

## Expected Output (Part 1)
```
=== PYTHON QUIZ GAME ===

Question 1: What is the capital of Nigeria?
Your answer: Abuja
Correct!

Question 2: How many continents are there?
Your answer: 6
Wrong! The answer is: 7

Question 3: What does CPU stand for?
Your answer: central processing unit
Correct!

Question 4: In what year did Nigeria gain independence?
Your answer: 1960
Correct!

Question 5: What planet is closest to the sun?
Your answer: venus
Wrong! The answer is: mercury

=== RESULTS ===
Your score: 3 / 5
Good job! Almost there!
```

---

You can view the solution in `class_task_solution.py`.
