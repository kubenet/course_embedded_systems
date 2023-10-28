import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv('your_data.csv')

# Set the page title
st.title('Data Monitoring Dashboard')

# Display the data
st.subheader('Data Overview')
st.write(data.head())

# Show data statistics
st.subheader('Data Statistics')
st.write(data.describe())

# Visualize data using charts
st.subheader('Data Visualization')

# Bar chart
st.subheader('Bar Chart')
bar_chart_data = data['column_name'].value_counts()
st.bar_chart(bar_chart_data)

# Line chart
st.subheader('Line Chart')
line_chart_data = data['column_name']
st.line_chart(line_chart_data)

# Area chart
st.subheader('Area Chart')
area_chart_data = data['column_name']
st.area_chart(area_chart_data)

# Scatter plot
st.subheader('Scatter Plot')
scatter_plot_data = data[['column_name_1', 'column_name_2']]
st.scatterplot(scatter_plot_data['column_name_1'], scatter_plot_data['column_name_2'])

# Add other visualizations as needed

# Show raw data
st.subheader('Raw Data')
st.write(data)

# Add interactivity (optional)
# Example: Filter data based on a specific condition
st.sidebar.title('Filter Data')
selected_category = st.sidebar.selectbox('Select Category', data['category'].unique())
filtered_data = data[data['category'] == selected_category]
st.write(filtered_data)


