# Class Task: Introduction to Scikit-Learn Preprocessing 🧹

## Objective
Your task is to practice the basic syntax of Scikit-Learn's preprocessing tools on a small toy dataset. 

## Instructions
1. Open `class_task_starter.py`.
2. A small Pandas DataFrame has been provided. Note that it has missing values (`NaN`) in the 'Age' and 'Salary' columns, and a text category in the 'Purchased' column.
3. **Task 1: Handle Missing Data**
   - Import `SimpleImputer` from `sklearn.impute`.
   - Create an imputer that replaces missing values with the `mean`.
   - Apply the imputer to the 'Age' and 'Salary' columns.
4. **Task 2: Encode Categorical Data**
   - Import `LabelEncoder` from `sklearn.preprocessing`.
   - Use the encoder to transform the 'Purchased' column (Yes/No) into numbers (1/0).
5. Print the final cleaned DataFrame.
