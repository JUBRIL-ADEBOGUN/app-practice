import streamlit as st
import pandas as pd, numpy as np
import sklearn

st.title('Machine Learning App')

st.write('This is a practice of deploying machine lesaning models.')
#with st.expander('Data'):
df = pd.read_csv("https://github.com/JUBRIL-ADEBOGUN/DSN-AI-BOOTCAMP-2024/blob/main/Train%20Dataset%20.csv", nrows=10)
df
