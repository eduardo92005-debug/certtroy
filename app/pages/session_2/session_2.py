import streamlit as st
from ...utils import helper
from ...common import template

@template.common_components
def render():
    helper.set_actual_section("Seção 1")
    st.title("Formulário de Calibração")
    st.title("Sessao 2")
