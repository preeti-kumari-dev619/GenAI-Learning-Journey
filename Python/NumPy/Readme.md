# Assignment 9: NumPy (Mathematical & Statistical Operations)

## Problem Statement
You are working as a Data Analyst trainee. Your task is to use NumPy to perform basic mathematical computations, array operations, and statistical analysis on numerical data. This assignment focuses on understanding important formulas, mathematical operations, and statistical functions provided by NumPy.

This assignment covers only:
- Creating NumPy arrays
- Mathematical operations
- Important NumPy formulas
- Statistical operations (mean, median, variance, standard deviation, etc.)

## Restrictions
- Use only NumPy (no pandas, no matplotlib).
- Avoid loops where NumPy vectorized operations are possible.
- Keep the code clean and beginner-friendly.
- This assignment builds strong numerical foundations for the upcoming Pandas, ML, and Data Science modules.

## Requirements
- Python 3.8 or higher
- NumPy library

## Setup

1. Check Python is installed:
   ```bash
   python3 --version
   ```

2. Install NumPy (skip if already installed):
   ```bash
   pip install numpy
   ```

## Project Structure
```
assignment9/
├── task1.py   # Task 1: Creating NumPy Arrays
├── task2.py   # Task 2: Important Mathematical Operations (+, -, *, /, **)
├── task2b.py  # Task 2 (alt): Same operations using np.add(), np.subtract(), etc.
├── task3.py   # Task 3: Important NumPy Mathematical Formulas (sqrt, exp, log, sum, cumsum)
├── task4.py   # Task 4: Aggregation Operations (row/column sum, min, max, mean)
├── task5.py   # Task 5: Statistical Operations (mean, median, variance, std, range)
├── task6.py   # Task 6: Percentiles & Sorting
├── task7.py   # Task 7: Mini Use Case - Sales Analysis
└── README.md
```

## Task Breakdown

**Task 1 – Creating NumPy Arrays**
Create a 1D array (1–10), a 2D array of shape (3,3), and an array from a list. Print shape and dtype of each.

**Task 2 – Important Mathematical Operations**
Given `A = [10,20,30,40]` and `B = [1,2,3,4]`, compute addition, subtraction, multiplication, division, and power — first with operators, then with `np.add()`, `np.subtract()`, `np.multiply()`, `np.divide()`, `np.power()`.

**Task 3 – Important NumPy Mathematical Formulas**
Given `values = [2,4,6,8,10]`, compute square root, exponential, natural log, sum, and cumulative sum.

**Task 4 – Aggregation Operations**
Given a 3x3 2D array, compute row-wise sum, column-wise sum, minimum, maximum, and overall mean.

**Task 5 – Statistical Operations (Core Focus)**
Given `marks = [78,85,90,66,72,88,95,60]`, compute mean, median, variance, standard deviation, min/max, and range.

**Task 6 – Percentiles & Sorting**
Sort the marks array, find the 25th/50th/75th percentiles, and count how many students scored above the average.

**Task 7 – Mini Use Case: Sales Analysis**
Given a week of daily sales, compute total weekly sales, average daily sales, highest/lowest sales day, standard deviation, and identify days above average.

## How to Run

Each task is an independent script. Run any file directly with Python:

```bash
python3 task1.py
python3 task2.py
python3 task2b.py
python3 task3.py
python3 task4.py
python3 task5.py
python3 task6.py
python3 task7.py
```

On Windows, use `python` instead of `python3` if `python3` is not recognized:
```bash
python task1.py
```

## Notes
- All scripts use only NumPy — no loops were used where vectorized operations were possible, per the assignment restrictions.
- `np.var()` and `np.std()` use population formulas (divide by N) by default. Use `ddof=1` if sample statistics are required instead.
- Array dtype (`int32` vs `int64`) may differ by platform (Windows defaults to `int32`, Linux/Mac to `int64`) — expected NumPy behavior, not an error.
- Day numbers in `task7.py` are converted to 1-indexed (Day 1–7) for readability; NumPy itself is 0-indexed internally.

## Troubleshooting
| Issue | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'numpy'` | Run `pip install numpy` |
| `python3: command not found` | Use `python` instead, or install Python 3 |
| Output differs slightly in dtype (`int32` vs `int64`) | Platform-dependent default, not a bug |