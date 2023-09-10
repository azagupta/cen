import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def app(census_df):


    st.sidebar.header("Select the Charts/Plots:")
    plot_list = st.sidebar.multiselect("Choose Charts/Plots", ["Count Plot", "Pie Plot", "Box Plot"])

    if "Count Plot" in plot_list:
        st.subheader("Count Plot")
        sns.countplot(data=census_df, x='your_column_name')
        st.pyplot()

    if "Pie Plot" in plot_list:
        st.subheader("Pie Plot")


    if "Box Plot" in plot_list:
        st.subheader("Box Plot")
