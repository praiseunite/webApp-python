# Session 16: Introduction to Different Types of Machine Learning 🤖

Welcome to Session 16! In the previous session, we cleaned and prepared our data using Scikit-Learn preprocessing tools. Now, we put that prepared data to use — by actually building Machine Learning models. In this session, we explore the three major families of ML and implement two of the most important algorithms: **Logistic Regression** and **K-Means Clustering**.

## 📝 Learning Objectives
By the end of this session, you will be able to:
1. Describe the three different types of Machine Learning.
2. Explain and implement **Logistic Regression**, a Supervised Learning algorithm.
3. Describe and implement **K-Means Clustering**, an Unsupervised Learning technique.
4. Explain the concept of **Reinforcement Learning**.

---

## 1. The Three Types of Machine Learning

All Machine Learning algorithms fall into one of three broad categories, depending on the *kind of data* they learn from.

![Types of Machine Learning - Overview Diagram](C:/Users/DELL/.gemini/antigravity-ide/brain/2d7b68e3-902d-47a7-a593-fb0a545cb8eb/ml_types_diagram_1784820036613.png)

| Type | Learning Style | Data Required | Key Question |
|---|---|---|---|
| **Supervised Learning** | Learns from labelled examples | Input + Correct Output | "What is the right answer?" |
| **Unsupervised Learning** | Finds hidden patterns on its own | Input only (no labels) | "What patterns exist?" |
| **Reinforcement Learning** | Learns from trial and error | Agent + Environment + Reward | "What action maximizes my reward?" |

---

## 2. Supervised Learning — Logistic Regression

### What is Supervised Learning?
In **Supervised Learning**, we train a model on a **labelled dataset** — meaning every data point in our training set has a known, correct answer (called a **label** or **target**).

Think of it like a student learning from a marked exam paper. The student sees 100 questions AND the correct answers. Over time, the student learns the underlying rules well enough to answer new, unseen questions correctly.

**Real-World Examples:**
- 📧 **Email Spam Detection:** Training data = thousands of emails, each labelled "Spam" or "Not Spam". The model learns to classify new emails.
- 🏠 **House Price Prediction:** Training data = houses with features (size, location) and their known sale prices. The model learns to predict the price of a new house.
- 🩺 **Medical Diagnosis:** Training data = patient records, each labelled with a diagnosis. The model learns to assist in diagnosing new patients.

---

### Logistic Regression — Binary Classification

Despite having the word "Regression" in its name, **Logistic Regression** is primarily used for **Classification** problems — specifically, predicting one of two outcomes (Binary Classification).

**When to use it:** When your target variable is a **category** with two possible values.
- Will a customer **churn** (Yes/No)?
- Is this email **spam** (Yes/No)?
- Did this patient **survive** (Yes/No)?

### The Sigmoid Function — The Heart of Logistic Regression

Unlike Linear Regression which predicts a continuous number (like price), Logistic Regression uses a special mathematical function called the **Sigmoid Function** (σ) to convert any input value into a **probability between 0 and 1**.

![Logistic Regression Sigmoid Curve & Decision Boundary](C:/Users/DELL/.gemini/antigravity-ide/brain/2d7b68e3-902d-47a7-a593-fb0a545cb8eb/logistic_regression_sigmoid_1784820044927.png)

The sigmoid function formula:
```
σ(z) = 1 / (1 + e^(-z))
```

- If the probability is **> 0.5**, we predict **Class 1** (e.g., "Spam")
- If the probability is **≤ 0.5**, we predict **Class 0** (e.g., "Not Spam")

The **0.5 threshold** is called the **Decision Boundary**.

---

### Implementing Logistic Regression with Scikit-Learn

The process for any Scikit-Learn model follows the same workflow:
1. **Prepare the data** (split into Train and Test sets)
2. **Instantiate** the model
3. **Train** the model (`.fit()`)
4. **Evaluate** the model (`.score()` or `.predict()`)

