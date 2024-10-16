import streamlit as st
from sklearn.impute import SimpleImputer
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import KNNImputer


original = pd.read_csv('pages/cleaned_v2.csv')

st.title('Handling Missing Data - Imputation')
st.write('The dataset has missing salary information and the data is missing \
         compeletely at random (MCAR) as it is missing not because of a raltionship\
         to another feature or to certain values of the salary\
         Here, we compare the results of different imputation methods to see \
         how the dataset is affected\n In this page, we apply different\
         Data Imputation Techniques to see how the dataset is affected. First, let\'s see \
         the missing data that needs to be imputed.')

# Create a heatmap to visualize missing data
# Note that these are images as generating the plots slows down the loading
# All codes are available on the GitHub Repo.
st.image("Images/missing_heat_map.png", caption="Missing Data")

st.write('As can be seen from the figure above, there\'s a lot of missing salary data \
         which is a very important feature for the purposes of this application. Imputation \
         takes care of that and fills in the missing data. However, which imputation technique \
         is better? That\'s what we will try to answer in the follwoing sections.')
st.subheader('Data Distribution')
st.write('Since we implemented more than one imputation technique, we want to know which one is better \
         for this application. Below we will compare these to see what sort of information we can get \
         and if that information can help us pick an imputation technique over another.\n')

st.image("Images/histograms.png", caption="Data Distribution Comparison")

st.write('Let\'s see what information we can get from a box plot as it will help us better see the \
         quartiles and outliers')
st.image("Images/box_plots.png", caption="Box Plots")
