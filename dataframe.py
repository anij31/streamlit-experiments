import streamlit as st
import pandas as pd

# Create a sample dataframe from python dictionary
df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

st.write("Attempt to create a pandas dataframe")
st.write(df)