import streamlit as st
from app.common import template 
from app.utils import helper

def __section__():
    helper.set_actual_section("Secao 1", "Dados do executante")

@template.common_components
def render():
    defaut_inputs = {
        "data_calibracao": ("Data de Calibração", st.date_input),
        "ordem": ("Ordem", st.text_input),
        "validade": ("Validade", st.date_input),
        "tipo_calibracao": ("Tipo de calibracao",st.text_input),
        "num_lote": ("Numero de lote de controle",st.text_input),
        "equipamento": ("Equipamento", st.text_input),
        "centro": ("Centro", st.text_input),
        "executante": ("Executante", st.text_input),
        "bt_confirmar": ("Confirmar", st.button)
    }
    helper.batch_create_io(defaut_inputs)
__section__()
render()