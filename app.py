import streamlit as st
import pandas as pd
import plotly.express as px

vehicles = pd.read_csv('vehicles_us.csv')
vehicles_50 = vehicles[vehicles['price']<=9000]
vehicles_75 = vehicles[vehicles['price']<=17000]

st.write('Header Selection:')
title1 = st.checkbox('Header 1')
title2 = st.checkbox('Header 2')

if title1:
    st.header('United States Vehicle Data', divider='blue')
if title2:
    st.header('US Vehicle Data (1908-2019)', divider='red')

st.write('Student note: how can I use streamlit checkboxes to modify graphs? I could not find any good examples online.')
st.write('Would it be possible to have examples or lessons sent to me?')

chart1 = px.scatter(vehicles, x='model_year', y='odometer', title='Car Model Year vs Mileage')
chart2 = px.histogram(vehicles_50['price'], x='price', y='total cars at price', title='Price vs Frequency')
chart3 = px.histogram(vehicles_75['price'], x='price', y='total cars at price', title='Price vs Frequency')
chart4 = px.histogram(vehicles['price'], x='price', y='total cars at price', title='Price vs Frequency')

st.write(chart1)

st.write('Histogram Selection:')
hist1 = st.checkbox('50th Percentile of Car Prices')
hist2 = st.checkbox('75th Percentile of Car Prices')
hist3 = st.checkbox('All Car Prices', disabled=False)

if hist1:
    st.write(chart2)
if hist2:
    st.write(chart3)
if hist3:
    st.write(chart4)