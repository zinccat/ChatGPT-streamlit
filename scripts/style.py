import streamlit as st

def set_style():
    # Setting page title and header
    st.set_page_config(page_title="Exobrain", page_icon="🤯") #, layout="wide", initial_sidebar_state="expanded")
    # space before sidebar title, code error
    hide_streamlit_style = """
                    <style>
                    [data-testid="stSidebarNav"] {
                    visibility: hidden;
                        height: 0px;
                    }
                    .css-1oe5cao e1fqkh3o9 {
                    visibility: hidden;
                    height: 0px;
                    }
                    <style>
                    .css-nps9tx, .e1m3hlzs0, .css-1p0bytv, .e1m3hlzs1 {
                    visibility: hidden;
                    height: 0px;
                    }
                    div[data-testid="stToolbar"] {
                    visibility: hidden;
                    height: 0%;
                    position: fixed;
                    }
                    div[data-testid="stDecoration"] {
                    visibility: hidden;
                    height: 0%;
                    position: fixed;
                    }
                    div[data-testid="stStatusWidget"] {
                    visibility: hidden;
                    height: 0%;
                    position: fixed;
                    }
                    #MainMenu {
                    visibility: hidden;
                    height: 0%;
                    }
                    header {
                    visibility: hidden;
                    height: 0%;
                    }
                    footer {
                    visibility: hidden;
                    height: 0%;
                    }
                    </style>
                    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 