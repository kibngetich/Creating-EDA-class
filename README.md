# OOP Plotting Class with Matplotlib and Seaborn in Python

This repository showcases a custom `Plot` class built using **Object-Oriented Programming (OOP)** principles in Python. It wraps around `matplotlib.pyplot` and `seaborn` to provide a flexible and reusable interface for creating a variety of plots.

## Purpose

This project was created as part of my journey to solidify my understanding of OOP in Python, specifically:

- Class design and structure
- Method encapsulation
- Parameter customization and defaults
- Reusability and abstraction
- Integration with visualization libraries (Matplotlib and Seaborn)

## Features

The `Plot` class supports the following types of plots:

- **Histogram**
- **Line Plot**
- **Scatter Plot**
- **Bar Plot**
- **Box Plot**
- **Violin Plot**
- **Heatmap**
- **Pair Plot**
- **Count Plot**

Each method provides common customization options such as figure size, colors, labels, titles, grid toggling, saving the plot to file, and more. Seaborn-powered methods offer additional styling and advanced visualizations.

---

## Tools Used

- **Python 3.11.7** — Core programming language
- **Matplotlib** — Primary library for static plotting
- **Seaborn** — High-level API for statistical plots
- **Pandas** — Data manipulation and analysis

---

## Sample Usage

```python
from kev_plot import Plot

plotter = Plot()

# Example: Line Plot
x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 18, 20]
plotter.line(x, y, title="Example Line Plot", color='green')

# Example: Box Plot
import pandas as pd
df = pd.DataFrame({
    'gender': ['Male', 'Female', 'Female', 'Male'],
    'income': [50000, 60000, 62000, 58000]
})
plotter.boxplot(data=df, x='gender', y='income', title="Income by Gender")

# Example: Heatmap
import numpy as np
data = np.random.rand(5, 5)
plotter.heatmap(data=data, title="Sample Heatmap")





