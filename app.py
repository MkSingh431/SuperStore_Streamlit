import streamlit as st
import pandas as pd
import plotly.express as px
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title='SuperStore!!!',page_icon=':bar_chart',layout='wide')

st.title(":bar_chart: Sample SuperStore EDA")


st.markdown("<style>div.block-container{pandding-top:lrem;}</style>",unsafe_allow_html=True)

fl=st.file_uploader(":file_folder:Uploader a file",type=(["csv","txt","xlsx","xls"]))
if fl is not None:
 filename=fl.name
 st.write(filename)
 df=pd.read_csv(filename, encoding='ISO-8859-1')
else:
 os.chdir(r"C:\Programmings\Streamlit\SuperStore")
 df=pd.read_csv("Superstore.csv",encoding='ISO-8859-1')
 

col1, col2=st.columns((2))
df['Order Date']=pd.to_datetime(df['Order Date'])

# Getting the min max date
startDate=pd.to_datetime(df['Order Date']).min()
endDate=pd.to_datetime(df['Order Date']).max()

with col1:
 date1=pd.to_datetime(st.date_input("Start Date",startDate))
 
with col2:
 date2=pd.to_datetime(st.date_input("End Date",endDate))

df=df[(df['Order Date']>=date1) & (df['Order Date']<=date2)].copy()

st.sidebar.header(" Choose your filter:")
region=st.sidebar.multiselect("Pick your Region",df['Region'].unique())
