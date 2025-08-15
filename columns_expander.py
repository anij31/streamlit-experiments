import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like a sidebar
left_column.button('Press me!')

# Call streamlit functions inside with block
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ('Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin')
    )
    st.write(f"You are in {chosen} house!")