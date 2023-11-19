import streamlit as st
from app.common import template 
from app.utils import helper
from app.common.components import green_button
from streamlit_extras.switch_page_button import switch_page

def __section__():
    helper.set_actual_section("Seção 2", "Sobre o equipamento")

@template.common_components
def render():
    defaut_inputs = {
        "local_instalacao": ("Local de instalacao", st.text_input),
        "padrao_manun": ("Padrao manutencao", st.text_input)
    }
    helper.batch_create_io(defaut_inputs)
    bt_confirm = green_button.__style__("Confirmar")
    if bt_confirm:
        switch_page("Operações")
__section__()
render()