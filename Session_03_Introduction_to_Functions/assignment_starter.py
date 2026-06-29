# Assignment: Student Report Card Generator
# Complete the TODOs below to build your report card program.

# --- Step 1: Get student info ---
# TODO: Create a function called get_student_info()
#   - Ask the user for their name using input()
#   - Ask for their age and convert to int
#   - Return both values: return name, age


# --- Step 2: Get scores ---
# TODO: Create a function called get_scores()
#   - Create an empty list called 'scores'
#   - Use a for loop with range(3) to ask for 3 subject scores
#   - Convert each to int and append to the scores list
#   - Return the scores list


# --- Step 3: Calculate average ---
# TODO: Create a function called calculate_average(scores)
#   - Calculate: total / number of scores
#   - Hint: sum(scores) gives the total, len(scores) gives the count
#   - Return the average


# --- Step 4: Determine grade ---
# TODO: Create a function called get_grade(average)
#   - 70+: return "A - Excellent"
#   - 60-69: return "B - Very Good"
#   - 50-59: return "C - Good"
#   - 40-49: return "D - Pass"
#   - Below 40: return "F - Fail"


# --- Step 5: Print report card ---
# TODO: Create a function called print_report(name, age, scores, average, grade)
#   - Print a nicely formatted report card showing all the student's info
#   - Use a for loop to print each subject score with a number (Subject 1, Subject 2, etc.)


# --- Step 6: Run the program ---
# TODO: Call all the functions in order:
#   name, age = get_student_info()
#   scores = get_scores()
#   average = calculate_average(scores)
#   grade = get_grade(average)
#   print_report(name, age, scores, average, grade)

print("=== STUDENT REPORT CARD GENERATOR ===\n")
# Your function calls go here:
