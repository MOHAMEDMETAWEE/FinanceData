import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
plt.style.use('ggplot')
full=pd.read_csv('C:/Users/Mohamed/Desktop/data sests for data analysis/full_data.csv')
full.rename(columns={'marital status':'marital_status'},inplace=True)
st.set_page_config(page_title = "Customer Classifiaction") 
st.title("Studying the spending behavior of specific customer groups.")
demo=st.sidebar.selectbox('Choose Demographic:',options=['Occupation','Age Group','Marital Status','Category','City','Gender'])
cho=st.sidebar.selectbox(f'Choose {demo}:',options=full[demo.lower().replace(" ","_")].unique())
mon=st.sidebar.selectbox('Choose Month:',options=['May',"June",'July','August','September','October'])

df= full.groupby([full[demo.lower().replace(" ","_")],full['month'],full['payment_type']])['spend'].agg([('total','sum'),('count','count'),('AVG','mean')]).reset_index()
col1,col2=st.columns(2)
st.title('Total revenu')
st.header('{:,}'.format(df.query(f'month=="{mon}"').query(f'{demo.lower().replace(' ','_')}=="{cho}"')['total'].sum()))
col2.title('AVG transaction volumn')
col2.header('{:,}'.format(df.query(f'month=="{mon}"').query(f'{demo.lower().replace(' ','_')}=="{cho}"')['AVG'].mean()))
col1.title('Number of transactions')
col1.header('{:,}'.format(df.query(f'month=="{mon}"').query(f'{demo.lower().replace(' ','_')}=="{cho}"')['count'].sum()))


py=px.line(df.query(f'month=="{mon}"'),
          x=f'{demo.lower().replace(' ','_')}',
          y='total',
          color='payment_type',
          title=f'The Relation between "{demo}" and Payment Type in "{mon}"')
st.plotly_chart(py)


st.header('Choose TWO Payment Types to compair between')
cl1,cl2=st.columns(2)
pay1=cl1.selectbox('Choose Payment Type 1:',options=full['payment_type'].unique())
pay2=cl2.selectbox('Choose Payment Type 2:',options=['UPI','Credit Card','Net Banking','Debit Card'])
f,a= plt.subplots(2)
sns.histplot(full.query(f'{demo.lower().replace(' ',"_")}=="{cho}"').query(f'month=="{mon}"').query(f'payment_type=="{pay1}"')['spend'],
             bins=250,
             kde=True,
             stat='probability',
             cumulative=True,
             ax=a[1]
            )
sns.histplot(full.query(f'{demo.lower().replace(' ',"_")}=="{cho}"').query(f'month=="{mon}"').query(f'payment_type=="{pay2}"')['spend'],
             bins=250,
             kde=True,
             stat='probability',
             cumulative=True,
            ax=a[1]
            )
sns.histplot(full.query(f'{demo.lower().replace(' ',"_")}=="{cho}"').query(f'month=="{mon}"').query(f'payment_type=="{pay1}"')['spend'],
             bins=250,
             kde=True,
             stat='probability',
            #  cumulative=True,
             ax=a[0]
            )
sns.histplot(full.query(f'{demo.lower().replace(' ',"_")}=="{cho}"').query(f'month=="{mon}"').query(f'payment_type=="{pay2}"')['spend'],
             bins=250,
             kde=True,
             stat='probability',
            #  cumulative=True,
            ax=a[0]
            )
a[0].legend([f'{pay1}',f'{pay2}'])
a[1].legend([f'{pay1}',f'{pay2}'])
st.pyplot(f)