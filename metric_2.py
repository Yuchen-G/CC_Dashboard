import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df2 = pd.read_excel('mi_2021_oor_data.xlsx', sheet_name='Sheet1')
df2 = df2[['COUNTY/METRO','Income needed to afford 1 bdrm FMR', 'Income needed to afford 2 bdrm FMR']]

#Toggle data display
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df2)