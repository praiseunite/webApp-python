# Class Task: Student Results File Manager

## Objective
Practice opening, writing, reading, and appending to files using Python's `with` statement and file modes.

## Instructions

### Part A: Write to a File
1. Open a file called `results.txt` in **write mode** (`"w"`).
2. Write the following three student results to the file, one per line:
   - `"Alice - 92\n"`
   - `"Bob - 78\n"`
   - `"Charlie - 85\n"`

### Part B: Read the File
1. Open `results.txt` in **read mode** (`"r"`).
2. Use `readlines()` to get all the lines as a list.
3. Loop through the list and print each result line.

### Part C: Append a New Student
1. Open `results.txt` in **append mode** (`"a"`).
2. Add a new line: `"Diana - 90\n"`.
3. Read and print the entire file again to confirm Diana was added without deleting the others.

**Bonus Challenge:** Add an `if/else` statement inside the loop in Part B: if the score (the number after the `-`) is 80 or above, also print `"(Distinction)"` next to the name.

See `class_task_solution.py` for the solution.
