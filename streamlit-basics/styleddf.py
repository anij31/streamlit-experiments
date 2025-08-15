import streamlit as st
import pandas as pd
import numpy as np

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=[f"col {i}" for i in range(20)]
)

st.dataframe(dataframe)