import pandas as pd
import plotly.express as px
import streamlit as st
st.title('Dataset Analysis')
# Load your data
data = pd.read_csv('cleaned_v2.csv')

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

# Get unique locations for dropdown
locations = data['Location'].unique()

# Create dropdown buttons for each location
buttons = [
    {
        'label': location,
        'method': 'update',
        'args': [
            {'x': [location], 'y': [data.loc[data['Location'] == location, 'Salary From']]},
            {'title': f'Salary From vs {location}'}
        ]
    }
    for location in locations
]

# Add button to show all locations
buttons.append({
    'label': 'All Locations',
    'method': 'update',
    'args': [
        {'x': data['Location'], 'y': data['Salary From']},
        {'title': 'Salary From vs Location'}
    ]
})

# Update layout with dropdown menu
fig.update_layout(
    updatemenus=[
        {
            'buttons': buttons,
            'direction': 'down',
            'showactive': True,
            'x': 0.1,
            'xanchor': 'left',
            'y': 1.1,
            'yanchor': 'top'
        }
    ]
)

# Streamlit app layout
st.title('Salary vs Location Visualization')
st.plotly_chart(fig)
