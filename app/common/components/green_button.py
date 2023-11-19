import streamlit as st
from streamlit_extras.stylable_container import stylable_container 


def __style__(text):
    with stylable_container(
        key="green_button",
        css_styles="""
            button {
                background-color: green;
                color: white;
                border-radius: 20px;
                width:100%;
            }
            """,
    ):
        start_button = st.button(text)
        return start_button