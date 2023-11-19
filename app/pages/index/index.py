import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from app.common.components import green_button
                   

def render():
    # Texto explicativo inicial
    text = """
    Muitas indústrias e laboratórios dependem de equipamentos que convertem eletricidade em peso para garantir a precisão e a confiabilidade de seus processos. 
    Para garantir a qualidade e a confiabilidade desses equipamentos, a calibração regular é essencial. 
    O Certificado de Calibração é um documento fundamental que fornece detalhes sobre o processo de calibração, os resultados obtidos e outras informações relevantes. 
    Neste contexto, criaremos um aplicativo básico em Streamlit para gerar um Certificado de Calibração para um equipamento de conversão de eletricidade em peso, que consistirá em três seções: Dados do Executante, Dados das Análises e Revisão.
    """

    st.title("Aplicativo de Certificado de Calibração")
    st.write(text)
    start_button = green_button.__style__("Iniciar")
    if start_button:
        switch_page("Seção_1")
render()