import streamlit as st
from streamlit_extras.stylable_container import stylable_container 


def __style__(text):
    with stylable_container(
        key="new_button",
        css_styles="""
            button {
                background-color: #dc3545;
                color: white;
                width:100%;
            }
            """,
    ):
        return st.form_submit_button(text)