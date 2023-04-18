import numpy as np
import csv
import os
import streamlit as st

def init():
    # Initialise session state variables
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []
    if 'messages' not in st.session_state:
        st.session_state['messages'] = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    if 'model_name' not in st.session_state:
        st.session_state['model_name'] = []

def generate_csv():
    random_id = np.random.randint(1000000000)
    if not os.path.exists('./history'):
        os.makedirs('./history')
    with open(f'./history/{random_id}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['role', 'content'])
        if 'messages' in st.session_state:
            for i in st.session_state['messages']:
                # ignore system messages
                if i['role'] == 'system':
                    continue
                writer.writerow([i['role'], i['content']])
    with open(f'./history/{random_id}.csv', 'rb') as f:
        data = f.read()
    # print(data)
    os.remove(f'./history/{random_id}.csv')
    return data