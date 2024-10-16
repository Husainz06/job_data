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


st.subheader('Average Salary Per State - Qualification Based')


# Fill NaN values in salary columns with 0 for calculations
data['Salary From'] = data['Salary From'].fillna(0)
data['Salary To'] = data['Salary To'].fillna(0)

# Calculate average salary
data['Average Salary'] = (data['Salary From'] + data['Salary To']) / 2

# Create a container for the checkboxes
with st.container():
    st.write("Select Qualifications to Filter:")
    qualifications = ['Python', 'Java', 'C++', 'SQL', 'Javascript', 'linux']
    
    # Create horizontal checkboxes
    cols = st.columns(len(qualifications))
    selected_qualifications = {}
    for i, qual in enumerate(qualifications):
        selected_qualifications[qual] = cols[i].checkbox(qual, value=True)

# Filter data based on selected qualifications
filtered_data = data.copy()
for qual, selected in selected_qualifications.items():
    if not selected:
        filtered_data = filtered_data[filtered_data[qual] == 0]

# Group by location and calculate the average salary
average_salary_by_location = filtered_data.groupby('Location')['Average Salary'].mean().reset_index()

# Create a Plotly bar chart for average salary per location with unique colors
fig = px.bar(
    average_salary_by_location,
    x='Location',
    y='Average Salary',
    color='Location',  # Color by location
    title='Average Salary per Location',
    labels={'Average Salary': 'Average Salary ($)', 'Location': 'Location'},
)

# Update layout for better visibility
fig.update_layout(xaxis_tickangle=-45)

# Show the plot in Streamlit
st.plotly_chart(fig)
