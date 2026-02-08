import streamlit as st
import pandas as pd
import plotly.express as px
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title='SuperStore!!!',page_icon=':bar_chart',layout='wide')

st.title(":bar_chart: Sample SuperStore EDA")


st.markdown('<style>div.block-container{pandding-top:lrem;}</style>',unsafe_allow_html=True)

fl = st.file_uploader(":file_folder:Upload a file",type=(["csv","txt","xlsx","xls"]))
if fl is not None:
 filename =fl.name
 st.write(filename)
 df=pd.read_csv(filename,encoding='ISO-8859-1')
else:
 os.chdir(r"C:\Programmings\Streamlit\SuperStore")
 df = pd.read_csv('Superstore.csv', encoding='ISO-8859-1')
 
 
col1, col2 =st.columns((2))
df["Order Date"]=pd.to_datetime(df["Order Date"])
 
 # Getting the min max date 
startDate = pd.to_datetime(df['Order Date']).min()
endDate=pd.to_datetime(df['Order Date']).max()

with col1:
 date1=pd.to_datetime(st.date_input("Start Date",startDate))

with col2:
 date2=pd.to_datetime(st.date_input("Start Date",endDate))

df =df[(df["Order Date"]>=date1) & (df['Order Date']<=date2)].copy()

st.sidebar.header("Choose your filter: ")
region=st.sidebar.multiselect("Pick your Region",df['Region'].unique())
if not region:
 df2= df.copy()
else:
 df2=df[df["Region"].isin(region)]

#create for state
state = st.sidebar.multiselect("Pick your state",df2['State'].unique())
if not state:
 df3=df2.copy()
else:
 df3=df2[df2['State'].isin(state)]
 
# create for city
city =st.sidebar.multiselect("Pick your city:",df3["City"].unique())

# filter the data based on region, state and city
if not region and not state and not city:
 filtered_df =df
elif not state and not city:
 filtered_df =df[df["Region"].isin(region)]
elif not region and not city:
 filtered_df=df[df["State"].isin(state)]
elif state and city:
 filtered_df=df3[df3["State"].isin(state) & df3['City'].isin(city)]
elif region and city:
 filtered_df=df3[df3["Region"].isin(region) & df3['City'].isin(city)]
elif region and state:
 filtered_df=df3[df3["Region"].isin(region) & df3['State'].isin(state)]
elif city:
 filtered_df=df3[df3["City"].isin(city)]
else:
 filtered_df=df3[
  df3['Region'].isin(region)
  & df3['State'].isin(state)
  & df3['City'].isin(city)
 ]
 
category_df=filtered_df.groupby(by=['Category'],as_index=False)["Sales"].sum()

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
 st.subheader("Category wise Sales")
 fig = px.bar(
  category_df, 
  x="Category", 
  y="Sales", 
  text=['${:,.2f}'.format(x) for x in category_df["Sales"]],
  template="seaborn",
  height=450
 )
 st.plotly_chart(fig,use_container_width=True)

with chart_col2:
 st.subheader("Region wise Sales")
 fig =px.pie(filtered_df, values="Sales",names="Region",hole=0.5, height=450)
 fig.update_traces(text=filtered_df['Region'],textposition='outside')
 st.plotly_chart(fig,use_container_width=True)
 

cl1,cl2=st.columns(2)
with cl1:
    with st.expander("Category_ViewData"):
        st.dataframe(category_df)
        csv = category_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            'Download Data',
            data=csv,
            file_name="Category.csv",
            mime="text/csv",
            help="click here to download the data as a csv file"
        )

with cl2:
    with st.expander("Region_ViewData"):
        region_df = filtered_df.groupby(by="Region", as_index=False)["Sales"].sum()
        st.dataframe(region_df)
        csv = region_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            'Download Data',
            data=csv,
            file_name="Region.csv",
            mime="text/csv",
            help="click here to download the data as a csv file"
        )

st.markdown("---") 

filtered_df['month_year'] = filtered_df['Order Date'].dt.to_period('M').dt.strftime("%Y : %b")
st.subheader("Time Series Analysis")

linechart = filtered_df.groupby('month_year', as_index=False)['Sales'].sum()

fig2 = px.line(
    linechart,
    x='month_year',
    y='Sales',
    labels={"Sales": "Amount"},
    height=500,
    width=1000,
    template="gridon"
)
st.plotly_chart(fig2, use_container_width=True)

with st.expander("View data of Timeseries:"):
 st.write(linechart.T.style.background_gradient(cmap="Blue"))
 csv = linechart.to_csv(index=False).encode('utf-8')
 st.download_button("Download Data", data=csv, file_name="Timeseries.csv",mime="text/csv")
 
st.markdown("---")

# create a tree based on Region, category, sub-category
st.subheader("Hierarchical view of Sales using treeMap")
fig3=px.treemap(filtered_df,path=['Region','Category','Sub-Category'],values="Sales",hover_data=["Sales"],
                color="Sub-Category")
fig3.update_layout(width=800, height=650)
st.plotly_chart(fig3, use_container_width=True)

chart1,chart2=st.columns((2))
with chart1:
 st.subheader("Segment wise Sales")
 fig=px.pie(filtered_df, values="Sales",names="Segment",template="plotly_dark")
 fig.update_traces(text=filtered_df['Segment'],textposition='inside')
 st.plotly_chart(fig,use_container_width=True)
 
with chart2:
 st.subheader("Category wise Sales")
 fig=px.pie(filtered_df, values="Sales",names="Category",template="gridon")
 fig.update_traces(text=filtered_df['Category'],textposition='inside')
 st.plotly_chart(fig,use_container_width=True)
 
import plotly.figure_factory as ff
st.subheader(":point_right: Month wise Sub-Category Sales Summary")
with st.expander("Summary_Table"):
 df_sample =df[0:5][["Region","State","City",'Category',"Profit","Quantity"]]
 fig=ff.create_table(df_sample,colorscale='Cividis')
 st.plotly_chart(fig,use_container_width=True) 

st.markdown("---")

st.markdown("Month wise sub-category Sales table")
filtered_df['month']=filtered_df['Order Date'].dt.month_name()
sub_category_year=pd.pivot_table(data=filtered_df,values="Sales",index=['Sub-Category'],columns='month')
st.write(sub_category_year.style.background_gradient(cmap="Blues"))

# Create the scatter plot
fig4 = px.scatter(
 filtered_df,
 x="Sales",
 y="Profit",
 size="Quantity",
 title="Relationship between Sales and Profits using Scatter plot"
)
fig4.update_layout(
 title_font=dict(size=20),
 xaxis_title="Sales",
 xaxis_title_font=dict(size=19),
 yaxis_title="Profit",
 yaxis_title_font=dict(size=19)
)
st.plotly_chart(fig4, use_container_width=True)

with st.expander("View Data"):
 st.write(filtered_df.iloc[:500,1:20:2].style.background_gradient(cmap='YlOrBr'))
 
# Download the orginal Dataset
csv=df.to_csv(index=False).encode('utf-8')
st.download_button("Download Data",data=csv,file_name="Data.scs",mime="text/csv")
