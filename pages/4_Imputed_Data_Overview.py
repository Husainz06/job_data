import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.write('Testing plots')

mean_df = pd.read_csv('pages/mean_imputed.csv')

mean_df['Salary From'].plot(kind='hist', bins=30, alpha=0.5, color='blue', edgecolor='black')
st.pyplot(plt)