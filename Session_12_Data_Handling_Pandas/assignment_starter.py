import pandas as pd

# Load the dataset
df = pd.read_csv('employees.csv')

# TODO: Print the .info() to see missing values

# TODO: Fill missing values in 'Salary' with the mean salary
# Hint: mean_salary = df['Salary'].mean()
# df['Salary'] = df['Salary'].fillna(...)

# TODO: Fill missing values in 'Join_Date' with '2023-01-01'

# TODO: Clean the 'Name' column by stripping whitespaces

# TODO: Clean the 'Department' column by stripping whitespaces and making it uppercase

# TODO: Filter the DataFrame to include ONLY employees in the 'IT' department
# it_df = df[...]

# TODO: Save the filtered DataFrame to 'it_employees.csv' (set index=False)

print("Data cleaning and filtering complete. Saved to it_employees.csv")