```python
# =============================================================
# LOGISTIC REGRESSION — Student Exam Pass/Fail Predictor
# =============================================================
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# --- 1. CREATE SAMPLE DATA ---
# Feature: Number of hours a student studied
# Target: 1 = Passed, 0 = Failed
hours_studied = np.array([1, 2, 2.5, 3, 4, 4.5, 5, 6, 6.5, 7, 8, 9]).reshape(-1, 1)
passed =        np.array([0, 0,   0, 0, 0,   1, 1, 1,   1, 1, 1, 1])

# --- 2. SPLIT DATA into Training (80%) and Testing (20%) sets ---
X_train, X_test, y_train, y_test = train_test_split(
    hours_studied, passed, test_size=0.2, random_state=42
)

# --- 3. INSTANTIATE the model ---
model = LogisticRegression()

# --- 4. TRAIN the model ---
model.fit(X_train, y_train)

# --- 5. PREDICT on the test set ---
y_predicted = model.predict(X_test)
print(f"Predicted results for test set: {y_predicted}")
print(f"Actual results for test set:    {y_test}")

# --- 6. EVALUATE the model's performance ---
accuracy = accuracy_score(y_test, y_predicted)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# --- 7. MAKE A NEW PREDICTION ---
# If a student studies for 3.5 hours, will they pass?
new_student_hours = np.array([[3.5]])
prediction = model.predict(new_student_hours)
probability = model.predict_proba(new_student_hours)

print(f"\n--- New Prediction ---")
print(f"Hours Studied: 3.5")
print(f"Pass (1) or Fail (0)? --> {prediction[0]}")
print(f"Probability of passing: {probability[0][1]*100:.1f}%")
```

### Understanding the Train/Test Split

A crucial concept in ML is that we **never** test a model on the same data it was trained on. That would be like giving a student the exact same exam they used to study — they would achieve 100% but learn nothing useful.

```
Full Dataset (100%)
        |
  ------+------
  |            |
80% Train    20% Test
(model       (model is
 learns)      evaluated)
```

---

## 3. Unsupervised Learning — K-Means Clustering

### What is Unsupervised Learning?
In **Unsupervised Learning**, we give the algorithm data **without any labels**. The algorithm must discover hidden patterns, groupings, or structure in the data entirely on its own.

Think of it like a librarian who has received thousands of unsorted books. Without being told the categories, the librarian groups similar books together: all the science books, all the romance novels, all the history books. This is exactly what clustering algorithms do.

**Real-World Examples:**
- 🛒 **Customer Segmentation:** Group customers by buying behavior (e.g., budget shoppers, brand loyalists, impulse buyers) without pre-defining the groups.
- 📰 **News Article Grouping:** Automatically group news articles about the same topic (sports, politics, technology).
- 🧬 **Gene Expression Analysis:** Find groups of genes with similar expression patterns.

---

### K-Means Clustering — How It Works

**K-Means** is the most popular clustering algorithm. The **K** stands for the number of clusters you want the algorithm to find. You must decide `K` before running the algorithm.

![K-Means Clustering Step-by-Step](C:/Users/DELL/.gemini/antigravity-ide/brain/2d7b68e3-902d-47a7-a593-fb0a545cb8eb/kmeans_clustering_steps_1784820068765.png)

**The 4-Step Algorithm:**

| Step | Action |
|---|---|
| **1. Initialize** | Randomly place K "centroids" (cluster center points) in the data space |
| **2. Assign** | Assign each data point to the nearest centroid (based on distance) |
| **3. Update** | Move each centroid to the *mean position* of all points assigned to it |
| **4. Repeat** | Repeat steps 2 & 3 until the centroids stop moving (convergence) |

---

### Implementing K-Means Clustering with Scikit-Learn

