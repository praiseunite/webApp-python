# Assignment: Mini-Project — Student Report Card Generator

## What You'll Build
A program that uses **functions** to collect student data, calculate grades, and print a formatted report card. This teaches you to break a big problem into small, reusable functions — the most important habit in programming.

---

## Base Level (Everyone should complete this)

Open `assignment_starter.py` and complete the TODOs:

1. **Create a function `get_student_info()`** that:
   - Asks the user for their name using `input()`
   - Asks for their age and converts it to an integer
   - Returns both values: `return name, age`

2. **Create a function `get_scores()`** that:
   - Creates an empty list called `scores`
   - Uses a `for` loop with `range(3)` to ask the user for 3 subject scores
   - Converts each score to an integer and appends it to the list
   - Returns the list of scores

3. **Create a function `calculate_average(scores)`** that:
   - Takes a list of scores as a parameter
   - Calculates the average: `sum of all scores / number of scores`
   - Returns the average
   - Hint: `sum(scores)` gives you the total, `len(scores)` gives the count

4. **Create a function `get_grade(average)`** that:
   - Takes the average as a parameter
   - Returns a grade string based on these rules:
     - 70 and above: `"A - Excellent"`
     - 60-69: `"B - Very Good"`
     - 50-59: `"C - Good"`
     - 40-49: `"D - Pass"`
     - Below 40: `"F - Fail"`

5. **Create a function `print_report(name, age, scores, average, grade)`** that prints a formatted report card:
   ```
   ================================
        STUDENT REPORT CARD
   ================================
   Name:    Amina
   Age:     22
   
   Subject 1:  75
   Subject 2:  82
   Subject 3:  68
   
   Average:    75.0
   Grade:      A - Excellent
   ================================
   ```

6. **At the bottom of the script**, call all the functions in order:
   ```python
   name, age = get_student_info()
   scores = get_scores()
   average = calculate_average(scores)
   grade = get_grade(average)
   print_report(name, age, scores, average, grade)
   ```

---

## Stretch Level

1. **Add a `get_remark(grade)` function** that returns an encouraging message based on the grade:
   - A: "Outstanding performance! Keep it up!"
   - B: "Great work! Push for that A next time."
   - C: "Good effort. A little more study will get you higher."
   - D: "You passed, but there's room for improvement."
   - F: "Don't give up! Talk to your teacher for extra help."

2. **Allow custom number of subjects:** Change `get_scores()` to take a parameter for how many subjects:
   ```python
   def get_scores(num_subjects):
   ```

---

## Boss Level

1. **Multiple students:** Wrap everything in a `while` loop that keeps asking "Add another student? (yes/no)". Store each student's data in a **list of dictionaries**:
   ```python
   all_students = []
   # Each student is: {"name": "Amina", "average": 75.0, "grade": "A"}
   ```

2. **Class summary:** After all students are entered, print a summary showing the class average and the highest-scoring student.

---

## Submission
Complete your work in `assignment_starter.py` and be ready to walk through your code in the next session.
