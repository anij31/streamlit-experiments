import pandas as pd
import streamlit as st

# create a sample dataframe
df = pd.DataFrame({
    "first_column": [1, 2, 3, 4],
    "second_column": [10, 20, 30, 40]
})

# create a static table
st.table(df)

