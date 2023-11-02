import streamlit as st

def __style__(width_percentage):
    button_css="button {" + f"width:{width_percentage}% !important;" + "}"
    html_style_button = f"""
        <style>
        {button_css}
        </style>"""
    st.markdown(html_style_button,unsafe_allow_html=True)   