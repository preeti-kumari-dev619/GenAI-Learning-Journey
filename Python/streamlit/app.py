import streamlit as st
st.title("welcome to streamlit!")
name = st.text_input("Enter your Name:")
if st.button("Greet me"):
    if name:
        st.write(f"hello, {name}!")
    else:
        st.write(f"please Enter your name:")