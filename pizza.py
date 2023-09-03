# Streamlit application to take the pizza order from the user and display the total amount.

import streamlit as st
import pandas as pd


# Title
st.title("Pizza Ordering App")

pizza_dict = {
    "Onion Pizza": 100,
    "Capsicum Pizza": 150,
    "Paneer Pizza": 200,
    "Chicken Pizza": 250,
    "Margherita Pizza": 300,
    "Toppings": 50,
}

# Text Input for Name
name = st.text_input("Enter your name")
number = st.text_input("Enter your number")
address = st.text_input("Enter your address")

# Distance from the restaurant
slider = st.slider("Distance from the restaurant in KM", min_value=0, max_value=10)

if slider > 5:
    st.write("Sorry, we do not deliver beyond 5 KM")

else:
    # Multi-Selectbox for food items
    food_items = st.multiselect("Select your food items", pizza_dict.keys())

    # Button
    button = st.button("Place Order")
    if button:
        total = 0
        for item in food_items:
            total = total + pizza_dict[item]

        st.write("Your order has been placed and the total amount is {}".format(total))



