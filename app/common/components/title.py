import streamlit as st
from app.utils import helper
def __render__():
    st.markdown("<h1 style='text-align: center;'>CERTTROY</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>{helper.get_actual_section()} - {helper.get_actual_section_description()}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>Gerador de Certificado de Calibracao</h3>", unsafe_allow_html=True)