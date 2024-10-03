import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Load dataset
data = pd.read_csv('https://raw.githubusercontent.com/AhlanAlghiff/Daily-Bike-Sharing-Analysis-Dashboard/refs/heads/master/dashboard/bike_df.csv')

# Data preprocessing
data['dteday'] = pd.to_datetime(data['dteday'])
data['month'] = data['dteday'].dt.month
data['season'] = data['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

# Dashboard title
st.title('Bike Sharing Analysis Dashboard')

# Sidebar untuk pilih visual dari group yang tersedia
st.sidebar.header('Select Visualization')
visualization_type = st.sidebar.selectbox(
    'Choose the type of visualization:',
    ['Total Rentals by Season', 'Total Rentals by Month', 'Data Preview']
)

# Display yang akan muncul
if visualization_type == 'Total Rentals by Season':
    st.header('Total Rentals by Season')
    season_counts = data.groupby('season')['count'].sum()
    st.bar_chart(season_counts)

elif visualization_type == 'Total Rentals by Month':
    st.header('Total Rentals by Month')
    month_counts = data.groupby('month')['count'].sum()
    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_counts.index = month_labels
    st.bar_chart(month_counts)

else:
    st.header('Data Preview')
    st.write(data.head())

# Total Penyewa sepeda
total_rentals = data['count'].sum()
st.subheader(f'Total Bike Rentals: {total_rentals}')
