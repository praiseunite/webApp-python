# Session 18: Try It Yourself — Review of Book Sessions 12–15 🔁

Welcome to **Session 18**! This is a hands-on review session that consolidates everything you have learned across four major book chapters. No new theory today — it is all about **applying your skills** through realistic, integrated exercises.

![Session 18 Review Roadmap — Pandas, Visualization, ML Types, Regression](C:/Users/DELL/.gemini/antigravity-ide/brain/2d7b68e3-902d-47a7-a593-fb0a545cb8eb/session18_review_roadmap_1784822240003.png)

---

## 📋 Quick Concept Recap

Before diving into the exercises, use this table as a rapid reference:

| Book Session | Topic | Key Skills |
|---|---|---|
| **Session 12** | Pandas Data Handling | Series, DataFrame, `read_csv`, `dropna`, `fillna`, `groupby`, `.str` accessor |
| **Session 13** | Data Visualization | Matplotlib (`plt.plot`, `bar`, `hist`, `scatter`), Seaborn (`sns.heatmap`, `boxplot`) |
| **Session 14** | ML Types | Supervised (Logistic Regression), Unsupervised (K-Means), Reinforcement Learning |
| **Session 15** | Regression Techniques | Simple & Multiple Linear Regression, `train_test_split`, MAE, RMSE, R² Score |

---

## 🎯 Session Structure

This session has **three parts**:

| Part | Activity | Time |
|---|---|---|
| **Part 1** | Choose Your Main Project (A, B, or C) | ~60 mins |
| **Part 2** | Integrated Mini-Challenge | ~20 mins |
| **Part 3** | Debugging Challenge (Everyone) | ~15 mins |

---

## Part 1: Choose Your Main Project

Pick **ONE** of the following three projects. Each integrates multiple skills from the reviewed sessions.

---

### 🅰️ Option A — The Student Analytics Dashboard (Pandas + Visualization)

**Scenario:** The Academic Department at Aptech has given you a CSV file (`student_data.csv`) of student records. The data is messy. Your job is to clean it, analyze it, and produce a set of professional charts for the Head of Department's report.

**File:** Work in `review_starter.py` → Section A

**Tasks:**

#### A1. Data Cleaning (Book Session 12)
1. Load `student_data.csv` into a Pandas DataFrame.
2. Print the shape and first 5 rows. Identify all quality issues.
3. Fix all of the following:
   - Standardize all names to **Title Case** (fix `bob smith`, `CHARLIE BROWN`, etc.)
   - Strip extra **whitespace** from the `City` column.
   - Drop rows with **missing `Score_ML`** values.
   - Fill missing **`Score_Pandas`** values with the **median** of that column.
   - Remove the row where **`Age` is negative** (invalid data).
4. Print the cleaned DataFrame's shape. How many rows were removed?

#### A2. Analysis (Book Session 12)
5. Using `groupby`, calculate the **mean score for each subject** (Pandas, Visualization, ML, Regression) for **each Course**.
6. Find the **top 3 students** by total score across all 4 subjects.
7. What percentage of students are from **Lagos**?

#### A3. Visualization (Book Session 13)
8. **Bar Chart:** Average score per Course in the `Score_ML` column.
9. **Histogram:** Distribution of `Score_Regression` scores (bins=8).
10. **Box Plot (Seaborn):** Distribution of `Score_Pandas` per `Gender`.
11. Give each chart a proper title, axis labels, and professional styling.

---

### 🅱️ Option B — The Exam Predictor (ML + Regression)

**Scenario:** Using the cleaned student data, build two Machine Learning models: one to **predict exam scores** (regression) and one to **classify scholarship eligibility** (classification). Compare their performance.

**File:** Work in `review_starter.py` → Section B

**Tasks:**

#### B1. Data Preparation (Book Sessions 12 & 15)
1. Load and clean `student_data.csv` (same cleaning steps as Option A).
2. Encode the `Course` column using `pd.get_dummies()`.
3. Encode the `Gender` column (M=0, F=1) using `LabelEncoder`.
4. Drop non-numeric columns (`StudentID`, `Name`, `City`, `Scholarship`).

#### B2. Regression Model — Predict `Score_Regression` (Book Session 15)
5. Set `Score_Regression` as the target `y`. All other score columns + encoded features as `X`.
6. Split: 80/20 train/test, `random_state=42`.
7. Train a `LinearRegression` model.
8. Print **MAE**, **RMSE**, and **R²** on the test set.
9. Plot **Actual vs Predicted** scores (scatter plot + perfect prediction line).

#### B3. Classification Model — Predict `Scholarship` (Book Session 14)
10. Set `Scholarship` (Yes=1, No=0) as the new target `y`. Use the same `X`.
11. Train a `LogisticRegression` model (same 80/20 split).
12. Print the **accuracy** and **classification report**.
13. Predict: Would a student with average scores across all subjects receive a scholarship?

