# Streamlit Assignment 8 - Basic App Building

## Student Information

Name: Your Name

Assignment: Streamlit (Basic App Building)

Technology Used: Python, Streamlit

---

## Project Overview

This project contains 4 beginner-friendly Streamlit applications created to understand the basics of Streamlit components and interactive UI development.

The project focuses on:

- Creating simple Streamlit applications
- Taking user input
- Displaying outputs
- Using buttons, sliders, selectboxes, and sidebars
- Creating simple dashboards
- Building interactive user interfaces

---

## Project Folder Structure

streamlit_assignment/

├── app_basic.py

├── app_discount.py

├── app_product_form.py

├── app_dashboard.py

└── README.md

---

## Task 1: Basic Streamlit App (app_basic.py)

### Features

- Displays title: Welcome to Streamlit
- Takes user's name as input
- Greets the user after clicking a button

### Streamlit Components Used

- st.title()
- st.text_input()
- st.button()
- st.write()

---

## Task 2: Price Calculator (app_discount.py)

### Features

- Takes product price as input
- Takes discount percentage using a slider
- Calculates final discounted price
- Displays result
- Shows Before vs After comparison table

### Streamlit Components Used

- st.title()
- st.number_input()
- st.slider()
- st.button()
- st.success()
- st.table()

---

## Task 3: Product Form (app_product_form.py)

### Features

- Uses sidebar for product input
- Takes product name
- Selects product category
- Takes product price
- Displays product details after clicking Add Product

### Streamlit Components Used

- st.sidebar.text_input()
- st.sidebar.selectbox()
- st.sidebar.number_input()
- st.sidebar.button()
- st.success()
- st.write()

---

## Task 4: Mini Dashboard (app_dashboard.py)

### Features

- Displays a simple sales dashboard
- Selects a month
- Displays monthly sales
- Shows sales bar chart

### Streamlit Components Used

- st.title()
- st.selectbox()
- st.metric()
- st.write()
- st.bar_chart()

---

## How to Run the Project

### Step 1: Open Terminal

Navigate to the project folder.

```bash
cd streamlit_assignment
```

### Step 2: Install Streamlit

```bash
pip install streamlit
```

### Step 3: Run Applications

Run each file separately.

Basic App

```bash
streamlit run app_basic.py
```

Price Calculator

```bash
streamlit run app_discount.py
```

Product Form

```bash
streamlit run app_product_form.py
```

Mini Dashboard

```bash
streamlit run app_dashboard.py
```

---

## Concepts Learned

- Streamlit basics
- User input handling
- Buttons
- Sidebar usage
- Selectbox
- Sliders
- Tables
- Metrics
- Bar charts
- Interactive UI development

---

## Restrictions Followed

- No database used
- No sessions used
- No APIs used
- No file uploaders used
- Beginner-friendly implementation

---

## Author

Preeti Kumari

