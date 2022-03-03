import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df2 = pd.read_excel('mi_2021_oor_data.xlsx', sheet_name='Sheet1')
df2 = df2[['COUNTY/METRO','Income needed to afford 1 bdrm FMR', 'Income needed to afford 2 bdrm FMR']]
df2 = df2.dropna()

#Toggle data display
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df2)

#County multiselect
if st.checkbox('Show filtered data'):
    st.subheader('Filtered data')
    full_county_list = list(df2['COUNTY/METRO'].values)
    options = st.multiselect('Select counties to inspect',
    full_county_list)
    our_counties = options
    df2 = df2[df2['COUNTY/METRO'].isin(our_counties)]
    df2 = pd.melt(df2, id_vars=['COUNTY/METRO'])
    st.write(df2)


#g.despine(left=True)
#g.set_axis_labels("Counties", "Annual Income to afford Fair Market Rent")
#g.legend.set_title("")
sns.set_style('whitegrid')
if st.checkbox('Show our county chart'):
    #import seaborn as sns
    #st.subheader('Annual Income Needed to Afford FMR')
    #sns.catplot(data=df2, kind='bar',
    #x='COUNTY/METRO', y='value', hue='variable', palette='dark', alpha=.6, height=6)
    #st.pyplot()
    x = np.arange(len(df2['COUNTY/METRO'].unique()))
    labels = list(df2['COUNTY/METRO'].unique())
    width = 0.35
    one_bd = df2.loc[df2['variable']=='Income needed to afford 1 bdrm FMR', 'value']
    two_bd = df2.loc[df2['variable']=='Income needed to afford 2 bdrm FMR', 'value']
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, one_bd, width, label='1 bdrm')
    rects2 = ax.bar(x + width/2, two_bd, width, label='2 bdrm')
    ax.set_ylabel('Annual Income Needed to Afford 1 Bdrm FMR')
    ax.set_title('Income for FMR by County - 1 and 2 Bedrooms')
    ax.legend()
    fig.tight_layout()
    plt.xticks(x, labels)
    st.pyplot(fig)