"""
REVIEW STARTER — Session 18: Try It Yourself
=============================================
Book Sessions 12–15: Pandas | Visualization | ML Types | Regression

Instructions:
  - Complete ONE of the three main project sections (A, B, or C).
  - Complete Part 2 (Integrated Mini-Challenge) regardless of your choice.
  - Complete the debug challenge in debug_challenge.py.

Read Review_Tasks.md for full task descriptions.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (accuracy_score, classification_report,
                             r2_score, mean_absolute_error, mean_squared_error)

# =============================================================
# SHARED: DATA LOADING & CLEANING
# (Used by all three project options — complete this first!)
# =============================================================

def load_and_clean():
    """
    Load student_data.csv and return a cleaned DataFrame.
    Apply the cleaning steps from Task A1.
    """
    df = pd.read_csv('student_data.csv')

    # TODO A1-1: Print shape and head
    # print(df.shape)
    # print(df.head())

    # TODO A1-2: Fix Name column → Title Case
    # df['Name'] = ...

    # TODO A1-3: Strip whitespace from City column
    # df['City'] = ...

    # TODO A1-4: Drop rows where Score_ML is missing
    # df = df.dropna(subset=[...])

    # TODO A1-5: Fill missing Score_Pandas with the median
    # df['Score_Pandas'] = df['Score_Pandas'].fillna(...)

    # TODO A1-6: Remove rows where Age is negative
    # df = df[df['Age'] >= 0]

    print(f"Cleaned dataset shape: {df.shape}")
    return df


# Load the data
df = load_and_clean()


# =============================================================
# SECTION A: Student Analytics Dashboard (Pandas + Visualization)
# =============================================================
# Uncomment and complete the section below if you chose Option A

# --- A2: ANALYSIS ---
# TODO A2-1: GroupBy Course → mean of all 4 score columns
# course_means = df.groupby('Course')[['Score_Pandas','Score_Visualization',
#                                       'Score_ML','Score_Regression']].mean()
# print(course_means)

# TODO A2-2: Top 3 students by total score
# df['Total_Score'] = df[['Score_Pandas','Score_Visualization',
#                           'Score_ML','Score_Regression']].sum(axis=1)
# top3 = ...
# print(top3[['Name','Total_Score']])

# TODO A2-3: Percentage of students from Lagos
# lagos_pct = ...
# print(f"Students from Lagos: {lagos_pct:.1f}%")

# --- A3: VISUALIZATION ---
# TODO A3-1: Bar chart — Average Score_ML per Course
# ...

# TODO A3-2: Histogram — Distribution of Score_Regression
# ...

# TODO A3-3: Seaborn Box Plot — Score_Pandas distribution per Gender
# ...


# =============================================================
# SECTION B: Exam Predictor (Regression + Classification)
# =============================================================
# Uncomment and complete below if you chose Option B

# --- B1: DATA PREPARATION ---
# TODO B1-1: Encode Course using pd.get_dummies(), drop_first=True
# df_b = pd.get_dummies(df, columns=['Course'], drop_first=True)

# TODO B1-2: Encode Gender (M=0, F=1)
# le = LabelEncoder()
# df_b['Gender'] = le.fit_transform(df['Gender'])

# TODO B1-3: Drop non-numeric / non-feature columns
# df_b = df_b.drop(columns=['StudentID', 'Name', 'City', 'Scholarship'])

# --- B2: REGRESSION MODEL ---
# TODO B2-1: X = all columns except Score_Regression; y = Score_Regression
# X_reg = ...
# y_reg = ...

# TODO B2-2: Split 80/20 and train LinearRegression
# ...

# TODO B2-3: Print MAE, RMSE, R²
# ...

# TODO B2-4: Scatter plot — Actual vs Predicted
# ...

# --- B3: CLASSIFICATION MODEL ---
# TODO B3-1: Encode Scholarship (Yes=1, No=0)
# df_b['Scholarship_num'] = df_b['Scholarship'].map({'Yes':1, 'No':0})  # before drop

# TODO B3-2: X same features; y = Scholarship_num
# ...

# TODO B3-3: Train LogisticRegression and print accuracy + report
# ...

# TODO B3-4: Predict for an average student
# avg_scores = X_cls.mean().values.reshape(1, -1)
# prediction = clf_model.predict(avg_scores)
# ...


# =============================================================
# SECTION C: K-Means Student Grouper (Unsupervised ML)
# =============================================================
# Uncomment and complete below if you chose Option C

# --- C1: PREPARE DATA ---
# TODO C1-1: Select 4 score columns and scale them
# score_cols = ['Score_Pandas','Score_Visualization','Score_ML','Score_Regression']
# X_cluster = df[score_cols].copy()
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X_cluster)

# --- C2: ELBOW METHOD ---
# TODO C2: Loop K=1 to 7, compute inertia, plot elbow curve
# inertia = []
# for k in range(1, 8):
#     ...
# # Comment: My chosen K is ___ because ___

# --- C3: APPLY K-MEANS ---
# TODO C3-1: Fit KMeans with chosen K, add 'Tier' column to df
# chosen_k = 3
# km = KMeans(n_clusters=chosen_k, random_state=42, n_init=10)
# df['Tier'] = km.fit_predict(X_scaled)

# TODO C3-2: Print summary table and name each tier
# tier_summary = df.groupby('Tier')[score_cols].mean()
# print(tier_summary)

# --- C4: VISUALIZE ---
# TODO C4-1: Scatter — Score_Pandas vs Score_ML, colored by Tier
# ...

# TODO C4-2: Bar chart — Average total score per Tier
# ...


# =============================================================
# PART 2: INTEGRATED MINI-CHALLENGE
# Complete this regardless of which project option you chose
# =============================================================

print("\n" + "=" * 60)
print("PART 2: INTEGRATED MINI-CHALLENGE")
print("=" * 60)

# TODO Q1: Correlation between Score_Pandas and Score_Regression
# corr = df[['Score_Pandas', 'Score_Regression']].corr()
# print(f"\nQ1 — Correlation:\n{corr}")

# TODO Q2: City with highest average Score_ML
# best_city = ...
# print(f"\nQ2 — City with highest avg ML score: {best_city}")

# TODO Q3: % of Data Science students who are ML competent (Score_ML >= 75)
# ds_students = df[df['Course'] == 'Data Science']
# competent_pct = ...
# print(f"\nQ3 — Competent DS students: {competent_pct:.1f}%")

# TODO Q4: Figure with 2 subplots (bar chart + pie chart)
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
# ...
# plt.tight_layout()
# plt.show()
