import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df2 = pd.read_excel('mi_2021_oor_data.xlsx', sheet_name='Sheet1')
df2 = df2[['COUNTY/METRO','Income needed to afford 1 bdrm FMR', 'Income needed to afford 2 bdrm FMR']]

#Toggle data display
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df2)

#Our counties
our_counties = ['Wayne County', 'Macomb County', 'Oakland County']
df2 = df2[df2['COUNTY/METRO'].isin(our_counties)]
df2 = pd.melt(df2, id_vars=['COUNTY/METRO'])


#g.despine(left=True)
#g.set_axis_labels("Counties", "Annual Income to afford Fair Market Rent")
#g.legend.set_title("")
if st.checkbox('Show our county chart', value=True):
    import seaborn as sns
    st.subheader('Annual Income Needed to Afford FMR')
    sns.catplot(data=df2, kind='bar',
    x='COUNTY/METRO', y='value', hue='variable', palette='dark', alpha=.6, height=6)
    st.pyplot()