import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
plt.style.use('ggplot')
full=pd.read_csv('C:/Users/Mohamed/Desktop/data sests for data analysis/full_data.csv')
full.rename(columns={'marital status':'marital_status'},inplace=True)
bi= [0,30000,60000,90000,np.inf]
lab= ['<30k','30k:60k','60k:90k','>90k']
full['avg_inc_cat']=pd.cut(full['avg_income'],bins=bi,labels=lab)
st.set_page_config(page_title = "Customer Demographics and certain groups behavior") 
st.title("Studying the spending behavior of specific customer groups.")
occ= st.sidebar.selectbox('Choose Occupation:',full['occupation'].unique())
cit= st.sidebar.selectbox('Choose City:',full['city'].unique())
mart= st.sidebar.selectbox('Choose Martial Status:',full['marital_status'].unique())
gen= st.sidebar.selectbox('Choose Gender:',full['gender'].unique())
ag= st.sidebar.selectbox('Choose Age Group:',full['age_group'].unique())
inc= st.sidebar.selectbox('Choose  Income Category:',full['avg_inc_cat'].unique())
mon= st.sidebar.selectbox('Choose  month:',full['month'].unique())
cat= st.sidebar.selectbox('Choose  Category:',full['category'].unique())
dt= full.groupby([full['occupation'],full['city'],full['avg_inc_cat'],full['marital_status'],full['category'],
                  full['gender'],full['age_group'],full['month'],
                  full['payment_type']])['spend'].agg([('total','sum'),('count','count'),('avg trans vol','mean')]).sort_values(by='total',ascending=False).reset_index()
st.write(dt.head(10))


dts=dt.query(f'occupation=="{occ}"').query(f'city=="{cit}"').query(f'marital_status=="{mart}"').query(f'gender=="{gen}"').query(f'age_group=="{ag}"').query(f'avg_inc_cat=="{inc}"').query(f'category=="{cat}"')
das= dts.groupby([dts['month'],dts['payment_type']])['total'].agg([('total','sum')]).reset_index()
das.month=pd.Categorical(das.month,categories=['May', 'June', 'July','August','September','October'])
das=das.sort_values('month')

p=px.line(das,x='month',
          y='total',
          color='payment_type')
st.plotly_chart(p)






cl1,cl2=st.columns(2)
pay1= cl1.selectbox('Choose Payment Type 1:',full['payment_type'].unique())
pay2= cl2.selectbox('Choose Payment Type 2:',full['payment_type'].unique())
data= full.query(f'occupation=="{occ}"').query(f'city=="{cit}"').query(f'marital_status=="{mart}"').query(f'gender=="{gen}"').query(f'age_group=="{ag}"').query(f'avg_inc_cat=="{inc}"').query(f'month=="{mon}"').query(f'category=="{cat}"')
f1d=data.query(f'payment_type=="{pay1}"')
f2d=data.query(f'payment_type=="{pay2}"')
cl1.write(f1d['spend'].sum())
cl1.write(f1d['spend'].count())
cl2.write(f2d['spend'].sum())
cl2.write(f2d['spend'].count())
cl1.write(f1d)
cl2.write(f2d)

f,a= plt.subplots(2)
sns.histplot(f1d['spend'],
             bins=10,
             kde=True,
            #  cumulative=True,
            stat='probability',
             ax=a[0])
sns.histplot(f2d['spend'],
             bins=10,
             kde=True,
            #  cumulative=True,
            stat='probability',
             ax=a[0])
sns.histplot(f1d['spend'],
             bins=10,
             kde=True,
             cumulative=True,
            stat='probability',
             ax=a[1])
sns.histplot(f2d['spend'],
             bins=10,
             kde=True,
             cumulative=True,
            stat='probability',
             ax=a[1])
a[0].legend([f'{pay1}',f'{pay2}'])
a[1].legend([f'{pay1}',f'{pay2}'])
st.pyplot(f)
