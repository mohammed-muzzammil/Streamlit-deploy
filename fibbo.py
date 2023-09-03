# Streamlit application to take user input a number and display the Fibonacci series up to that number.
import streamlit as st

# Title
st.title("Fibonacci Series")

# Number Input
number = st.number_input("Enter a number", min_value=0, max_value=1000, value=0)

# Button
button = st.button("Generate Fibonacci Series")

if button:
    a = 0
    b = 1
    st.write(a)
    st.write(b)
    for i in range(number-2):
        c = a + b
        st.write(c)
        a = b
        b = c