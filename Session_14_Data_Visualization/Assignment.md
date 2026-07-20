# Assignment: Weather Dashboard 🌤️📉

## Objective
Combine your Pandas knowledge with Data Visualization to analyze and plot a weather dataset. You will create a dashboard-like image with multiple subplots using both Matplotlib and Seaborn.

## Dataset Setup
A file named `weather_data.csv` is provided in the session folder. It contains 30 days of weather data with the following columns:
- `Day`: Day of the month (1-30)
- `Temperature`: Average daily temperature in Celsius
- `Humidity`: Average daily humidity percentage
- `WindSpeed`: Average wind speed in km/h
- `Condition`: A categorical description (Sunny, Cloudy, Rainy)

## Requirements

### 1. Load the Data
- Use Pandas to read `weather_data.csv` into a DataFrame.

### 2. Create a Subplot Figure
- Create a Matplotlib Figure with 2 rows and 2 columns of subplots (a 2x2 grid). 
- Set the overall figure size to something large, like `(12, 10)`.
- Give the entire figure a main title: "Monthly Weather Analysis".

### 3. Populate the Subplots

**Top-Left Subplot: Temperature Trend**
- Plot `Day` vs. `Temperature` as a **Line Plot**.
- Add a title ("Temperature over 30 Days"), x-label, and y-label.

**Top-Right Subplot: Humidity vs. Wind Speed**
- Create a **Scatter Plot** showing the relationship between `Humidity` and `WindSpeed`.
- *(Optional challenge: Use Seaborn's `scatterplot` and color the dots based on the `Condition` column!)*

**Bottom-Left Subplot: Weather Conditions Breakdown**
- Count how many days were Sunny, Cloudy, or Rainy. *(Hint: Use Pandas `.value_counts()`)*
- Plot these counts as a **Bar Chart**.
- Add appropriate labels and title.

**Bottom-Right Subplot: Temperature Distribution**
- Create a **Histogram** of the `Temperature` column to show its distribution.
- Use `bins=10`. Add an edge color for clarity.

### 4. Display
- Call `plt.tight_layout()` to prevent labels from overlapping.
- Finally, use `plt.show()` to display the dashboard.

---

## Instructions
1. Open `assignment_starter.py`.
2. Implement the requirements described above.
3. Run the script and admire your custom Data Visualization dashboard!
