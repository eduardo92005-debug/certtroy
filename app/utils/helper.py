import streamlit as st

def batch_create_io(inputs=None):
    for input_id, (label, input_func) in inputs.items():
        input_value = input_func(label)
    return inputs

def get_actual_section():
    return st.session_state.ACTUAL_SECTION

def get_actual_section_description():
    return st.session_state.ACTUAL_SECTION_DESCRIPTION

def set_actual_section(value, additional_description=None):
    st.session_state.ACTUAL_SECTION = value
    st.session_state.ACTUAL_SECTION_DESCRIPTION = additional_description
    return value
    