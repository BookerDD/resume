import streamlit as st

col1, col2 = st.columns(2, gap='large', vertical_alignment='center')
with col1:
    st.image('./photo/resume.png', width=300)
with col2:
    st.title('Белов Андрей Юрьевич', anchor=False)
    st.text("""
        Телефон: +7(906)-988-88-61
        Телеграмм: @BookerDD
        E-mail: andr123b123@yandex.ru
    """)

st.text("""
    Разрабатывал визуальный образ и проводил исследование для врачей
    Новосибирского кардиологического диспансера, что также являлось моей 
    дипломной работой. Используемые технологии: PyQt6, mathplotlib, pandas
    
    Личные качества: спокойный, трудолюбивый, доброжелательный и отзывчивый
""")