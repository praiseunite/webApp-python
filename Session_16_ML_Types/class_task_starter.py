"""
CLASS TASK STARTER — Session 16: Logistic Regression
======================================================
Task: Build a Logistic Regression model to predict
      whether a bank customer will default on a loan.

Instructions: Follow the TODO comments below.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# =============================================================
# DATA — Bank Customer Records
# =============================================================
data = {
    'Age':             [22, 35, 45, 28, 52, 31, 40, 60, 27, 38, 49, 33, 55, 29, 42,
                        25, 37, 50, 34, 48, 26, 58, 30, 44, 36],
    'Income':          [45000, 80000, 120000, 55000, 200000, 70000, 95000, 250000, 48000, 85000,
                        150000, 72000, 180000, 52000, 110000, 40000, 88000, 160000, 78000, 130000,
                        42000, 220000, 65000, 105000, 90000],
    'Loan_Amount':     [150000, 200000, 350000, 180000, 500000, 220000, 300000, 600000, 160000, 250000,
                        400000, 230000, 450000, 170000, 320000, 140000, 260000, 420000, 210000, 380000,
                        145000, 550000, 195000, 310000, 270000],
    'Credit_Score':    [580, 720, 800, 610, 850, 680, 740, 820, 590, 710, 780, 650, 810, 600, 750,
                        560, 700, 790, 670, 760, 570, 830, 630, 730, 690],
    'Months_Employed': [12, 48, 120, 24, 200, 36, 84, 240, 18, 60, 156, 42, 180, 30, 96,
                        6,  54, 168,  48, 132, 8, 210, 28, 90, 66],
    'Defaulted':       [1,  0,   0,   1,  0,   0,  0,   0,  1,  0,   0,  0,  0,   1,  0,
                        1,  0,   0,   0,  0,   1,  0,   1,  0,  0]
}

df = pd.DataFrame(data)
print("Dataset loaded successfully!")
print(df.head())
print(f"\nShape: {df.shape}")
print(f"Default rate: {df['Defaulted'].mean()*100:.1f}%\n")

# =============================================================
# TODO 1: SEPARATE FEATURES AND TARGET
# - Create X with all columns EXCEPT 'Defaulted'
# - Create y with ONLY the 'Defaulted' column
# =============================================================
X = None  # Replace with your code
y = None  # Replace with your code

# =============================================================
# TODO 2: SPLIT DATA — 80% train, 20% test, random_state=42
# =============================================================
X_train, X_test, y_train, y_test = None, None, None, None  # Replace

# =============================================================
# TODO 3: CREATE AND TRAIN THE LOGISTIC REGRESSION MODEL
# =============================================================
model = None  # Instantiate LogisticRegression()
# Call model.fit() on the training data

# =============================================================
# TODO 4: EVALUATE THE MODEL
# - Predict on X_test
# - Print accuracy_score
# - Print classification_report
# =============================================================


# =============================================================
# TODO 5: MAKE A PREDICTION FOR A NEW CUSTOMER
# Features: Age=35, Income=85000, Loan_Amount=200000, 
#           Credit_Score=680, Months_Employed=48
# Print: "✅ LOW RISK - Likely to repay the loan."
# OR:    "⚠️  HIGH RISK - Likely to default on the loan."
# =============================================================
new_customer = np.array([[35, 85000, 200000, 680, 48]])

# Your prediction code here...