```python
# =============================================================
# K-MEANS CLUSTERING — Customer Segmentation Example
# =============================================================
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# --- 1. CREATE SAMPLE DATA ---
# Each row is a customer: [Annual Spending (RM), Visit Frequency (times/month)]
np.random.seed(42)

# Simulating 3 customer types
budget_shoppers  = np.random.normal(loc=[500, 5], scale=[100, 1], size=(30, 2))
regular_shoppers = np.random.normal(loc=[2000, 15], scale=[200, 2], size=(30, 2))
premium_shoppers = np.random.normal(loc=[5000, 25], scale=[300, 3], size=(30, 2))

# Combine all customers into one unlabelled dataset
X = np.vstack([budget_shoppers, regular_shoppers, premium_shoppers])

print(f"Total customers in dataset: {X.shape[0]}")
print("Note: We do NOT give the model the labels! It must find the groups itself.\n")

# --- 2. SCALE THE DATA ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- 3. APPLY K-MEANS CLUSTERING (K=3 clusters) ---
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)

# --- 4. GET RESULTS ---
labels = kmeans.labels_          # Which cluster each customer belongs to (0, 1, or 2)
centers = kmeans.cluster_centers_ # The final centroid positions

print(f"Cluster labels assigned to each customer:")
print(labels)
print(f"\nNumber of customers in each cluster:")
for i in range(3):
    count = np.sum(labels == i)
    print(f"  Cluster {i}: {count} customers")

# --- 5. VISUALIZE THE RESULTS ---
colors = ['#e74c3c', '#2ecc71', '#3498db']
cluster_names = ['Cluster A', 'Cluster B', 'Cluster C']

plt.figure(figsize=(10, 6))
for i in range(3):
    cluster_points = X[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1],
                c=colors[i], label=cluster_names[i], alpha=0.7, s=80)

plt.xlabel("Annual Spending (RM)")
plt.ylabel("Visit Frequency (times/month)")
plt.title("K-Means Customer Segmentation (K=3)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nInsight: The model discovered 3 distinct customer groups without any labels!")
```

### Choosing the Right K — The Elbow Method

A common challenge with K-Means is deciding the best value of **K** (number of clusters). The **Elbow Method** helps with this by plotting the **inertia** (sum of squared distances from each point to its nearest centroid) for different values of K.

```python
# --- THE ELBOW METHOD ---
inertia_values = []
K_range = range(1, 8)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertia_values.append(km.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia_values, marker='o', color='#9b59b6', linewidth=2, markersize=8)
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia (Sum of Squared Distances)")
plt.title("The Elbow Method — Finding the Optimal K")
plt.xticks(K_range)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
# Look for the "elbow" — the point where inertia stops dropping sharply.
# That K value is typically the best choice!
```

---

## 4. Reinforcement Learning

### What is Reinforcement Learning?

**Reinforcement Learning (RL)** is the third and most distinct type of Machine Learning. Unlike Supervised or Unsupervised Learning, RL does not learn from a pre-existing dataset. Instead, an **agent** learns by **interacting with an environment** through trial and error.

The agent takes actions, and the environment responds with:
1. A new **state** (observation of what the environment looks like now)
2. A **reward** signal (+ve for good actions, -ve for bad actions)

The agent's goal is to learn a **policy** — a strategy for choosing actions — that **maximises its total reward over time**.

![Reinforcement Learning Loop — Agent, Environment, State, Reward, Action](C:/Users/DELL/.gemini/antigravity-ide/brain/2d7b68e3-902d-47a7-a593-fb0a545cb8eb/reinforcement_learning_loop_1784820077504.png)

---

### Key Components of Reinforcement Learning

| Component | Definition | Game Example (Pac-Man) |
|---|---|---|
| **Agent** | The learner / decision maker | Pac-Man character |
| **Environment** | The world the agent operates in | The game board / maze |
| **State** | The current situation the agent observes | Current position, ghost positions |
| **Action** | A decision made by the agent | Move Up / Down / Left / Right |
| **Reward** | Feedback from the environment | +10 (ate a dot), -100 (caught by ghost) |
| **Policy** | The strategy the agent learns | "If ghost is near, run away" |

---

### Real-World Applications of RL

