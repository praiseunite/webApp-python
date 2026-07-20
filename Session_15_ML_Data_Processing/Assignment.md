# Assignment: Preparing Housing Data for ML 🏠🤖

## Objective
Take a raw, messy dataset (`raw_housing_data.csv`) and apply a complete Machine Learning data processing pipeline to it using Pandas and Scikit-Learn.

## Dataset
You are provided with `raw_housing_data.csv`. It contains data about houses and whether they were sold quickly.
- **Features (X):** `Square_Footage`, `Bedrooms`, `Age_of_Home`, `Neighborhood`
- **Target Variable (y):** `Sold_Quickly` (Yes/No)

Notice that the data has missing values (`NaN`), categorical text (`Neighborhood`, `Sold_Quickly`), and numerical columns on vastly different scales (e.g., `Square_Footage` vs. `Bedrooms`).

## Requirements

### 1. Load Data & Separate Features from Target
- Load the CSV using Pandas.
- Separate the data into features `X` (all columns EXCEPT `Sold_Quickly`) and target `y` (`Sold_Quickly`).

### 2. Handle Missing Data (`SimpleImputer`)
- Use `SimpleImputer` to replace missing values in the numerical columns (`Square_Footage`, `Bedrooms`, `Age_of_Home`) with the **median** value of each column.

### 3. Encode Categorical Data 
- **Target (y):** Use `LabelEncoder` to convert the `Sold_Quickly` column into 0s and 1s.
- **Features (X):** The `Neighborhood` column is text (e.g., 'Downtown', 'Suburb'). Since we cannot use math on words, and `LabelEncoder` implies an order, we should theoretically use `OneHotEncoder`. However, for this assignment, to keep it simple, use **Pandas `get_dummies()`** OR `OneHotEncoder` to encode the `Neighborhood` column. *Hint: `pd.get_dummies(X, columns=['Neighborhood'])` is the easiest way!*

### 4. Feature Scaling (`StandardScaler`)
- Use `StandardScaler` to standardize all the features in `X`. 
- Print the final scaled feature array `X` and encoded target array `y`.

---

## Instructions
1. Open `assignment_starter.py`.
2. Implement the requirements described above.
3. Your final output should be an array `X` of numbers (all roughly between -3 and 3) and an array `y` of 0s and 1s. This data is now perfectly ready to be fed into a Machine Learning algorithm!
