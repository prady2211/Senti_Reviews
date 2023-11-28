import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(page_title= 'Reviews & Sentiments', layout= "wide")

image = Image.open('C:/Users/91976/Visual Code Projects/Sentiment & Review/download (1).png')
st.sidebar.image(image)

st.title("Reviews & Sentiments")
df= pd.read_csv("C:/Users/91976/Desktop/Reviews.csv")

st.markdown('---')

st.sidebar.subheader('Filter Product Here:')
item = st.sidebar.selectbox('Choose the Product for the Review',df['name'].unique())

st.subheader("Selected Product  : ")
st.write(item)

st.markdown('---')

col1,col2 = st.columns(2)


with col1:
 Avg_Rating=pd.DataFrame(df[df['name']==item]['reviews.rating']).mean()
 st.subheader("Avg. Rating: ")
 st.write(round(float(Avg_Rating),2))

with col2:
 Total_Ratings = pd.DataFrame(df[df['name']==item]['reviews.rating']).count()
 st.subheader("Total No of Reviews: ")
 st.write(int(Total_Ratings))

st.markdown('---')

st.subheader("Bar Plot:")
Bar_Graph=pd.DataFrame(df[df['name']==item]['reviews.rating']).value_counts()
Bar_Graph=Bar_Graph.reset_index()
chart=px.bar(Bar_Graph,x='reviews.rating',y='count',)
st.plotly_chart(chart)
 
st.subheader("Pie Chart:")
Bar_Graph=pd.DataFrame(df[df['name']==item]['reviews.rating']).value_counts()
Bar_Graph=Bar_Graph.reset_index()
fig=px.pie(Bar_Graph,values ='count',names='reviews.rating')
st.plotly_chart(fig)





