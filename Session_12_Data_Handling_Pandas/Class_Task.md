# Class Task: Introduction to Pandas DataFrame 🐼

## Objective
Practice loading a dataset, inspecting its contents, and performing basic text processing using Pandas.

## Instructions
1. Open `class_task_starter.py`.
2. A file named `employees.csv` is provided in your folder. Read this file into a Pandas DataFrame.
3. Print the first 5 rows of the DataFrame to inspect the data.
4. You will notice that the `Department` column has some messy whitespace (e.g., `" IT "`, `" HR "`). Use a Pandas text processing function (`str.strip()`) to clean this column.
5. Convert all the text in the `Department` column to uppercase using `.str.upper()`.
6. Print the cleaned DataFrame to verify your changes.

### Expected Output
The console should first print the messy data, and then print the cleaned data where the `Department` column has no extra spaces and is fully capitalized.