- 🎮 **Game AI:** DeepMind's AlphaGo (beat the world champion at Go), OpenAI's Dota 2 agent, and game bots that play Atari games at superhuman levels.
- 🚗 **Self-Driving Cars:** The car (agent) learns to navigate roads safely by receiving rewards for staying in its lane and penalties for collisions.
- 🤖 **Robotics:** Teaching a robot arm to grasp objects of different shapes by trial and error.
- 💹 **Algorithmic Trading:** An agent learns trading strategies that maximise profit while minimising risk.
- 🏥 **Healthcare:** Optimising treatment plans for patients (e.g., the best sequence of drug dosages).

---

### A Simple RL Concept in Python

While full RL requires specialized libraries (like `gymnasium` or `stable-baselines3`), we can demonstrate the **core idea** of a reward-based update loop with a simple example:

```python
# =============================================================
# REINFORCEMENT LEARNING — Conceptual Demo (Reward Loop)
# A simple coin-flip agent that learns which action is better
# =============================================================
import numpy as np

# The agent has 2 possible "actions": Action 0 and Action 1.
# Action 0 gives an average reward of 1.0 (worse)
# Action 1 gives an average reward of 2.5 (better) — unknown to the agent!

np.random.seed(42)
action_rewards = {0: 1.0, 1: 2.5}   # True reward for each action (agent doesn't know this)
num_episodes   = 1000
epsilon        = 0.1                  # Exploration rate: 10% of the time, try random action

# Agent's current estimate of reward for each action (starts at 0)
estimated_rewards = np.zeros(2)
action_counts     = np.zeros(2)

total_reward = 0
print("Starting RL training loop...\n")

for episode in range(1, num_episodes + 1):
    # --- EPSILON-GREEDY POLICY ---
    # Most of the time: choose the action with the best estimated reward (exploit)
    # Sometimes: choose a random action to discover something new (explore)
    if np.random.random() < epsilon:
        chosen_action = np.random.randint(0, 2)  # Explore
    else:
        chosen_action = np.argmax(estimated_rewards)  # Exploit

    # --- RECEIVE REWARD FROM ENVIRONMENT ---
    actual_reward = np.random.normal(loc=action_rewards[chosen_action], scale=0.5)
    total_reward += actual_reward

    # --- UPDATE ESTIMATE ---
    action_counts[chosen_action] += 1
    # Incremental average update
    estimated_rewards[chosen_action] += (actual_reward - estimated_rewards[chosen_action]) / action_counts[chosen_action]

# --- RESULTS ---
print(f"Training complete after {num_episodes} episodes.")
print(f"Total reward accumulated:          {total_reward:.2f}")
print(f"Agent's estimated reward (Action 0): {estimated_rewards[0]:.2f} (True: 1.0)")
print(f"Agent's estimated reward (Action 1): {estimated_rewards[1]:.2f} (True: 2.5)")
print(f"Agent correctly learned that Action {np.argmax(estimated_rewards)} is better! ✅")
```

---

## 5. Summary — Quick Comparison

| Feature | Supervised | Unsupervised | Reinforcement |
|---|---|---|---|
| **Labelled Data** | ✅ Required | ❌ Not used | ❌ Not used |
| **Goal** | Predict labels | Find structure | Maximize reward |
| **Python Algorithms** | `LogisticRegression`, `DecisionTree`, `SVM` | `KMeans`, `DBSCAN`, `PCA` | Q-Learning, PPO, DQN |
| **Key Libraries** | `scikit-learn` | `scikit-learn` | `gymnasium`, `stable-baselines3` |
| **Real Example** | Spam Detection | Customer Groups | AlphaGo, Self-Driving |

---

## 🎥 Recommended Watch
- [Supervised vs Unsupervised vs Reinforcement Learning](https://www.youtube.com/watch?v=1FZ0A1QCMWc)
- [Logistic Regression in Python | Scikit-Learn](https://www.youtube.com/watch?v=HYcXgN9HaTM)
- [K-Means Clustering — How it Works](https://www.youtube.com/watch?v=4b5d3muPQmA)
- [Reinforcement Learning — An Introduction (Simple)](https://www.youtube.com/watch?v=JgvyzIkgxF0)
