import streamlit as st

about_page = st.Page(
    page='views/about_me.py',
    title='Обо мне',
    default=True
)

education_page = st.Page(
    page='views/education.py',
    title='Образование'
)

skills_page = st.Page(
    page='views/skills.py',
    title='Навыки'
)

langs_page = st.Page(
    page='views/langs.py',
    title='Языки'
)

position_page = st.Page(
    page='views/desired_pos.py',
    title='Желаемая должность'
)

pg = st.navigation(
    {
        'Основная информация': [about_page],
        'Дополнительная информация': [education_page, skills_page, langs_page, position_page]
    }
)

pg.run()


