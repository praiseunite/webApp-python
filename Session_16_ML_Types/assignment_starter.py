"""
ASSIGNMENT STARTER — Session 16: K-Means Clustering
=====================================================
Task: Segment ShopNaija e-commerce customers into groups
      using K-Means clustering.

Instructions: Follow the TODO comments and the Assignment.md file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# =============================================================
# GENERATE THE DATASET (run this once to create the CSV,
# or just work with the DataFrame directly)
# =============================================================
np.random.seed(42)

# Three customer groups (unknown to the algorithm)
n = 40
budget = pd.DataFrame({
    'CustomerID':        range(1, n+1),
    'Annual_Spend_Naira':np.random.normal(120000, 25000, n).clip(50000),
    'Monthly_Orders':    np.random.normal(2.5, 0.8, n).clip(0.5).round(1),
    'Avg_Order_Value':   np.random.normal(4800, 1000, n).clip(1000),
    'Returns_Rate':      np.random.normal(0.18, 0.05, n).clip(0, 1).round(3)
})
regular = pd.DataFrame({
    'CustomerID':        range(n+1, 2*n+1),
    'Annual_Spend_Naira':np.random.normal(550000, 80000, n).clip(300000),
    'Monthly_Orders':    np.random.normal(8, 1.5, n).clip(3).round(1),
    'Avg_Order_Value':   np.random.normal(18000, 3000, n).clip(5000),
    'Returns_Rate':      np.random.normal(0.09, 0.03, n).clip(0, 1).round(3)
})
premium = pd.DataFrame({
    'CustomerID':        range(2*n+1, 3*n+1),
    'Annual_Spend_Naira':np.random.normal(2500000, 400000, n).clip(1200000),
    'Monthly_Orders':    np.random.normal(20, 4, n).clip(10).round(1),
    'Avg_Order_Value':   np.random.normal(80000, 15000, n).clip(30000),
    'Returns_Rate':      np.random.normal(0.04, 0.02, n).clip(0, 1).round(3)
})

df = pd.concat([budget, regular, premium], ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv('customer_data.csv', index=False)
print("customer_data.csv created!")

# Load from CSV (as students will do)
df = pd.read_csv('customer_data.csv')

# =============================================================
# PART 1: EXPLORE & PREPARE THE DATA
# TODO 1a: Print df.head(), df.shape, and df.describe()
# TODO 1b: Check for missing values with df.isnull().sum()
# TODO 1c: Drop 'CustomerID' and scale the remaining features
#          using StandardScaler. Store scaled data in X_scaled.
# =============================================================


# =============================================================
# PART 2: FIND THE OPTIMAL K (ELBOW METHOD)
# TODO 2a: Loop K from 1 to 8, fit KMeans, record .inertia_
# TODO 2b: Plot the Elbow Curve
# TODO 2c: In a comment, state your chosen K and why
# =============================================================

# chosen_k = ?  # <-- set this after analysing the elbow plot

# =============================================================
# PART 3: APPLY K-MEANS WITH YOUR CHOSEN K
# TODO 3a: Fit a final KMeans model with your chosen K
# TODO 3b: Add the cluster labels to the ORIGINAL df as column 'Segment'
# =============================================================


# =============================================================
# PART 4: ANALYZE & NAME THE SEGMENTS
# TODO 4a: Group by 'Segment' and compute the mean of each feature
# TODO 4b: Print the summary table
# TODO 4c: In print statements, identify which cluster is:
#           Budget / Regular / Premium
# =============================================================


# =============================================================
# PART 5: VISUALIZE THE SEGMENTS
# TODO 5: Scatter plot — Annual_Spend_Naira vs Monthly_Orders
#         Color points by Segment, add title, labels, legend
# =============================================================
