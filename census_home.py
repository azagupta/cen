# S5.1: Configure the home as directed above.
import streamlit as st

pages_dict = {
             "Home": census_home,
             "Visualise Data": census_plots
         }


st.sidebar.title('Navigation')
user_choice = st.sidebar.radio("Go to", tuple(pages_dict.keys()))
if user_choice == "Home":
    home.app() # The 'app()' function should not take any input if the selection option is "Home".
else:
    selected_page = pages_dict[user_choice]
    selected_page.app(census_home)
	