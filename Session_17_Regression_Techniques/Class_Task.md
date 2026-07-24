# Class Task: Simple Linear Regression — Student Score Predictor 📚

## Objective
Build a Simple Linear Regression model to predict a student's **exam score** based on the **number of hours they studied**. Then visualize the result and make a new prediction.

## Scenario
You are a teaching assistant at Aptech. You have collected data from 20 students in the previous cohort, showing how many hours they studied and their final exam score (out of 100). You want to build a model that can predict a new student's score based on how many hours they plan to study.

## Instructions
1. Open `class_task_starter.py`.
2. A dataset has already been provided for you as lists.
3. Complete the TODOs to build, evaluate, and visualize a Linear Regression model.

---

## Steps to Complete

### Step 1: Prepare the Data
- Convert the lists to a Pandas DataFrame.
- Separate into features `X` (hours studied — must be a **2D array**) and target `y` (exam scores).

### Step 2: Split the Data
- Use `train_test_split` with `test_size=0.25` and `random_state=0`.

### Step 3: Train the Model
- Instantiate `LinearRegression()` and train it on the training data.
- Print the **intercept** and **slope (coefficient)** of the line.
- Write out the full equation: `Score = β₀ + β₁ × Hours_Studied`

### Step 4: Evaluate the Model
- Predict on the test set.
- Calculate and print the **R² Score** and **MAE**.

### Step 5: Visualize
- Create a scatter plot of ALL data points (training data in blue, test data in red).
- Draw the **regression line** in orange across the full X range.
- Add proper title, axis labels, and a legend.

### Step 6: New Prediction
- Predict the exam score for a student who studies for **7.5 hours**.
- Print the result in a clear sentence.

---

> **Tip:** Remember that `X` must be a **2D array** for Scikit-Learn. Use `df[['Hours_Studied']]` (double brackets) or `.reshape(-1, 1)` on a NumPy array.
