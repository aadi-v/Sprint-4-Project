import streamlit as st
import pandas as pd
import plotly.express as px

vehicles = pd.read_csv('vehicles_us.csv')

title1 = st.checkbox('Title 1')
title2 = st.checkbox('Title 2')

if title1:
    st.header('United States Vehicle Data', divider='blue')
if title2
    st.header('US Vehicle Data (1908-2019)', divder='red')

st.header('United States Vehicle Data', divider='blue')

chart1 = px.scatter(vehicles, x='model_year', y='price')
chart2 = px.histogram(vehicles['model_year'])
st.write(chart1)
st.write(chart2)