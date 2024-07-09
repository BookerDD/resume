import streamlit as st

st.title('Навыки')

col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
with col1:
    st.subheader('Hard Skills')
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
    st.subheader('Soft Skills')
    st.markdown("""
        - Работа в команде
        - Коммуникация
        - Отзывчивость
        - Умение искать информацию
        - Креативность
        - Организационные навыки
        - Спорт
""")




