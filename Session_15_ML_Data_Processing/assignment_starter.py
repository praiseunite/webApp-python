import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 1. Load Data
# df = pd.read_csv('raw_housing_data.csv')
# print("--- Original Data ---")
# print(df.head(10))

# Separate features (X) and target (y)
# X = ... (drop 'Sold_Quickly')
# y = ... (only 'Sold_Quickly')

# 2. Handle Missing Data (Imputation)
# numeric_cols = ['Square_Footage', 'Bedrooms', 'Age_of_Home']
# imputer = SimpleImputer(missing_values=np.nan, strategy='median')
# X[numeric_cols] = ...

# 3. Encode Categorical Data
# Target y: Yes/No -> 1/0
# le = LabelEncoder()
# y = ...

# Features X: Neighborhood -> Dummy variables
# X = pd.get_dummies(X, columns=['Neighborhood'])
# print("\n--- X after encoding ---")
# print(X.head())

# 4. Feature Scaling
# scaler = StandardScaler()
# X_scaled = ...

# print("\n--- Final Processed X (Scaled) ---")
# print(X_scaled)
# print("\n--- Final Processed y ---")
# print(y)
