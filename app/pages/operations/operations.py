import streamlit as st
from app.common import template 
from app.utils import helper
from streamlit_extras.switch_page_button import switch_page
from app.pages.operations.components import submit_button
from app.pages.operations.components import end_button
import time

def __section__():
    helper.set_actual_section("Operações", "Sobre as operações")

@template.common_components
def render():
    #helper.validate_input(mask = r"^[A-Za-z ]+$", key = "test",text="TESTANNDO")
    #helper.tes()
    # default_inputs = {
    #     "num_operation": ("Numero da operação", st.text_input),
    #     "Tolerancia": ("Tolerancia", st.text_input),
    #     "VVC": ("VCC: Valor do certificado", st.date_input),
    #     "FOUND": ("Encontrado: Valor lido na instalação",st.text_input),
    #     "X1": ("X1: Medição X1",st.text_input),
    #     "X2": ("X2: Medição X2", st.text_input),
    #     "X3": ("X3: Medição X3", st.text_input),
    #     "U": ("Incerteza calculada", st.text_input),
    #     "K": ("FATOR K calculado", st.text_input),
    #     "E": ("Erro total calculado", st.text_input),
    #     "bt_new": ("(+) Nova operacao",submit_button.__style__)
    # }
    with st.form("st-form-main",clear_on_submit=True):
        num_operation = st.text_input("Numero da operação")
        tolerancia = st.text_input("Tolerancia")
        vvc = st.date_input("VCC: Valor do certificado")
        found = st.text_input("Encontrado: Valor lido na instalação")
        x1 = st.text_input("X1: Medição X1")
        x2 = st.text_input("X2: Medição X2")
        x3 = st.text_input("X3: Medição X3")
        u = st.text_input("Incerteza calculada")
        k = st.text_input("FATOR K calculado")
        e = st.text_input("Erro total calculado")
        bt_new = submit_button.__style__("(+) Nova operação")
    
    data = {
        "num_operation": num_operation,
        "Tolerancia": tolerancia,
        "VVC": vvc,
        "FOUND": found,
        "X1": x1,
        "X2": x2,
        "X3": x3,
        "U": u,
        "K": k,
        "E": e,
        "bt_new": bt_new
    }
    # output = helper.form_creator(default_inputs)
    bt_confirm = end_button.__style__("Finalizar")
    # bt_new = default_inputs["bt_new"][1]
    # st.session_state.INITIAL = 0
    if bt_confirm:
        #generate_pdf()
        switch_page("Home")
    if bt_new: 
        print(data)
        #post_on_bd()
        # if st.session_state.INITIAL == 0:
        #     print("teste")
        #     with st.spinner("Aguarde..."):
        #         time.sleep(5)
        #     st.success("Insira uma nova operacao!")
        # print(st.session_state.INITIAL)
        # st.session_state.INITIAL = 1
__section__()
render()