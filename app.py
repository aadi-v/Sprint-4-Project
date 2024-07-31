import streamlit as st
import pandas as pd
import plotly.express as px

vehicles = pd.read_csv('vehicles_us.csv')

st.write('Header Selection:')
title1 = st.checkbox('Header 1')
title2 = st.checkbox('Header 2')

if title1:
    st.header('United States Vehicle Data', divider='blue')
if title2:
    st.header('US Vehicle Data (1908-2019)', divider='red')

st.write('Student note: how can I use streamlit checkboxes to modify graphs? I could not find any good examples online.')
st.write('Would it be possible to have examples or lessons sent to me?')

chart1 = px.scatter(vehicles, x='model_year', y='price', title='Car Model Year vs Price',)
chart2 = px.histogram(vehicles['model_year'], title='Model Year vs Frequency')
st.write(chart1)
st.write(chart2)