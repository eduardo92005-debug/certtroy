import streamlit as st
from streamlit_extras.stylable_container import stylable_container 


def __style__(text):
    with stylable_container(
        key="full_width_button",
        css_styles="""
            button {
                width:100%;
            }
            """,
    ):
        button = st.button(text)
        return button