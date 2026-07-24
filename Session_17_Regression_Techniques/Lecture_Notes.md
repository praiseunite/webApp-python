# Session 17: Regression Techniques for Machine Learning in Python 📈

Welcome to Session 17! In our last session, we explored the three types of Machine Learning and implemented **Logistic Regression** for classification. Today, we focus exclusively on **Regression** — one of the most fundamental and widely-used techniques in supervised machine learning, used for predicting **continuous numerical values**.

## 📝 Learning Objectives
By the end of this session, you will be able to:
1. Describe what regression is and how it differs from classification.
2. Explain and compare the different types of regression techniques.
3. Implement **Simple Linear Regression** and **Multiple Linear Regression** using Python and Scikit-Learn.
4. Evaluate the performance of a regression model using industry-standard metrics.

---

## 1. What is Regression in Machine Learning?

**Regression** is a type of Supervised Learning technique used to predict a **continuous numerical output** based on one or more input features.

The fundamental question regression answers is: **"How much?"** or **"How many?"**

### Regression vs. Classification — A Critical Distinction

While both are Supervised Learning tasks, they differ in the type of output they predict:

![Regression vs Classification — Key Differences](C:/Users/DELL/.gemini/antigravity-ide/brain/2d7b68e3-902d-47a7-a593-fb0a545cb8eb/regression_vs_classification_1784820921598.png)

| Feature | Regression | Classification |
|---|---|---|
| **Output Type** | Continuous number | Discrete category/class |
| **Examples** | House price, temperature, salary | Spam/Not Spam, Pass/Fail |
| **Key Question** | "How much?" / "How many?" | "Which category?" |
| **Evaluation Metric** | MAE, RMSE, R² Score | Accuracy, F1-Score |
| **Algorithm Example** | Linear Regression | Logistic Regression, SVM |

### Real-World Regression Problems:
- 🏠 **Property Valuation:** Predict house price based on size, location, and age.
- 💼 **Salary Prediction:** Estimate an employee's salary based on years of experience.
- 🌦️ **Weather Forecasting:** Predict tomorrow's temperature from historical weather data.
- ⚡ **Energy Consumption:** Predict a building's electricity usage based on occupancy and size.
- 📦 **Sales Forecasting:** Predict next month's product sales for inventory planning.

---

## 2. Types of Regression Techniques

There are many regression algorithms, each suited to different data patterns and problem types.

![Overview of Regression Technique Types](C:/Users/DELL/.gemini/antigravity-ide/brain/2d7b68e3-902d-47a7-a593-fb0a545cb8eb/types_of_regression_1784820930226.png)

### 2.1 Simple Linear Regression
Predicts the relationship between **one** independent variable (feature `X`) and **one** dependent variable (target `y`) using a straight line.

- **Formula:** `ŷ = β₀ + β₁x`
- **Use when:** You have a single numeric feature and suspect a linear relationship.
- **Example:** Predicting salary from years of experience.

### 2.2 Multiple Linear Regression
An extension of Simple Linear Regression that uses **two or more** independent variables to predict one output.

- **Formula:** `ŷ = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ`
- **Use when:** Multiple factors influence the outcome.
- **Example:** Predicting house price from `size + bedrooms + location + age`.

### 2.3 Polynomial Regression
Fits a **curved (polynomial) line** to the data instead of a straight one. Used when the relationship between X and y is non-linear (e.g., exponential growth).

- **Formula:** `ŷ = β₀ + β₁x + β₂x² + β₃x³ + ...`
- **Use when:** The scatter plot shows a curved relationship.
- **Example:** Predicting COVID-19 case growth, crop yield vs. fertilizer amount.

### 2.4 Ridge Regression (L2 Regularization)
A variant of Linear Regression that adds a **penalty term** to prevent the model from overfitting by keeping the model coefficients small.

- **Use when:** You have many features and the model is overfitting (performing well on training data but poorly on test data).

### 2.5 Lasso Regression (L1 Regularization)
Similar to Ridge, but its penalty term can **shrink some coefficients to exactly zero** — effectively performing automatic feature selection.

- **Use when:** You suspect only a few features are truly important and want the model to eliminate the rest automatically.

### 2.6 Logistic Regression *(covered in Session 16)*
Despite its name, this is a **classification** technique that predicts categorical outcomes (Yes/No). Reviewed here for completeness.

