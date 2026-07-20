# Session 12: Data Handling Using Pandas 🐼

Welcome to Session 12! In this session, we transition into Data Science by learning about the most powerful data manipulation library in Python: **Pandas**. 

## 📝 Learning Objectives
By the end of this session, you will be able to:
1. Describe the purpose and importance of Pandas in Python.
2. Differentiate and explain the two main data structures provided by Pandas: **Series** and **DataFrame**.
3. Use commonly used Pandas data manipulation functions (loading data, cleaning data, filtering).
4. Apply text processing functions to Pandas columns.

---

## 1. What is the Purpose of Pandas?

**Pandas** is an open-source Python library built on top of NumPy. It provides high-performance, easy-to-use data structures and data analysis tools. 
Its main purposes include:
- **Data Cleaning:** Handling missing data (NaN values) and fixing formatting issues.
- **Data Transformation:** Merging, reshaping, and pivoting datasets.
- **Data Analysis:** Grouping data, calculating statistics (mean, median, max), and filtering rows based on conditions.
- **File I/O:** Easily reading and writing data to various formats like CSV, Excel, SQL, and JSON.

**Installation:**
```bash
pip install pandas
```

---

## 2. The Two Main Data Structures in Pandas

Pandas provides two primary structures to handle data:

### A. Series
A **Series** is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, Python objects, etc.). Think of it as a single column in an Excel spreadsheet.

```python
import pandas as pd

# Creating a Series from a list
ages = pd.Series([25, 30, 22, 28], name="Age")
print(ages)
```

### B. DataFrame
A **DataFrame** is a two-dimensional, size-mutable, tabular data structure with labeled axes (rows and columns). It is essentially a dictionary of Series objects. Think of it as an entire Excel spreadsheet or SQL table.

```python
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 22, 28],
    "City": ["New York", "London", "Paris", "Tokyo"]
}
df = pd.DataFrame(data)
print(df)
```

---

## 3. Commonly Used Data Manipulation Functions

The most common way to work with DataFrames is by importing data from a file, such as a CSV.

### Reading and Inspecting Data
- `pd.read_csv("filename.csv")`: Loads data from a CSV file into a DataFrame.
- `df.head(n)`: Returns the first `n` rows (default is 5).
- `df.tail(n)`: Returns the last `n` rows.
- `df.info()`: Prints a concise summary of the DataFrame (column names, data types, non-null counts).
- `df.describe()`: Generates descriptive statistics (mean, std, min, max) for numerical columns.

```python
df = pd.read_csv("sales_data.csv")
print(df.head())
print(df.info())
```

### Data Cleaning and Filtering
- **Handling Missing Values:**
  - `df.dropna()`: Removes rows with missing values (NaN).
  - `df.fillna(value)`: Fills missing values with a specified value.
- **Filtering Rows:**
  - `df[df['Age'] > 25]`: Returns rows where Age is greater than 25.
  - `df[(df['Age'] > 25) & (df['City'] == 'London')]`: Multiple conditions.

---

## 4. Text Processing Functions in Pandas

Pandas provides a set of string processing methods under the `.str` accessor. These are incredibly useful for cleaning up text data.

- `df['Name'].str.lower()`: Converts all strings in the column to lowercase.
- `df['Name'].str.upper()`: Converts all strings in the column to uppercase.
- `df['City'].str.contains("New")`: Returns a boolean Series showing whether "New" is in the string.
- `df['Name'].str.replace("a", "@")`: Replaces occurrences of a substring.
- `df['Name'].str.strip()`: Removes leading and trailing whitespace.

### Example:
```python
# Convert all city names to uppercase
df['City'] = df['City'].str.upper()

# Filter names that start with 'A'
a_names = df[df['Name'].str.startswith('A')]
```

---

## 🎥 Recommended Watch
- [Pandas Data Science Tutorial in 10 Minutes](https://www.youtube.com/watch?v=zmdjNSmRXF4)
- [Python Pandas Tutorial (Part 1): Getting Started with Data Analysis](https://www.youtube.com/watch?v=ZyhVh-qRZPA) by Corey Schafer
