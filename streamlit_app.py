import streamlit as st
import pandas as pd, numpy as np
import sklearn

st.title('Machine Learning App')

st.write('This is a practice of deploying machine lesaning models.')
with st.expander('Data'):
  df = pd.read('https://github.com/JUBRIL-ADEBOGUN/Telecom-Customer-Churn/blob/main/customer-churn-cleaned.csv')
  df
