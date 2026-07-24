"""
DEBUGGING CHALLENGE — Session 18: Try It Yourself
==================================================
This file contains a broken ML pipeline.
Find and fix all 6 bugs described in Review_Tasks.md.

HOW TO USE:
  1. Read the code carefully.
  2. Try to run it — it will crash. Read the error message.
  3. Use the hints in Review_Tasks.md if you get stuck.
  4. Fix each bug one at a time and re-run until it prints results correctly.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegresion          # BUG 1
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("student_data.csv")

# Step 1: Drop missing values
df = df.dropna(subset=['Score_Pandas', 'Score_ML', 'Score_Regression'])
df = df[df['Age'] >= 0]

# Step 2: Prepare features and target
X = df[['Score_Pandas', 'Score_Visualization', 'Score_ML']]
y = df['Score_Regression']

# Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # BUG 2 (no random_state)

# Step 4: Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.fit_transform(X_test)             # BUG 3

# Step 5: Train model
model = LinearRegresion()                                  # (also BUG 1 here)
model.fit(X_train_scaled, y_train)

# Step 6: Predict and evaluate
y_pred = model.predict(X_test)                            # BUG 4

r2  = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"R² Score: {r2:.4f}")
print(f"MAE:      {mae:.2f}")

# Step 7: Predict for a new student [Score_Pandas=80, Score_Viz=75, Score_ML=85]
new_student = [80, 75, 85]                                # BUG 5
prediction  = model.predict(new_student)
print(f"Predicted Regression Score: {prediction[0]:.2f}")
