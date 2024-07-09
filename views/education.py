import streamlit as st

st.title('Образование')

col1, col2 = st.columns([1, 6])

with col1:
    st.write('\n')
    st.write('\n')
    st.image('./photo/nstu.png', width=80)
with col2:
    st.subheader('Бакалавр - 2024')
    st.write(
        'Новосибирский государственный технический университет, Новосибирск\n'
        'Факультет автоматики и вычислительной техники\n'
        '09.03.04 “Программная инженерия”'
    )
