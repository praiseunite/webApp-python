# Class Task: Build Your First Logistic Regression Classifier 🎓

## Objective
Apply the Logistic Regression workflow covered in today's lecture on a new dataset to predict whether a bank customer will **default on a loan**.

## Scenario
You are a data scientist at a Nigerian bank. The bank wants to predict, based on a customer's financial profile, whether they are likely to default on a loan payment. This is a **binary classification** problem:
- **Target = 1:** Customer will **default** (High Risk)
- **Target = 0:** Customer will **not default** (Low Risk)

## Instructions
1. Open `class_task_starter.py`.
2. A dataset of bank customer records has been provided as a dictionary.
3. Follow the steps in the starter file to build and evaluate a Logistic Regression model.

## Steps to Complete

### Step 1: Load the Data
- Create a Pandas DataFrame from the provided dictionary.
- Separate the data into features `X` (all columns EXCEPT `Defaulted`) and target `y` (`Defaulted` column).

### Step 2: Split the Data
- Use `train_test_split` to split the data into **80% training** and **20% testing** sets.
- Set `random_state=42` to ensure reproducible results.

### Step 3: Train the Model
- Import `LogisticRegression` from `sklearn.linear_model`.
- Instantiate the model and call `.fit()` on the training data.

### Step 4: Evaluate the Model
- Use `.predict()` on the test data.
- Print the **accuracy score** using `accuracy_score` from `sklearn.metrics`.
- Print the full **classification report** using `classification_report`.

### Step 5: Make a Prediction
- Predict whether a **new customer** will default given:
  - `Age=35`, `Income=85000`, `Loan_Amount=200000`, `Credit_Score=680`, `Months_Employed=48`
- Print whether the customer is **High Risk** or **Low Risk**.

---
> **Expected Output:** Your model should achieve an accuracy of approximately **80-90%**. The final prediction should print "High Risk" or "Low Risk" for the new customer.
