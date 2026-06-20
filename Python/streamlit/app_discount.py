import streamlit as st
st.title("Price Calculator")
price = st.number_input("Enter Product Price", min_value=0)
discount = st.slider(
    "select discount percentage",
    min_value=0,
    max_value=50,
    value=10
)

if st.button("Calculate Price"):
    discount_amount = (price * discount) / 100
    final_price = price - discount_amount
    st.success(f"Final Price: {final_price:.2f}")

    table_data = [
        ["Before", price],
        ["After", final_price]
    ]
    st.write("###price comparison")
    st.table(table_data)