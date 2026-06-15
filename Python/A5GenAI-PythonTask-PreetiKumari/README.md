# Assignment 5 - Importing, Creating Modules & Packages (Python)

## Objective

This assignment focuses on understanding Python Modules and Packages.

The goal is to learn how to:

- Create Python modules (.py files)
- Import modules
- Create packages using `__init__.py`
- Import functions from modules and packages
- Organize code in a structured folder

---

## Project Structure

```text
modules_assignment/

│── main.py
│── math_utils.py
│── string_utils.py

└── shop_package/
    │── __init__.py
    │── discount.py
    └── billing.py
```

---

## Tasks Completed

### Task 1: Create a Module (math_utils.py)

Functions:

- `add(a, b)` → Returns addition
- `subtract(a, b)` → Returns subtraction
- `square(n)` → Returns square of a number

---

### Task 2: Create Another Module (string_utils.py)

Functions:

- `capitalize_words(text)` → Capitalizes each word
- `reverse_string(text)` → Reverses a string
- `word_count(text)` → Counts total words

---

### Task 3: Create a Package (shop_package)

### discount.py

Functions:

- `apply_discount(price, percent)`
- `flat_discount(price)`

### billing.py

Functions:

- `calculate_total(prices)`
- `apply_tax(amount)`

### __init__.py

Imports functions from package modules.

---

### Task 4: Import the Package in main.py

Imported and tested:

- Package modules
- Package functions
- Billing functions
- Discount functions

---

## Concepts Learned

- Python Modules
- Import Statements
- Python Packages
- __init__.py
- Code Organization

---

## Technologies Used

- Python 3

---

## Assignment Purpose

This assignment was created to build a strong foundation in Python modules and packages before moving to advanced Python concepts.