---

## 3. Understanding Model Fit: Underfitting vs. Overfitting

Before implementing regression, it's critical to understand the concept of **model fit** — whether your model is learning the right patterns from data.

![Underfitting vs Good Fit vs Overfitting](C:/Users/DELL/.gemini/antigravity-ide/brain/2d7b68e3-902d-47a7-a593-fb0a545cb8eb/overfitting_underfitting_1784820961058.png)

| Problem | Cause | Training Score | Test Score | Solution |
|---|---|---|---|---|
| **Underfitting** | Model too simple | Low | Low | Use a more complex model |
| **Good Fit** | Balanced complexity | High | High | ✅ This is the goal |
| **Overfitting** | Model too complex | Very High | Low | Use regularization or more data |

---

## 4. Implementing Simple Linear Regression

### The Mathematical Foundation

Simple Linear Regression finds the **Line of Best Fit** — the straight line that minimizes the sum of squared distances between the actual data points and the predicted line.

![Linear Regression Line of Best Fit — Equation, Residuals, Prediction](C:/Users/DELL/.gemini/antigravity-ide/brain/2d7b68e3-902d-47a7-a593-fb0a545cb8eb/linear_regression_best_fit_1784820952388.png)

The equation of the line: **`ŷ = β₀ + β₁x`**

- **ŷ** (y-hat): The predicted output value
- **β₀** (beta-zero): The **intercept** — the predicted value of y when x = 0
- **β₁** (beta-one): The **slope** — how much y changes for each unit increase in x
- **Residual / Error:** The difference between the actual value and the predicted value (`y - ŷ`)

The algorithm finds the values of β₀ and β₁ that minimize the **Sum of Squared Residuals (SSR)** — this technique is called **Ordinary Least Squares (OLS)**.

---

### Step-by-Step Implementation

```python
# =============================================================
# SIMPLE LINEAR REGRESSION — Salary Predictor
# Predicting a Nigerian employee's salary from years of experience
# =============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --- STEP 1: CREATE THE DATASET ---
data = {
    'Years_Experience': [1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2,
                         3.7, 3.9, 4.0, 4.0, 4.1, 4.5, 4.9, 5.1, 5.3,
                         5.9, 6.0, 6.8, 7.1, 7.9, 8.2, 8.7, 9.0, 9.5, 10.3],
    'Salary_Naira':     [390000, 405000, 430000, 480000, 510000, 555000, 580000, 595000, 590000,
                         640000, 650000, 660000, 670000, 680000, 720000, 760000, 790000, 815000,
                         870000, 900000, 980000, 1020000, 1100000, 1140000, 1190000, 1230000, 1290000, 1370000]
}
df = pd.DataFrame(data)

print("Dataset Preview:")
print(df.head())
print(f"\nShape: {df.shape}")

# --- STEP 2: PREPARE FEATURES AND TARGET ---
X = df[['Years_Experience']]   # Must be 2D: double brackets → DataFrame, not Series
y = df['Salary_Naira']

# --- STEP 3: SPLIT DATA ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining samples: {X_train.shape[0]}")
print(f"Testing samples:  {X_test.shape[0]}")

# --- STEP 4: CREATE AND TRAIN THE MODEL ---
model = LinearRegression()
model.fit(X_train, y_train)

print(f"\n✅ Model Trained!")
print(f"  Intercept (β₀): ₦{model.intercept_:,.2f}")
print(f"  Slope (β₁):      ₦{model.coef_[0]:,.2f} per year of experience")
print(f"\n  Equation: Salary = ₦{model.intercept_:,.0f} + {model.coef_[0]:,.0f} × Years_Experience")

# --- STEP 5: MAKE PREDICTIONS ---
y_predicted = model.predict(X_test)

# --- STEP 6: EVALUATE THE MODEL ---
mae  = mean_absolute_error(y_test, y_predicted)
mse  = mean_squared_error(y_test, y_predicted)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_predicted)

print("\n--- Model Evaluation ---")
print(f"  MAE  (Mean Absolute Error):       ₦{mae:,.2f}")
print(f"  RMSE (Root Mean Squared Error):   ₦{rmse:,.2f}")
print(f"  R²   (R-Squared / Accuracy):       {r2:.4f}  ({r2*100:.2f}%)")

# --- STEP 7: VISUALIZE ---
plt.figure(figsize=(10, 6))

# Plot actual data points
plt.scatter(X_train, y_train, color='#3498db', alpha=0.7, s=80, label='Training Data', zorder=3)
plt.scatter(X_test, y_test, color='#e74c3c', alpha=0.9, s=80, marker='D', label='Test Data (Actual)', zorder=3)

# Plot the regression line across the full range
x_line = np.linspace(X['Years_Experience'].min(), X['Years_Experience'].max(), 200).reshape(-1, 1)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, color='#f39c12', linewidth=2.5, label='Regression Line (Prediction)', zorder=2)

# Plot test predictions
plt.scatter(X_test, y_predicted, color='#2ecc71', s=80, marker='^', label='Test Data (Predicted)', zorder=4)

plt.xlabel("Years of Experience", fontsize=13)
plt.ylabel("Salary (₦)", fontsize=13)
plt.title("Simple Linear Regression — Salary vs. Experience", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# --- STEP 8: PREDICT FOR A NEW EMPLOYEE ---
new_employee_years = np.array([[6.5]])
predicted_salary   = model.predict(new_employee_years)[0]
print(f"\n--- New Prediction ---")
print(f"  An employee with 6.5 years of experience:")
print(f"  Predicted Salary → ₦{predicted_salary:,.0f}")
```

