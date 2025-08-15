import streamlit as st

# Create a slider widget
x = st.slider('x')
st.write(x, 'squared is', x * x)
