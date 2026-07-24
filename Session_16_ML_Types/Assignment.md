# Assignment: Customer Segmentation with K-Means Clustering 🛒

## Objective
Use **K-Means Clustering** to segment customers of a Nigerian e-commerce platform into distinct groups based on their purchasing behavior, enabling targeted marketing campaigns.

## Background
"ShopNaija" is an e-commerce platform that wants to move from sending the **same promotional email to all customers** to a **targeted strategy** where different customer segments receive different offers:
- 💎 **Premium Customers** → Luxury item recommendations
- 🔄 **Regular Customers** → Loyalty rewards & discounts
- 💸 **Budget Customers** → Flash sale alerts

Your job is to build a K-Means model that can automatically discover and label these segments.

## Dataset
You are provided with `customer_data.csv` (or you will create it from the starter file). It contains the following columns:

| Column | Description |
|---|---|
| `CustomerID` | Unique customer identifier |
| `Annual_Spend_Naira` | Total amount spent in Naira in the last 12 months |
| `Monthly_Orders` | Average number of orders placed per month |
| `Avg_Order_Value` | Average value of a single order (Naira) |
| `Returns_Rate` | Percentage of orders returned (0.0 to 1.0) |

## Requirements

### Part 1: Explore & Prepare the Data
1. Load the CSV using Pandas.
2. Print the first 5 rows, shape, and descriptive statistics (`.describe()`).
3. Check for and handle any missing values.
4. **Scale the features** using `StandardScaler`. *Note: Drop `CustomerID` before scaling — it is not a feature!*

### Part 2: Find the Optimal K (Elbow Method)
1. Loop through K values from 1 to 8.
2. Fit a KMeans model for each K and record the **inertia** (`.inertia_`).
3. Plot the Elbow Curve.
4. In a comment, state what you believe the optimal K is and why.

### Part 3: Apply K-Means with Optimal K
1. Fit the final KMeans model using the K you selected from the Elbow Method.
2. Add the cluster labels as a new column `Segment` to the **original (unscaled)** DataFrame.

### Part 4: Analyze & Name the Segments
1. Group the DataFrame by `Segment` and calculate the **mean** of each feature for each cluster.
2. Print this summary table.
3. Based on the averages, identify which cluster corresponds to which customer type (Premium, Regular, Budget) and print your interpretation.

### Part 5: Visualize the Segments
1. Create a **scatter plot** with `Annual_Spend_Naira` on the X-axis and `Monthly_Orders` on the Y-axis.
2. Color each point by its `Segment` label.
3. Add a proper title, axis labels, and a legend.

---

## Deliverables
- Completed `assignment_solution.py`
- The Elbow Curve plot
- The final Scatter Plot showing the 3 customer segments

## Instructions
1. Open `assignment_starter.py`.
2. Implement all 5 parts described above.
3. Your final summary table should clearly show the differences between clusters.
