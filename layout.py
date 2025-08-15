import streamlit as st

# Add a selection box to the sidebar
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home Phone', 'Mobile Phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'select a range of values',
    0.0, 100.0, (25.0, 75.0)
)