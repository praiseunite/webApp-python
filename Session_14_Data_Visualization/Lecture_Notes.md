# Session 14: Data Visualization in Python 📊

Welcome to Session 14! In our last session, we learned how to manipulate and clean data using Pandas. Today, we bring that data to life by visualizing it.

## 📝 Learning Objectives
By the end of this session, you will be able to:
1. Explain the concept of data visualization.
2. Describe the Python libraries that are used for data visualization.
3. Explain and implement various data visualization techniques available in Python.

---

## 1. The Concept of Data Visualization

**Data Visualization** is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.

### Why is Data Visualization Important?
- **Immediate Understanding:** Human brains process visual information much faster than text or spreadsheets.
- **Identifying Trends and Outliers:** A sudden spike in a line graph or an isolated dot in a scatter plot instantly highlights anomalies or seasonal trends.
- **Storytelling:** Visualizations help communicate findings effectively to non-technical stakeholders.

---

## 2. Python Libraries for Data Visualization

Python has a rich ecosystem of libraries for creating static, animated, and interactive visualizations. The two most commonly used libraries are **Matplotlib** and **Seaborn**.

### A. Matplotlib
**Matplotlib** is the foundational plotting library in Python. It provides low-level control over every aspect of a figure.
- It is highly customizable but can require more code for complex aesthetics.
- The `pyplot` module (typically imported as `plt`) provides a MATLAB-like interface for simple plotting.

**Installation:**
```bash
pip install matplotlib
```

### B. Seaborn
**Seaborn** is a statistical data visualization library built *on top* of Matplotlib.
- It comes with beautiful default themes and color palettes.
- It is highly integrated with **Pandas DataFrames**, making it incredibly easy to plot complex statistical relationships with just one line of code.

**Installation:**
```bash
pip install seaborn
```

---

## 3. Various Data Visualization Techniques in Python

Let's explore the most common types of charts and when to use them.

### Technique 1: Line Plot
- **Purpose:** Best for showing trends over time (e.g., stock prices, temperature changes).
- **Code Example (Matplotlib):**
```python
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temperature = [22, 24, 23, 26, 25]

plt.plot(days, temperature, marker='o', linestyle='-', color='b')
plt.title("Weekly Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.show()
```

### Technique 2: Bar Chart
- **Purpose:** Best for comparing categorical data (e.g., sales by region, population by country).
- **Code Example (Matplotlib):**
```python
categories = ['Apples', 'Bananas', 'Cherries']
quantities = [50, 30, 45]

plt.bar(categories, quantities, color=['red', 'yellow', 'darkred'])
plt.title("Fruit Inventory")
plt.show()
```

### Technique 3: Scatter Plot
- **Purpose:** Best for showing the relationship or correlation between two numerical variables.
- **Code Example (Seaborn):**
```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Using seaborn to easily plot a dataframe
data = pd.DataFrame({
    'Experience (Years)': [1, 2, 3, 4, 5],
    'Salary ($)': [40000, 45000, 52000, 58000, 65000]
})

sns.scatterplot(x='Experience (Years)', y='Salary ($)', data=data, s=100)
plt.title("Experience vs Salary")
plt.show()
```

### Technique 4: Histogram
- **Purpose:** Best for showing the distribution of a single numerical variable (how often certain values occur).
- **Code Example (Matplotlib):**
```python
import numpy as np

# Generate 1000 random heights (normally distributed)
heights = np.random.normal(170, 10, 1000)

plt.hist(heights, bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Heights")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()
```

---

## 🎥 Recommended Watch
- [Matplotlib Tutorial (Part 1): Creating and Customizing Our First Plots](https://www.youtube.com/watch?v=UO98lJQ3QGI) by Corey Schafer
- [Seaborn Tutorial for Beginners](https://www.youtube.com/watch?v=GcXcSZ0gQps)
