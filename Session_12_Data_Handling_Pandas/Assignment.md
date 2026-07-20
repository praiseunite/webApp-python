# Assignment: Data Cleaning and Analysis with Pandas 📊

## Objective
Take raw, messy data from a CSV file, clean it up, perform some basic analysis (filtering), and save the cleaned data to a new file.

## Instructions
1. Open `assignment_starter.py`.
2. Load the `employees.csv` dataset.
3. **Data Inspection:** Print the `.info()` of the DataFrame to see which columns have missing values.
4. **Data Cleaning (Handling Missing Values):**
   - Fill the missing values in the `Salary` column with the *average (mean)* salary.
   - Fill the missing values in the `Join_Date` column with a default date: `'2023-01-01'`.
5. **Data Cleaning (Text Processing):**
   - Clean the `Name` column by removing any leading or trailing whitespaces.
6. **Data Manipulation (Filtering):**
   - Create a new DataFrame that *only* contains employees who work in the **'IT'** department (make sure you account for those messy whitespaces by cleaning the `Department` column first, just like we did in the Class Task!).
7. **File I/O:**
   - Save this filtered "IT Department" DataFrame to a new file called `it_employees.csv`. Set `index=False` so Pandas doesn't write row numbers to the file.

### Expected Outcome
By the end of the script, you should have successfully handled all missing values (no more NaNs), filtered the dataset down to just IT employees, and generated a clean `it_employees.csv` file.
