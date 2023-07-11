import pandas as pd
import streamlit as st
import numpy as np

def get_names_from_csv(file):
    df = pd.read_csv(file)
    if 'Telegram handle' in df.columns:
        names = df[df['Telegram handle'] != '-']['Telegram handle'].tolist()
    else:
        names = []
        st.write("Column 'Telegram handle' not found.")
    return np.array(names)

st.title('Telegram Handle Extractor')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    names = get_names_from_csv(uploaded_file)
    if names.size: 
        st.write(f'users: {np.array2string(names, separator=", ", formatter={"str_kind": lambda x: f"\"{x}\""})}') 
    else:
        st.write("No names found in the 'Telegram handle' column.")
else:
    st.write("Please upload a CSV file.")
