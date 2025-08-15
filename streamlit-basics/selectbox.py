import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

option = st.selectbox(
    'which number do you like the best?',
    df['first_column']
)

'You selected: ', option