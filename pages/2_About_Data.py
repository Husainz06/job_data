import streamlit as st
import pandas as pd


st.subheader('Data Overview')
st.write("The dataset contsains a little over 12,300 Data Science job postings from\
         Indeed.com. Below is a sample of the original rawn data:\n")
original_df = pd.read_csv('/Users/husainz/Desktop/F2024/CMSE 830/Project/job_data/pages/US_data_science_jobs_2023-6-19_0.csv')
st.write(original_df.head(50))
st.write('The data had to be cleaned in several ways to get to be usable for this project.\
         To read more details about the cleaning and encoding process, check out the \'Data Preparation\' tab.')
original_df = pd.read_csv('/workspaces/job_data/pages/cleaned.csv')

st.write('Data Sample:')
st.write(df.head(50))



st.subheader("Basic Statistics")
st.write(df.describe())

st.subheader("Job count per state:")
st.write(df.groupby('Location').size().reset_index(name='Job Count'))