---

## 5. Implementing Multiple Linear Regression

When a single feature is not enough, we use **Multiple Linear Regression**. The process is almost identical — Scikit-Learn handles the added complexity internally.

```python
# =============================================================
# MULTIPLE LINEAR REGRESSION — House Price Predictor
# Features: Size (sqm), Bedrooms, Distance to City (km), Age (years)
# =============================================================
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error
import matplotlib.pyplot as plt

np.random.seed(42)
n = 100

df = pd.DataFrame({
    'Size_sqm':         np.random.randint(60, 400, n),
    'Bedrooms':         np.random.randint(1, 6, n),
    'Distance_km':      np.random.uniform(1, 30, n).round(1),
    'Age_years':        np.random.randint(0, 40, n),
})

# Simulate realistic house prices (in millions of Naira)
df['Price_Naira'] = (
    df['Size_sqm']   * 150000   +    # bigger house = more expensive
    df['Bedrooms']   * 800000   +    # more bedrooms = premium
    df['Distance_km']* -120000  +    # farther from city = cheaper
    df['Age_years']  * -80000   +    # older house = cheaper
    np.random.normal(0, 1500000, n)  # random noise
).round(-3)

print("Dataset Preview:")
print(df.head())
print(f"\nShape: {df.shape}")
print(f"Avg House Price: ₦{df['Price_Naira'].mean():,.0f}")

# --- Prepare, Split, Train ---
X = df.drop('Price_Naira', axis=1)
y = df['Price_Naira']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features for better performance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

# --- Evaluate ---
r2  = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"\n✅ Multiple Linear Regression Results:")
print(f"  R² Score: {r2:.4f}  ({r2*100:.2f}% of variance explained)")
print(f"  MAE:      ₦{mae:,.0f}")

# --- Feature Importance (via coefficients) ---
feature_importance = pd.DataFrame({
    'Feature':     X.columns,
    'Coefficient': model.coef_
}).sort_values('Coefficient', key=abs, ascending=False)

print("\n--- Feature Importance (by Coefficient Magnitude) ---")
print(feature_importance.to_string(index=False))

# --- Actual vs Predicted Plot ---
plt.figure(figsize=(8, 6))
plt.scatter(y_test / 1e6, y_pred / 1e6, color='#9b59b6', alpha=0.6, s=60)
plt.plot([y_test.min()/1e6, y_test.max()/1e6],
         [y_test.min()/1e6, y_test.max()/1e6],
         'r--', linewidth=2, label='Perfect Prediction Line')
plt.xlabel("Actual Price (₦ Millions)", fontsize=12)
plt.ylabel("Predicted Price (₦ Millions)", fontsize=12)
plt.title("Multiple Linear Regression — Actual vs Predicted House Prices", fontsize=13)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# --- Predict a New House ---
new_house = pd.DataFrame({
    'Size_sqm':   [200],
    'Bedrooms':   [3],
    'Distance_km':[10.0],
    'Age_years':  [5]
})
new_house_scaled = scaler.transform(new_house)
predicted_price  = model.predict(new_house_scaled)[0]
print(f"\n--- New House Prediction ---")
print(f"  Size: 200 sqm | Bedrooms: 3 | Distance: 10km | Age: 5 years")
print(f"  Predicted Price → ₦{predicted_price:,.0f}")
```

