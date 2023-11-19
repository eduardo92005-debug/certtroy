import streamlit as st
from streamlit_extras.stylable_container import stylable_container 


def __style__(text):
    with stylable_container(
        key="confirm_button",
        css_styles="""
            button {
                background-color: #007BFF;
                color: white;
                width:100%;
            }
            """,
    ):
        return st.button(text)