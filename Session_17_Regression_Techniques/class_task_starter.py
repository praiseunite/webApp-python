"""
CLASS TASK STARTER — Session 17: Simple Linear Regression
==========================================================
Task: Predict a student's exam score from hours studied.

Instructions: Complete all the TODO sections below.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# =============================================================
# DATA — Student Study Hours vs Exam Scores
# =============================================================
hours_studied = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5,
                 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5]

exam_scores   = [35, 42, 48, 52, 58, 62, 65, 68, 70, 74,
                 76, 79, 81, 84, 86, 88, 90, 92, 94, 96]

print("=== Student Exam Score Predictor ===\n")
print(f"Total students in dataset: {len(hours_studied)}")

# =============================================================
# TODO 1: CREATE A PANDAS DATAFRAME
# - Create a DataFrame with columns 'Hours_Studied' and 'Exam_Score'
# - Print the first 5 rows
# =============================================================
df = None  # Replace with pd.DataFrame(...)
# print(df.head())

# =============================================================
# TODO 2: SEPARATE FEATURES (X) AND TARGET (y)
# IMPORTANT: X must be 2D — use double brackets df[['Hours_Studied']]
# =============================================================
X = None  # Features (2D)
y = None  # Target

# =============================================================
# TODO 3: SPLIT DATA
# test_size=0.25, random_state=0
# =============================================================
X_train, X_test, y_train, y_test = None, None, None, None

# =============================================================
# TODO 4: CREATE AND TRAIN THE MODEL
# - Instantiate LinearRegression()
# - Call model.fit() on training data
# - Print the intercept and slope (coefficient)
# - Print the full equation: Score = β₀ + β₁ × Hours_Studied
# =============================================================
model = None
# model.fit(...)
# print(f"Intercept (β₀): {model.intercept_:.4f}")
# print(f"Slope (β₁):     {model.coef_[0]:.4f}")

# =============================================================
# TODO 5: EVALUATE THE MODEL
# - Predict on X_test
# - Print R² Score and MAE
# =============================================================
# y_pred = model.predict(X_test)
# r2  = r2_score(y_test, y_pred)
# mae = mean_absolute_error(y_test, y_pred)
# print(f"R² Score: {r2:.4f}")
# print(f"MAE:      {mae:.2f} marks")

# =============================================================
# TODO 6: VISUALIZE
# - Scatter: training data (blue circles), test data (red diamonds)
# - Line: regression line in orange across full X range
# - Add title, axis labels, legend, grid
# =============================================================


# =============================================================
# TODO 7: NEW PREDICTION
# - Predict the score for a student who studies 7.5 hours
# - Print: "A student who studies 7.5 hours is predicted to score: XX.XX / 100"
# =============================================================
new_hours = np.array([[7.5]])
# predicted_score = model.predict(new_hours)[0]
# print(f"\nA student who studies 7.5 hours is predicted to score: {predicted_score:.2f} / 100")