---

### 🅲 Option C — The K-Means Student Grouper (Unsupervised ML)

**Scenario:** The academic counsellors want to group students into **performance tiers** without being told the categories — so they can design targeted support programmes. Apply K-Means clustering.

**File:** Work in `review_starter.py` → Section C

**Tasks:**

#### C1. Prepare the Data (Book Session 12)
1. Load and clean `student_data.csv`.
2. Select only the four score columns as features: `Score_Pandas`, `Score_Visualization`, `Score_ML`, `Score_Regression`.
3. Scale the features with `StandardScaler`.

#### C2. Find the Optimal K (Book Session 14)
4. Run the **Elbow Method** for K=1 to 7. Plot the curve.
5. In a comment, justify your chosen K.

#### C3. Apply K-Means and Analyse (Book Session 14)
6. Fit the final KMeans model. Add cluster labels to the DataFrame as `Tier`.
7. Print a summary table: mean score per `Tier`.
8. Name each tier (e.g., "High Achiever", "Average Performer", "Needs Support") based on the means.

#### C4. Visualize (Book Session 13)
9. Scatter plot: `Score_Pandas` vs `Score_ML`, colored by `Tier`.
10. Bar chart: Average total score per `Tier`.

---

## Part 2: Integrated Mini-Challenge ⚡

**Do this regardless of which main project you chose.**

Using only the **clean** dataset (no missing values, valid ages), answer the following by writing Python code:

```
Q1. What is the correlation between Score_Pandas and Score_Regression?
    Hint: df[['Score_Pandas', 'Score_Regression']].corr()

Q2. Which city has the highest average Score_ML?

Q3. If Score_ML >= 75 means "Competent in ML", what percentage of 
    Data Science students are "Competent in ML"?

Q4. Create a single figure with 2 subplots side-by-side:
    - Left:  Bar chart of student count per City
    - Right: Pie chart of student distribution per Course
```

Write your answers in the `Part 2` section of `review_starter.py`.

---

## Part 3: Debugging Challenge 🐛

*Everyone must complete this section.*

The code below is from a student who tried to build a complete ML pipeline. It has **6 bugs**. Find and fix them all in `debug_challenge.py`.

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegresion
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("student_data.csv")

# Step 1: Drop missing values
df = df.dropna(subset=['Score_Pandas', 'Score_ML'])

# Step 2: Prepare features and target
X = df[['Score_Pandas', 'Score_Visualization', 'Score_ML']]
y = df['Score_Regression']

# Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 4: Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.fit_transform(X_test)   # BUG

# Step 5: Train model
model = LinearRegresion()   # BUG
model.fit(X_train_scaled, y_train)

# Step 6: Predict and evaluate
y_pred = model.predict(X_test)   # BUG

r2  = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"R² Score: {r2}")
print(f"MAE: {mae}")

# Step 7: Predict for a new student with scores [80, 75, 85]
new_student = [80, 75, 85]   # BUG — wrong shape for sklearn
prediction = model.predict(new_student)
print(f"Predicted Regression Score: {prediction}")
```

### Bug Hints
<details>
<summary>Hint 1</summary>
Check the import statement for LinearRegression — is it spelled correctly?
</details>
<details>
<summary>Hint 2</summary>
When scaling test data, should you use `fit_transform()` or just `transform()`? Why does it matter?
</details>
<details>
<summary>Hint 3</summary>
The model was trained on `X_train_scaled`. What data should you be predicting on?
</details>
<details>
<summary>Hint 4</summary>
Scikit-Learn expects a **2D array** for prediction. How do you reshape `[80, 75, 85]`?
</details>
<details>
<summary>Hint 5 (Bonus)</summary>
The `train_test_split` has no `random_state`. This isn't a crash bug, but it means results differ every run. What value should you add for reproducibility?
</details>

### Answers to Debug Challenge
<details>
<summary>Click to reveal all 6 bugs and fixes</summary>

1. **`LinearRegresion`** → **`LinearRegression`** (typo — missing 's')
2. **`scaler.fit_transform(X_test)`** → **`scaler.transform(X_test)`** (must NOT re-fit scaler on test data — this leaks test statistics into training)
3. **`model.predict(X_test)`** → **`model.predict(X_test_scaled)`** (model expects scaled data — same format as training)
4. **`new_student = [80, 75, 85]`** → **`new_student = np.array([[80, 75, 85]])`** (sklearn requires 2D array — double brackets)
5. **`train_test_split(X, y, test_size=0.2)`** → add **`random_state=42`** for reproducibility
6. **(Bonus)** The `from sklearn.linear_model import LinearRegresion` line itself has the typo — fixing both the import AND the instantiation is needed.

</details>

---

*If you get stuck, reference the lecture notes from Sessions 12–17, or peek at `review_solution.py` for guidance!*
