import streamlit as st

st.set_page_config(
    page_title="Project Portfolio",
    page_icon=":dog:", # 🐶
    layout="wide",
)

# Introduction:
with open("intro.txt", encoding="utf-8") as file:
    intro = file.read()

_, avatar_col, intro_col, _ = st.columns([1, 1, 2, 1])

with avatar_col:
    st.container(height=3, border=False)
    st.image("avatar.jpg")

with intro_col:
    with st.container(height=270, border=False):
        st.header("Benz")
        st.info(intro)

# Project Showcase:
project_cols = st.columns(3)

with project_cols[0]:
    with st.container(border=True):
        st.header("Chatbot")
        st.write("Description here")

with project_cols[1]:
    with st.container(border=True):
        st.header("Project 2")
        st.write("Description here")

with project_cols[2]:
    with st.container(border=True):
        st.header("Project 3")
        st.write("Description here")