---

## 6. Evaluating Regression Models — Key Metrics

| Metric | Formula | Meaning | Ideal Value |
|---|---|---|---|
| **MAE** (Mean Absolute Error) | avg\|actual - predicted\| | Average error in original units | As low as possible |
| **MSE** (Mean Squared Error) | avg(actual - predicted)² | Penalizes large errors more heavily | As low as possible |
| **RMSE** (Root MSE) | √MSE | Error in same units as target | As low as possible |
| **R² Score** | 1 - (SSR/SST) | % of variance in y explained by model | Closer to 1.0 is better |

### Interpreting R² Score:
```
R² = 0.00  → The model explains NOTHING — as good as just predicting the mean
R² = 0.70  → The model explains 70% of the variance in the data
R² = 0.95  → Excellent — the model captures 95% of the data pattern
R² = 1.00  → Perfect fit (usually means overfitting!)
```

---

## 7. Polynomial Regression — Handling Non-Linear Data

When the relationship between X and y is **curved**, Simple Linear Regression fails. We can use `PolynomialFeatures` from Scikit-Learn to transform our features and then apply Linear Regression on the transformed data.

```python
# =============================================================
# POLYNOMIAL REGRESSION — Crop Yield vs. Fertilizer
# =============================================================
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Simulate: yield increases then decreases with too much fertilizer
np.random.seed(42)
fertilizer = np.linspace(0, 10, 50)
yield_kg   = -3 * (fertilizer - 5)**2 + 80 + np.random.normal(0, 5, 50)

X = fertilizer.reshape(-1, 1)
y = yield_kg

# --- Degree 2 Polynomial Transformation ---
poly        = PolynomialFeatures(degree=2, include_bias=False)
X_poly      = poly.fit_transform(X)

# --- Fit Linear Regression on Polynomial Features ---
model = LinearRegression()
model.fit(X_poly, y)

y_pred_poly = model.predict(X_poly)
r2 = r2_score(y, y_pred_poly)

# --- Visualize ---
plt.figure(figsize=(9, 5))
plt.scatter(fertilizer, yield_kg, color='#3498db', alpha=0.7, s=60, label='Actual Data')

x_smooth      = np.linspace(0, 10, 200).reshape(-1, 1)
x_smooth_poly = poly.transform(x_smooth)
y_smooth_pred = model.predict(x_smooth_poly)
plt.plot(x_smooth, y_smooth_pred, color='#e74c3c', linewidth=2.5, label='Polynomial Regression (Degree 2)')

plt.xlabel("Fertilizer Amount (kg/hectare)", fontsize=12)
plt.ylabel("Crop Yield (kg)", fontsize=12)
plt.title(f"Polynomial Regression — Crop Yield vs. Fertilizer  (R² = {r2:.3f})", fontsize=13)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Polynomial Regression R² Score: {r2:.4f}")
```

---

## 8. Summary — Regression Technique Selection Guide

```
Is the relationship between X and y LINEAR?
    │
    ├─ YES → How many features?
    │           │
    │           ├─ ONE feature    → Simple Linear Regression
    │           └─ MANY features  → Multiple Linear Regression
    │                                 │
    │                               Is the model overfitting?
    │                                 ├─ YES, many features → Ridge or Lasso Regression
    │                                 └─ NO  → Multiple Linear Regression is fine
    │
    └─ NO (curved / non-linear) → Polynomial Regression
```

---

## 🎥 Recommended Watch
- [Linear Regression in Python | Scikit-Learn](https://www.youtube.com/watch?v=NUXdtN1W1FE) — StatQuest with Josh Starmer
- [Multiple Linear Regression | Full Tutorial](https://www.youtube.com/watch?v=EkAQAi3a4js)
- [Polynomial Regression in Python](https://www.youtube.com/watch?v=QptI-vDle8Y)
- [R-Squared Explained Simply](https://www.youtube.com/watch?v=2AQKmw14mHM)
