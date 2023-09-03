# Streamlit application to demo a simple banking functionality.

import streamlit as st

# Title
st.title("Banking App")

user_dict = {
    "user1": "password1",
    "user2": "password2",
}

balances = {
    "user1": 1000,
    "user2": 500
}

# Login
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username in user_dict.keys():
        if password == user_dict[username]:
            st.write("Login Successful")
            st.session_state["Login"] = True
            st.session_state["username"] = username
        else:
            st.write("Incorrect Password")
    else:
        st.write("Username not found")

if "Login" in st.session_state and st.session_state["Login"] == True:
    st.write("Welcome {}".format(st.session_state["username"]))

    # Selectbox
    option = st.sidebar.selectbox("What would you like to do?", ["None", "Check Balance", "Deposit", "Withdraw"])

    if option == "Check Balance":
        st.write("Your balance is {}".format(balances[st.session_state["username"]]))

    elif option == "Deposit":
        amount = st.number_input("Enter the amount to deposit")

        if st.button("Deposit"):

            balances[st.session_state["username"]] = balances[st.session_state["username"]] + amount
            st.write("Your balance is {}".format(balances[username]))

    elif option == "Withdraw":

        amount = st.number_input("Enter the amount to withdraw")

        if st.button("Withdraw"):

            if amount > balances[st.session_state["username"]]:
                st.write("Insufficient Balance")
            else:

                balances[st.session_state["username"]] = balances[st.session_state["username"]] - amount
                st.write("Your balance is {}".format(balances[st.session_state["username"]]))
