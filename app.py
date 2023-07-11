import pandas as pd
import streamlit as st

def get_names_from_csv(file):
    # Read the CSV file
    df = pd.read_csv(file)

    # Check if 'Telegram handle' column exists in the dataframe
    if 'Telegram handle' in df.columns:
        # Get the column and convert to list
        names = df['Telegram handle'].tolist()
    else:
        names = []
        st.write("Column 'Telegram handle' not found.")
    return names

st.title('Telegram Handle Extractor')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    names = get_names_from_csv(uploaded_file)
    if names:
        st.write(names)  # Print the list to the Streamlit app
    else:
        st.write("No names found in the 'Telegram handle' column.")
else:
    st.write("Please upload a CSV file.")
