import streamlit as st


st.text_input("Your Name: ", key="name")

# Access the value at any point with:
st.session_state.name