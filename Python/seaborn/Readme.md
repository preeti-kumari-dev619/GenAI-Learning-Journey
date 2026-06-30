# Assignment 12: Seaborn (Relational, Distribution, Categorical & Multi-Plots)

## Student Information

**Name:** Preeti Kumari  
**Course:** Data Analytics / Python Visualization  
**Assignment:** Assignment 12 - Seaborn Visualization  
**Dataset:** Titanic Dataset (Kaggle)

---

# Objective

The objective of this assignment is to perform Exploratory Data Analysis (EDA) using the Seaborn library. The assignment demonstrates different types of Seaborn visualizations to understand relationships, distributions, categorical comparisons, regression analysis, matrix plots, and figure-level plots.

---

# Dataset Information

**Dataset Name:** Titanic Dataset

**Source:** Kaggle

Dataset Link:
https://www.kaggle.com/datasets/yasserh/titanic-dataset

---

# Technologies Used

- Python 3.x
- Pandas
- Seaborn
- Matplotlib

---

# Required Libraries

Install the required libraries using pip:

```bash
pip install pandas
pip install matplotlib
pip install seaborn
```

or

```bash
pip install pandas matplotlib seaborn
```

---

# Import Libraries

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

---

# Dataset Loading

```python
df = pd.read_csv("Titanic-Dataset.csv")
```

---

# Tasks Completed

## Task 1: Relational Plot

- Created Relational Plot using `sns.relplot()`
- Numerical vs Numerical visualization
- Used categorical column as `hue`
- Scatter style visualization

---

## Task 2: Line Plot & Faceting

- Created Line Plot using `sns.lineplot()`
- Scatter-style line plot
- Used Faceting with categorical columns

---

## Task 3: Distribution Plots

Created:

- Histogram
- KDE Plot
- Rug Plot
- Histogram + KDE

---

## Task 4: Bivariate Distribution Plots

Created:

- Bivariate Histogram
- Bivariate KDE Plot

---

## Task 5: Matrix Plots

Created:

- Pair Plot
- Correlation Matrix
- Heatmap

---

## Task 6: Categorical Plots

Created:

- Bar Plot
- Box Plot
- Violin Plot
- Count Plot

---

## Task 7: Regression Plot

Created:

- Regression Plot using `sns.regplot()`

---

## Task 8: Multi-Plots & Figure-Level Plots

Created:

- FacetGrid
- relplot()
- catplot()
- displot()

---

# Numerical Columns Used

- Age
- Fare
- PassengerId
- Pclass
- Survived

---

# Categorical Columns Used

- Sex
- Embarked
- Pclass
- Survived

---

# Learning Outcomes

After completing this assignment, I learned:

- How to create relational plots using Seaborn.
- How to analyze numerical data using distribution plots.
- How to compare categories using categorical plots.
- How to identify relationships using regression plots.
- How to visualize correlations using heatmaps.
- How to use PairPlot for multiple numerical variables.
- How to create figure-level plots such as relplot, catplot, displot, and FacetGrid.
- How to perform basic Exploratory Data Analysis (EDA) using Seaborn.

---

# Folder Structure

```
GenAI-Task12-PreetiKumari/
│
├── README.md
├── Titanic-Dataset.csv
├── Task1_RelationalPlot.ipynb
├── Task2_LinePlot.ipynb
├── Task3_DistributionPlots.ipynb
├── Task4_BivariatePlots.ipynb
├── Task5_MatrixPlots.ipynb
├── Task6_CategoricalPlots.ipynb
├── Task7_RegressionPlots.ipynb
├── Task8_MultiPlots.ipynb
```

*(If you completed all tasks in a single notebook, replace the multiple notebook names with your notebook filename, for example `Assignment12_Seaborn.ipynb`.)*

---

# Conclusion

This assignment demonstrates the use of Seaborn for Exploratory Data Analysis (EDA). Different visualization techniques were applied to the Titanic dataset to explore relationships, distributions, categorical comparisons, regression trends, matrix visualizations, and figure-level plots. These visualizations help in understanding the dataset more effectively and support data-driven decision-making.

---

## Thank You