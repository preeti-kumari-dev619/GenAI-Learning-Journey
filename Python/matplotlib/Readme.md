# Assignment 11: Matplotlib (Core Plot Types & Visualization)

## Overview
This assignment demonstrates the use of core Matplotlib plotting functions to visualize real-world data from the Superstore dataset (Kaggle).

## Dataset
- **Source:** [Superstore Dataset - Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **File:** `Sample - Superstore.csv`
- **Encoding:** `latin-1`

## Requirements
- Python 3.x
- pandas
- matplotlib
- numpy

Install dependencies:
```bash
pip install pandas matplotlib numpy
```

## Restrictions
- Only `matplotlib.pyplot` used for plotting
- No Seaborn
- No `DataFrame.plot()` shortcuts

---

## Tasks

### Task 1 — Line Plot (`task1_line_plot.py`)
- Groups sales by month using `Order Date`
- Plots monthly sales trend over time
- Axes: Month (x), Sales (y)

### Task 2 — Scatter Plot (`task2_scatter_plot.py`)
- Plots relationship between `Sales` and `Profit`
- Reveals profit distribution across different sale sizes

### Task 3 — Bar Plot (`task3_bar_plot.py`)
- Vertical bar chart: Sales by Category
- Horizontal bar chart: Same data, flipped axes
- Category column used: `Furniture`, `Office Supplies`, `Technology`

### Task 4 — Multiple Bar Plot (`task4_multiple_bar.py`)
- Compares Sales by Category across different years (2014–2017)
- Side-by-side bars using `np.arange` and `bar width=0.2`
- Includes legend, title, and axis labels

### Task 5 — Stacked Bar Chart (`task5_stacked_bar.py`)
- Stacks Category sales per year using `bottom` parameter
- Each category layer starts where the previous one ended
- Includes legend, title, and axis labels

### Task 6 — Histogram (`task6_histogram.py`)
- Shows distribution of `Sales` column
- `bins=20` chosen to capture right-skewed distribution
- Axes: Sales (x), Frequency (y)

### Task 7 — Pie Chart (`task7_pie_chart.py`)
- Shows each Category's share of total Sales
- `autopct="%1.1f%%"` displays percentage inside each slice
- Categories: Furniture, Office Supplies, Technology

---

## How to Run
Place all `.py` files in the same folder as `Sample - Superstore.csv`, then run:
```bash
python task1_line_plot.py
python task2_scatter_plot.py
python task3_bar_plot.py
python task4_multiple_bar.py
python task5_stacked_bar.py
python task6_histogram.py
python task7_pie_chart.py
```