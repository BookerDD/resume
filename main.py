import streamlit as st

about_page = st.Page(
    page='views/about_me.py',
    title='Обо мне',
    icon=':material/person:',
    default=True
)
education_page = st.Page(
    page='views/education.py',
    title='Образование',
    icon=':material/school:'
)

skills_page = st.Page(
    page='views/skills.py',
    title='Навыки',
    icon=':material/person_play:'
)

langs_page = st.Page(
    page='views/langs.py',
    title='Языки',
    icon=':material/translate:'
)

position_page = st.Page(
    page='views/desired_pos.py',
    title='Желаемая должность',
    icon=':material/person_search:'
)

pg = st.navigation(
    {
        'Основная информация': [about_page],
        'Дополнительная информация': [education_page, skills_page, langs_page, position_page]
    }
)

pg.run()


