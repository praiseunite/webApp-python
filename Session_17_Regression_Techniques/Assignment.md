# Assignment: House Price Predictor — Multiple Linear Regression 🏠

## Objective
Build a complete **Multiple Linear Regression** pipeline to predict house prices in Lagos, Nigeria, using multiple property features. Deliver a model that a real estate agency could use to automatically estimate property values.

## Background
"LagosHomes Ltd." currently values properties manually using human agents, which is slow and inconsistent. They want a data-driven pricing model. Your model should:
1. Identify **which features most influence price**.
2. Predict the price of any new property input by the agent.
3. Communicate the model's reliability through evaluation metrics.

## Dataset
You will generate the dataset within the starter file. The dataset contains **150 house records** with the following features:

| Feature | Description | Type |
|---|---|---|
| `Size_sqm` | Property size in square metres | Numerical |
| `Bedrooms` | Number of bedrooms | Numerical |
| `Bathrooms` | Number of bathrooms | Numerical |
| `Distance_to_Island_km` | Distance to Lagos Island (business district) | Numerical |
| `Age_years` | Age of property | Numerical |
| `Has_BQ` | Has a boys' quarters (1=Yes, 0=No) | Binary |
| `Is_Serviced_Estate` | In a serviced estate (1=Yes, 0=No) | Binary |
| `Price_Naira` | **TARGET** — Property price in Naira | Numerical |

---

## Requirements

### Part 1: Load and Explore
1. Generate the dataset using the starter code.
2. Print: `.head()`, `.shape`, `.describe()`, and `.isnull().sum()`.
3. Plot a **correlation heatmap** using Seaborn's `heatmap` to see which features correlate most with price. *Hint: `sns.heatmap(df.corr(), annot=True, cmap='coolwarm')`*

### Part 2: Prepare the Data
1. Separate features `X` (all columns except `Price_Naira`) and target `y`.
2. Split: **80% train, 20% test**, `random_state=42`.
3. Apply `StandardScaler` to `X_train` and `X_test`.

### Part 3: Train the Model
1. Train a `LinearRegression` model on the scaled training data.
2. Print the **intercept** and a table of **feature names → coefficients**.

### Part 4: Evaluate the Model
Calculate and print all four metrics:
- **MAE** (Mean Absolute Error) in Naira
- **MSE** (Mean Squared Error)
- **RMSE** (Root Mean Squared Error) in Naira
- **R² Score** (as both a decimal and a percentage)

### Part 5: Visualize — Actual vs. Predicted
- Create a scatter plot of **Actual Price** (X-axis) vs **Predicted Price** (Y-axis).
- Add a red dashed **"Perfect Prediction" line** (where actual = predicted).
- Points close to this line = good predictions. Label axes in ₦ Millions.

### Part 6: Make Real Predictions
Predict the price for these two properties and print the results clearly:

**Property A (Luxury):**
- Size: 350 sqm | Bedrooms: 5 | Bathrooms: 4 | Distance: 3 km | Age: 2 years | Has BQ: Yes | Serviced Estate: Yes

**Property B (Starter Home):**
- Size: 90 sqm | Bedrooms: 2 | Bathrooms: 1 | Distance: 22 km | Age: 15 years | Has BQ: No | Serviced Estate: No

---

## Deliverables
- Completed `assignment_solution.py` with all 6 parts implemented.
- Correlation heatmap (displayed in window or saved as `correlation_heatmap.png`).
- Actual vs. Predicted scatter plot.

## Grading Criteria
| Criterion | Marks |
|---|---|
| Correct data preparation and scaling | 20 |
| Model trained and coefficients printed | 20 |
| All 4 evaluation metrics correct | 25 |
| Visualizations (heatmap + scatter plot) | 20 |
| New property predictions with clear output | 15 |
| **Total** | **100** |
