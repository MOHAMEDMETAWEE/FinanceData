import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
plt.style.use('ggplot')
spend=pd.read_csv('C:/Users/Mohamed/Desktop/data sests for data analysis/tt.csv').drop(columns='Unnamed: 0')

st.write(spend)


# occ= st.sidebar.selectbox('Choose Occupation:',spend['occupation'].unique())
# cit= st.sidebar.selectbox('Choose City:',spend['city'].unique())
# mart= st.sidebar.selectbox('Choose Martial Status:',spend['marital_status'].unique())
# gen= st.sidebar.selectbox('Choose Gender:',spend['gender'].unique())
# ag= st.sidebar.selectbox('Choose Age Group:',spend['age_group'].unique())
# inc= st.sidebar.selectbox('Choose  Income Category:',spend['avg_inc_cat'].unique())
# mon= st.sidebar.selectbox('Choose  month:',spend['month'].unique())
# cat= st.sidebar.selectbox('Choose  Category:',spend['category'].unique())
# dt= spend.groupby([spend['occupation'],spend['city'],spend['avg_inc_cat'],spend['marital_status'],spend['category'],
#                   spend['gender'],spend['age_group'],spend['month'],
#                   spend['payment_type']])['inc_uti'].agg([('total','sum'),('count','count'),('avg trans vol','mean')]).sort_values(by='total',ascending=False).reset_index()
# st.write(dt.head(10))




