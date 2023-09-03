import streamlit as st
import pandas as pd

with st.sidebar:
    st.title("Login")
    st.text_input("Username")
    
login = st.button("Login")
if login:
    st.session_state["login"] = True

if "login" in st.session_state and st.session_state["login"] == True:

    # Title
    st.title("A Simple Application")

    # Text Input
    name = st.text_input("Enter your name")

    # Displaying Text
    st.write(name)

    # Number Input
    age = st.number_input("Enter your age", min_value=18, max_value=100)

    # Radio Button
    status = st.radio("What is your status", ["None", "Married", "Unmarried"])
    st.write(status)

    # Selectbox
    occupation = st.selectbox("What is your occupation", ["None", "Student", "Teacher", "Doctor"])

    # Multi-Selectbox
    occupations = st.multiselect("What are your occupations", ["None", "Student", "Teacher", "Doctor"])


    # Checkbox
    ocu = st.checkbox("Are you a student?")

    # Slider
    age = st.slider("How old are you?", min_value=0, max_value=1000)

    # Button
    button = st.button("Click me")
    if button == True:
        st.session_state["button"] = True

    if "button" in st.session_state:
        st.write("You clicked the button")

    # Date Input
    date = st.date_input("When is your birthday?")

    # File Upload
    file = st.file_uploader("Upload your file", type=["csv", "xlsx"])
    if file:
        if file.type == "text/csv":
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)


# Download Button
st.download_button(
    label="Download data as CSV",
    data=file,
    file_name="helllo.csv",
    mime="text/csv",
)







