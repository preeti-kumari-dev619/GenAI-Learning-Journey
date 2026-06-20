import streamlit as st
st.title("simple sales dashboard")
st.write("This dashboard displays monthly sales data")
month = ["January", "February", "March", "April"]
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}
selected_month = st.selectbox(
    "Select a month:",
    month
)

st.metric(
    label=f"{selected_month} Sales",
    value=sales[selected_month]
)

st.subheader("Monthly Sales Chart")
st.bar_chart(list(sales.values()))