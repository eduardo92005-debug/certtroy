import streamlit as st
from app.common import template 
from app.utils import helper
from streamlit_extras.switch_page_button import switch_page
from app.common.components import green_button

def __section__():
    helper.set_actual_section("Seção 1", "Dados do executante")

@template.common_components
def render():
    #helper.validate_input(mask = r"^[A-Za-z ]+$", key = "test",text="TESTANNDO")
    #helper.tes()
    defaut_inputs = {
        "data_calibracao": ("Data de Calibração", st.date_input),
        "ordem": ("Ordem", st.text_input),
        "validade": ("Validade", st.date_input),
        "tipo_calibracao": ("Tipo de calibracao",st.text_input),
        "num_lote": ("Numero de lote de controle",st.text_input),
        "equipamento": ("Equipamento", st.text_input),
        "centro": ("Centro", st.text_input),
        "executante": ("Executante", st.text_input)
    }
   
    output = helper.batch_create_io(defaut_inputs)
    bt_confirm = green_button.__style__("Confirmar")
    if bt_confirm:
        print(output)
        switch_page("Seção_2")
__section__()
render()