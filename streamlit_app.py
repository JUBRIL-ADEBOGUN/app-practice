import streamlit as st
import pandas as pd, numpy as np
import sklearn

st.title('Machine Learning App')

st.write('This is a practice of deploying machine lesaning models.')
with st.expander('Data'):
  st.write("**Raw Data**")
  df = pd.read_csv("https://raw.githubusercontent.com/JUBRIL-ADEBOGUN/DSN-AI-BOOTCAMP-2024/refs/heads/main/Train%20Dataset%20.csv")
  df
st.header("Basic Data Exploration")

