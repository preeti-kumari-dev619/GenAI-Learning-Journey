import streamlit as st
st.title("Product Form")
st.write("Enter product details from the sidebar.")
product_name = st.sidebar.text_input("Product Name")
category = st.sidebar.selectbox(
    "category",
    ["Electronics", "Clothing", "Books", "Home", "Sports"]
)

price = st.sidebar.number_input(
    "price",
    min_value=0.0,
    step=1.0

)

if st.sidebar.button("Add Product"):
    st.success("Product added successfully")
    st.write("### products Details")
    st.write(f"Product Name: {product_name}")
    st.write(f"Category: {category}")
    st.write(f"Price: {price}")

