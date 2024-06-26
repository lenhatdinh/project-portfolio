import streamlit as st

st.set_page_config(
    page_title="Project Portfolio",
    page_icon=":dog:", # 🐶
    layout="wide",
)

# Introduction:
with open("intro.txt", encoding="utf-8") as file:
    intro = file.read()

_, avatar_col, intro_col, _ = st.columns([1, 1, 1.5, 1])

with avatar_col:
    st.container(height=1, border=False)
    st.image("avatar.jpg")

with intro_col:
    st.header("Benz")
    st.container(height=220, border=False).info(intro)

# Project Showcase:
project_cols = st.columns(3)

with project_cols[0].container(border=True):
    st.header("[Chatbot](https://github.com/lenhatdinh/chatbot)")
    st.write("Description here")

with project_cols[1].container(border=True):
    st.header("Project 2")
    st.write("Description here")

with project_cols[2].container(border=True):
    st.header("Project 3")
    st.write("Description here")