import streamlit as st

st.title('Навыки')

col1, col2 = st.columns(2, gap='large', vertical_alignment='center')
with col1:
    st.title('Hard Skills')
    st.markdown("""
        - Python
        - PostgreSQL
        - MySQL
        - PyQt6
        - Mathplotlib
        - Git & GitHub
        - Pandas
    """)
with col2:
    st.title('Soft Skills')
    st.markdown("""
        Soft skills
        - Работа в команде
        - Коммуникация
        - Отзывчивость
""")




