import streamlit as st
import pandas as pd
st.title("Findings and Thoughts")
st.write("In this page, we will diacuss what we did with the dataand what we \
         found so far. We will aslo discuss what we think about the data at this\
          point and what we plan to do next for this application.")
st.subheader("Raw Data")
st.write("Let's start by discussing the raw data and why we could not use it directly. \
         The raw data is a scraped dataset from 'indeed.com' that has about 12,300\
          data science job postings. The columns of the original dataset were as follows:\
         ")
raw_data = pd.read_csv("pages/originalOverview.csv")
d = pd.DataFrame({
    "Column": ["Job Title", "Location", "Job Salary","Job Description"],
    "Description": ["This column contained the job title from the posting ", 
                    "Location such as MI, California, Detroit MI ...etc",
                      "Salaries as numbers, ranges, or empty",
                      'A full description of the job inclus=ding qualification and \
                      sometimes the salary information']
})
st.table(d[['Column','Description']])
st.write("As we can see from the table above, there are many issues preventig using \
         the data as is. One of the reasons was inconsistency. A good example that shows\
          that would be the location column. Whne we look at the location, there are multiple\
          ways used to specify the location such as state name only, city and state, city, \
         state and zip code, state appreviation, and remote jobs. We needed to unify those \
         to help in the analysis. More details on how we did that are in the 'Data Preparation'\
         tab.")
st.write("One of the issues was the salary information. This feature is one of the main features\
          of the analysis in this application. However, it needd alot of work to be ready\
          to use. There were multiple problems when it came to salary information. Some salaries\
         are listed under the salary column, others are included within the job description,\
          and others are completely missing. Another issue is the formats, as some salaries \
         are listed as annual salaries, some are hourly and some eployers would list a range \
         that's contingent on experience. An extensive extraction and cleaning was neede to \
         make this data ready to use. See 'Data Preparation' tab and 'Imputation Comparison' \
         tab for more details.")
st.write("While job description has lots of useful data, it has lots of unnecessary data \
         as well. We had to parse this field to extract the needed data such as salary \
         information if available and the programming languages/qualifications required \
         for the job listing. Checkout the 'Data Preparation' Tab for more details.")
st.subheader("Cleaned Data")
st.write("cleaned data information goes here")
st.subheader("Imputed Data")
st.write("Trying to make a decision with missing data can be challenging. This missingess \
         we had to deal with in this dataset was the salary information. Unfortunately, \
         salary information is one of the main points of decision making in this application \
         so we had to do something about it. While some people may not be comfortable wtih \
         making decision based on synthesized data, others find totally fine if the data \
         is 'close enough' to the actual data. For that reason, we tested more than one \
         imputation method to fill in the missing data. Check out 'Imputation Comparison' \
         tab for more info.")
st.subheader("Findings")
st.write('While there\'s still much to explore about this dataset, here are our findings \
         so far: Findings based on visualization and correlation')
st.subheader("Thoughts")
st.write("Thoughts about the data and methods used")
st.subheader("What's Next")
st.write("Plans for the final project including using other functions to impute/\
         predict missing salary value. Additions to the project...etc.")
