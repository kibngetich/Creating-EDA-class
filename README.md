# OOP Plotting Class with Matplotlib in Python

This repository showcases a custom `Plot` class built using **Object-Oriented Programming (OOP)** principles in Python. It wraps around `matplotlib.pyplot` to provide a flexible and reusable interface for creating various plots.

## Purpose

This project was created as part of my journey to solidify my understanding of OOP in Python, specifically:

-  Class design and structure
-  Method encapsulation
-  Parameter customization and defaults
-  Reusability and abstraction

## Features

The `Plot` class supports the following types of plots:

-  Histogram
-  Line Plot
-  Scatter Plot
-  Bar Plot

Each method provides common customization options like figure size, color, labels, titles, grid toggling, saving the plot, and more.

---

## Sample Usage

```python
from kev_
plot import Plot

plotter = Plot()

# Example: Line Plot
x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 18, 20]

plotter.line(x, y, title="Example Line Plot", color='green')


