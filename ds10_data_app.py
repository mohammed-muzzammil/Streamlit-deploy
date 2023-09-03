import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# Title
st.markdown("<h1 style='text-align: center; color: black;'>Data Pre Processing</h1>", unsafe_allow_html=True)

# Define the connection parameters
host = "localhost"
user = "root"
password = "my-secret-pw"
database = "test"

# Create a connection object
connection = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")


# Data Import
def data_import():
    with st.sidebar:
        st.title("Data Import")
        file_options = ["csv", "xlsx"]
        file_type = st.radio("Select file type", file_options)
        if file_type == "csv":
            file = st.file_uploader("Upload a csv file", type="csv")
            if file:
                df = pd.read_csv(file)
                st.session_state["df"] = df

        elif file_type == "xlsx":
            file = st.file_uploader("Upload a excel file", type="xlsx")
            if file:
                df = pd.read_excel(file)
                st.session_state["df"] = df


# Missing Value Treatment
def missing_value_treatment():
    st.sidebar.title("Missing Value Treatment")
    choice = st.sidebar.radio("Select missing value treatment", ["None", "Mean", "Median", "Mode"])
    if choice == "Mean":
        if st.sidebar.button("Treat using Mean"):
            treat_using_mean()
    elif choice == "Median":
        if st.sidebar.button("Treat using Median"):
            treat_using_median()
    elif choice == "Mode":
        if st.sidebar.button("Treat using Mode"):
            treat_using_mode()


def treat_using_mean():
    df = st.session_state["df"]
    df = df.fillna(df.mean())
    st.dataframe(df)
    st.session_state["df"] = df


def treat_using_median():
    df = st.session_state["df"]
    df = df.fillna(df.median())
    st.dataframe(df)
    st.session_state["df"] = df


def treat_using_mode():
    df = st.session_state["df"]
    df = df.fillna(df.mode())
    st.dataframe(df)
    st.session_state["df"] = df


# Outlier Treatment
def outlier_treatment():
    st.sidebar.title("Outlier Treatment")
    df = st.session_state["df"]
    choice = st.sidebar.radio("Select outlier treatment", ["None", "IQR", "Z-Score"])
    if choice == "IQR":
        column_name = st.sidebar.selectbox("Select column name", df.columns)
        if st.sidebar.button("Treat using IQR"):
            treat_using_iqr(column_name)


def treat_using_iqr(column_name):
    df = st.session_state["df"]
    q1 = df[column_name].quantile(0.25)
    q3 = df[column_name].quantile(0.75)
    IQR = q3 - q1
    lower_limit = q1 - 1.5 * IQR
    upper_limit = q3 + 1.5 * IQR
    new_df = df[(df[column_name] > lower_limit) & (df[column_name] < upper_limit)]
    st.session_state["df"] = new_df
    st.dataframe(new_df)


# Data Export
def data_export():
    st.sidebar.title("Data Export")
    df = st.session_state["df"]
    choice = st.sidebar.radio("Select data export", ["None", "CSV", "MYSQL"])
    if choice == "CSV":
        st.sidebar.download_button(
            label="Download data as CSV",
            data=df.to_csv(index=False),
            file_name="data.csv",
            mime="text/csv",
        )
    elif choice == "MYSQL":
        df.to_sql("test_table_2", con=connection, if_exists="replace", index=False)
        st.write("Data exported to MYSQL")


def main():
    data_import()
    missing_value_treatment()
    outlier_treatment()
    data_export()


main()
