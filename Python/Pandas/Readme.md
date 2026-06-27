# Assignment 10: Pandas (Series, DataFrame, Functions, Filtering & Analysis)

## Overview

This assignment covers core Pandas operations using sales and student performance data in tabular form. All tasks are implemented in a single Python file / Jupyter Notebook.

**Scope:** Pandas Series, DataFrames, filtering, groupby, and built-in plotting.  
**No advanced EDA, ML, or complex visualizations.**

---

## Requirements

- Python 3.x
- pandas
- matplotlib (for plotting tasks)

Install dependencies:

```bash
pip install pandas matplotlib
```

---

## Restrictions

- Use **Pandas only** (NumPy allowed indirectly)
- **Avoid loops** where Pandas operations are possible
- Keep graphs **simple and readable**
- Use only `DataFrame.plot()` and `Series.plot()` — no matplotlib customization

---

## Tasks Summary

### Task 1 — Pandas Series Basics
- Create a Series from `marks = [78, 85, 90, 66, 72]`
- Print: values, index, dtype
- Access: first element, last two elements

### Task 2 — Mathematical Operations on Series
- Add 5 grace marks
- Subtract 2 from all values
- Multiply all marks by 1.05
- Divide all marks by 2

### Task 3 — Python Functionalities on Series
- Find: max, min, sum, mean
- Apply a lambda to check pass/fail (>= 70)
- Count how many students passed

### Task 4 — Create a DataFrame
- Build a `students` DataFrame with columns: `Name`, `Marks`, `Subject`
- Print: first 3 rows, last 2 rows, shape, column names

### Task 5 — Important DataFrame Functions
- Use `.info()`, `.describe()`, `.head()`, `.tail()`
- Sort by Marks descending
- Reset index after sorting

### Task 6 — Filtering & Conditional Selection
- Students who scored > 75
- Students in Math subject
- Students above average marks
- Students who failed (< 70)

### Task 7 — Grouping & Basic Analysis
- Average marks per subject
- Count of students per subject
- Maximum marks per subject

### Task 8 — Pandas Plotting
- Bar graph: student names vs marks
- Line graph: marks
- Histogram: marks distribution

### Task 9 — Mini Use Case: Sales Data Analysis
- DataFrame: `Day` vs `Revenue`
- Total revenue, average daily revenue
- Day with highest revenue
- Days above average revenue
- Plot: revenue vs day

---

## Dataset

### Students DataFrame

| Name  | Marks | Subject |
|-------|-------|---------|
| Amit  | 78    | Math    |
| Neha  | 85    | Math    |
| Rahul | 90    | Science |
| Sneha | 66    | Science |
| Pooja | 72    | Math    |

### Sales DataFrame

| Day | Revenue |
|-----|---------|
| Mon | 1200    |
| Tue | 1500    |
| Wed | 900     |
| Thu | 2000    |
| Fri | 1800    |

---

## Key Notes

- All operations return **new Series/DataFrames** — they do not modify in place unless reassigned.
- Use `iloc` over direct indexing to avoid issues after filtering.
- Always use `reset_index(drop=True)` after filtering/sorting if the result is used downstream.
- For counting, prefer `(series >= value).sum()` over `.apply(lambda...)` where possible.
- In Jupyter, plots render inline automatically — no `savefig()` needed.

---

## File Structure

```
assignment10/
│
├── assignment10.ipynb   # Main notebook with all tasks
└── README.md            # This file
```