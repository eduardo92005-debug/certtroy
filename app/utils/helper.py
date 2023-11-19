import streamlit as st
import random

def form_creator(inputs=None):
    io = {}
    with st.form(key=f"st-form-{random.randint(0,9999)}",clear_on_submit=True):
        for input_id, (label, input_func) in inputs.items():
            input_value = input_func(label)
            io[input_id] = input_value
        return io
    
def batch_create_io(inputs=None):
    io = {}
    for input_id, (label, input_func) in inputs.items():
        input_value = input_func(label)
        io[input_id] = input_value
    return io   
        

def get_actual_section():
    return st.session_state.ACTUAL_SECTION

def get_actual_section_description():
    return st.session_state.ACTUAL_SECTION_DESCRIPTION

def set_actual_section(value, additional_description=None):
    st.session_state.ACTUAL_SECTION = value
    st.session_state.ACTUAL_SECTION_DESCRIPTION = additional_description
    return value