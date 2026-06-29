# Assignment: Grade Processing System with Modules
# Complete the TODOs below.

# --- Step 1: Import your module ---
# TODO: import grade_tools
# (Make sure you've created grade_tools.py first!)


# --- Step 2: Get student info ---
print("=== STUDENT REPORT CARD ===\n")

# TODO: Ask the user for their name using input()

# TODO: Create an empty list called 'scores'
# TODO: Use a for loop with range(3) to ask for 3 subject scores
#   - Convert each to int and append to scores list


# --- Step 3: Use the module functions ---
# TODO: Call grade_tools.calculate_average(scores) and store in 'average'
# TODO: Call grade_tools.get_grade(average) and store in 'grade'
# TODO: Call grade_tools.get_remark() to get a remark
#   Hint: You'll need to extract just the letter from the grade string
#   The grade looks like "A - Excellent", so grade[0] gives you "A"


# --- Step 4: Print the report card ---
# TODO: Print a formatted report card showing:
#   - Student name
#   - Each subject score (use a for loop)
#   - Average
#   - Grade
#   - Remark


# --- STRETCH: Lambda birth year ---
# TODO: Import and use grade_tools.get_birth_year to show birth year
# Ask for age first, then: birth_year = grade_tools.get_birth_year(age)


# --- STRETCH: Sort multiple students ---
# TODO: Create a list of student dictionaries, each with "name" and "average"
# TODO: Use sorted() with a lambda to rank them by average (highest first)
# TODO: Print the ranking
