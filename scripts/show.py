import streamlit as st
from PIL import Image

# reset everything
def reset():
    # st.balloons()
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['messages'] = [
        {"role": "system", "content": ''}
    ]
    st.session_state['model_name'] = []
    st.experimental_rerun()

def show_history():
    for i in range(len(st.session_state['generated'])):
        st.info(f'''{st.session_state['past'][i]}''', icon="🧙")
        if isinstance(st.session_state["generated"][i], Image.Image):
            st.image(st.session_state["generated"][i], caption=f'''{st.session_state["generated"][i]}''', use_column_width=True)
        else:
            st.success(f'''{st.session_state["generated"][i]}''', icon="🤖")