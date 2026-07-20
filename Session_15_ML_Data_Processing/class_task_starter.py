import pandas as pd
import numpy as np
# TODO: Import SimpleImputer
# TODO: Import LabelEncoder

# Toy Dataset
data = {
    'Country': ['France', 'Spain', 'Germany', 'Spain', 'Germany', 'France'],
    'Age': [44, 27, 30, 38, np.nan, 35],
    'Salary': [72000, 48000, 54000, 61000, 58000, np.nan],
    'Purchased': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)
print("--- ORIGINAL DATA ---")
print(df)
print("\n")

# --- TASK 1: Handle Missing Data in Age and Salary ---
# TODO: Create SimpleImputer instance
# imputer = ...

# TODO: Fit and transform the 'Age' and 'Salary' columns
# df[['Age', 'Salary']] = ...


# --- TASK 2: Encode the 'Purchased' Column ---
# TODO: Create LabelEncoder instance
# le = ...

# TODO: Fit and transform the 'Purchased' column
# df['Purchased'] = ...

print("--- PROCESSED DATA ---")
print(df)
