import pandas as pd
import plotly.express as px
import streamlit as st
st.title('Dataset Analysis')
# Load your data
data = pd.read_csv('pages/knn_imputed_v2.csv')
st.subheader('Salary vs Location Visualization')
st.write('Use the following plot to see the salary ranges for jobs accress states.\
You can hover over a dot to show information.')
# Create a scatter plot for salary vs location
fig = px.scatter(
    data,
    x='Location',
    y='Salary From',  # Default to showing 'Salary From'
    color='Location',  # Color points by location
    title='Salary vs Location',
    height=600,
)

# Update hover information to format salaries with a dollar sign
fig.update_traces(
    hovertemplate=(
        'Job Title: %{hovertext}<br>' +
        'Salary From: $%{y:,.0f}<br>' +  # Added dollar sign here
        'Salary To: $%{customdata[0]:,.0f}<br>' +  # Added dollar sign here
        '<extra></extra>'
    ),
    hovertext=data['Job Title'],
    customdata=data[['Salary To']].values
)
st.plotly_chart(fig)
