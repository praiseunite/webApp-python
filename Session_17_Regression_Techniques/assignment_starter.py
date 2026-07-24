"""
ASSIGNMENT STARTER — Session 17: Multiple Linear Regression
============================================================
Task: Build a house price predictor for LagosHomes Ltd.
      using Multiple Linear Regression.

Instructions: Complete all 6 parts as described in Assignment.md
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =============================================================
# DATASET GENERATION — Run this to create the data
# =============================================================
np.random.seed(99)
n = 150

df = pd.DataFrame({
    'Size_sqm':              np.random.randint(50, 500, n),
    'Bedrooms':              np.random.randint(1, 7, n),
    'Bathrooms':             np.random.randint(1, 5, n),
    'Distance_to_Island_km': np.random.uniform(1, 40, n).round(1),
    'Age_years':             np.random.randint(0, 50, n),
    'Has_BQ':                np.random.randint(0, 2, n),
    'Is_Serviced_Estate':    np.random.randint(0, 2, n),
})

# Realistic Lagos property price formula
df['Price_Naira'] = (
    df['Size_sqm']              * 180000   +
    df['Bedrooms']              * 1200000  +
    df['Bathrooms']             * 800000   +
    df['Distance_to_Island_km'] * -300000  +
    df['Age_years']             * -90000   +
    df['Has_BQ']                * 2000000  +
    df['Is_Serviced_Estate']    * 5000000  +
    np.random.normal(0, 3000000, n)
).clip(5000000).round(-3)

print("✅ Dataset generated!")
print(df.head())
print(f"\nShape: {df.shape}")

# =============================================================
# PART 1: EXPLORE THE DATA
# TODO 1a: Print df.shape and df.describe()
# TODO 1b: Print df.isnull().sum()
# TODO 1c: Plot a correlation heatmap using seaborn
#          sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
# =============================================================


# =============================================================
# PART 2: PREPARE THE DATA
# TODO 2a: Separate X (all columns except 'Price_Naira') and y ('Price_Naira')
# TODO 2b: Split: test_size=0.2, random_state=42
# TODO 2c: Apply StandardScaler to X_train and X_test
#          (fit on train, transform both)
# =============================================================
X = None  # Replace
y = None  # Replace

X_train, X_test, y_train, y_test = None, None, None, None

scaler = StandardScaler()
X_train_scaled = None  # Replace: scaler.fit_transform(X_train)
X_test_scaled  = None  # Replace: scaler.transform(X_test)

# =============================================================
# PART 3: TRAIN THE MODEL
# TODO 3a: Instantiate and fit LinearRegression
# TODO 3b: Print the intercept
# TODO 3c: Print a table of feature names → coefficients
#          Hint: pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_})
# =============================================================
model = None  # Replace

# =============================================================
# PART 4: EVALUATE
# TODO: Calculate and print MAE, MSE, RMSE, and R²
# =============================================================
# y_pred = model.predict(X_test_scaled)

# mae  = ?
# mse  = ?
# rmse = ?
# r2   = ?

# =============================================================
# PART 5: VISUALIZE — Actual vs. Predicted Scatter Plot
# TODO: scatter(actual, predicted), add perfect-prediction line (red dashed)
#       Label axes in ₦ Millions
# =============================================================


# =============================================================
# PART 6: PREDICT NEW PROPERTIES
# Property A (Luxury): 350sqm, 5bed, 4bath, 3km, 2yr, BQ=1, Estate=1
# Property B (Starter): 90sqm, 2bed, 1bath, 22km, 15yr, BQ=0, Estate=0
# TODO: Create DataFrames for each, scale them, predict, and print nicely
# =============================================================
property_A = pd.DataFrame({
    'Size_sqm':              [350],
    'Bedrooms':              [5],
    'Bathrooms':             [4],
    'Distance_to_Island_km': [3.0],
    'Age_years':             [2],
    'Has_BQ':                [1],
    'Is_Serviced_Estate':    [1]
})

property_B = pd.DataFrame({
    'Size_sqm':              [90],
    'Bedrooms':              [2],
    'Bathrooms':             [1],
    'Distance_to_Island_km': [22.0],
    'Age_years':             [15],
    'Has_BQ':                [0],
    'Is_Serviced_Estate':    [0]
})

# Scale and predict Property A and B...
