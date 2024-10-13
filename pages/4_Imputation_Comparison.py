import streamlit as st
from sklearn.impute import SimpleImputer
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import KNNImputer


original_df = pd.read_csv('pages/cleaned.csv')

st.title('Handling Missing Data - Imputation')
st.write('The dataset has missing salary information and the data is missing \
         compeletely at random (MCAR) as it is missing not because of a raltionship\
         to another feature or to certain values of the salary\
         Here, we compare the results of different imputation methods to see \
         how the dataset is affected\n In this page, we apply different\
         Data Imputation Techniques to see how the dataset is affected')

st.subheader('Original Data')
st.write('Here we want to see how the original data looks like i.e. before imputation\n')


# First plot
plt.figure(figsize=(8, 6))
plt.boxplot([original_df['Salary From'].dropna(), original_df['Salary To'].dropna()])#, tick_labels=['Salary From', 'Salary To'])
plt.title('Salary Distribution (Box Plot)')
plt.ylabel('Salary')
plt.grid()

# Display the plot in Streamlit
st.pyplot(plt)

plt.clf()

st.subheader('Mean Imputation')
st.write('In this section, we apply mean imputation i.e. utilizing the mean and\
          standard deviation of the salaries column to fill in the missing values.\
         In this section, we are dropping the missing values fromt the visualization')

# Calculating the means and stds
#mean_low = original_df['Salary From'].mean()
#std_low = original_df['Salary From'].std()

#mean_high = original_df['Salary To'].mean()
#std_high = original_df['Salary To'].std()

# Make an independent copy of the dataframe
df_mean_imputation = pd.read_csv('pages/mean_imputed.csv')

#Find missing indicies in the columns
#missing_indices_low = df_mean_imputation['Salary From'].isna()
#missing_indices_high = df_mean_imputation['Salary To'].isna()

# Impute data using mean + std
#df_mean_imputation.loc[missing_indices_low, 'Salary From'] = np.random.randn(missing_indices_low.sum()) * std_low + mean_low
#df_mean_imputation.loc[missing_indices_high, 'Salary To'] = np.random.randn(missing_indices_high.sum()) * std_high + std_high

# Plot
plt.hist(df_mean_imputation['Salary From'], stacked = True, bins = 30)
plt.xlim(10000, 300000)

plt.figure(figsize=(8, 6))
plt.boxplot([df_mean_imputation['Salary From'], df_mean_imputation['Salary To']], tick_labels=['Salary From', 'Salary To'])
plt.title('Salary Distribution Mean Imputation')
plt.ylabel('Salary')
plt.grid()
st.pyplot(plt)

plt.clf()
st.subheader('KNN Imputation')
st.write('In this section, we apply KNN imputation to see what difference it makes in the \
          salary distribution compared to the Mean imputation.')



# KNN

#Make an indepenedent copy for KNN
df_knn = pd.read_csv('pages/knnimputed.csv')

# KNN
#df_knn['Salary From'] = pd.to_numeric(df_knn['Salary From'], errors='coerce')
#df_knn['Salary To'] = pd.to_numeric(df_knn['Salary To'], errors='coerce')

# Create KNNImputer
#knn_imputer = KNNImputer(n_neighbors=5)

# Select only numeric columns for imputation
#numeric_cols = df_knn.select_dtypes(include=['float64', 'int64']).columns

# Perform KNN imputation
#df_knn[numeric_cols] = knn_imputer.fit_transform(df_knn[numeric_cols])


# Plot

plt.figure(figsize=(8, 6))
plt.boxplot([df_knn['Salary From'], df_knn['Salary To']], tick_labels=['Salary From', 'Salary To'])
plt.title('Salary Distribution KNN Imputation')
plt.ylabel('Salary')
plt.grid()
st.pyplot(plt)


plt.clf()

st.subheader("Comparison")
st.write('In this section we compare the results of the imputations using histograms that show the distribution\
         of the salaries.')


# comparisons
import seaborn as sns

# original vs mean imputation

plt.subplot(221)
sns.histplot(original_df['Salary From'].dropna(), kde=True, color='blue', alpha=0.5, label='Original')
sns.histplot(df_mean_imputation['Salary From'], kde=True, color='green', alpha=0.5, label='Mean Imputed', bins=30)
plt.legend()

plt.subplot(222)
sns.histplot(original_df['Salary To'].dropna(), kde=True, color='blue', alpha=0.5, label='Original')
sns.histplot(df_mean_imputation['Salary To'], kde=True, color='green', alpha=0.5, label='Mean Imputed', bins=30)
plt.legend()
plt.show()
plt.suptitle('Original VS Mean Imputation')

st.pyplot(plt)
plt.clf()

# original vs knn

plt.subplot(221)
sns.histplot(original_df['Salary From'].dropna(), kde=True, color='blue', alpha=0.5, label='Original')
sns.histplot(df_knn['Salary From'], kde=True, color='green', alpha=0.5, label='KNN Imputed', bins=30)
plt.legend()

plt.subplot(222)
sns.histplot(original_df['Salary To'].dropna(), kde=True, color='blue', alpha=0.5, label='Original')
sns.histplot(df_knn['Salary To'], kde=True, color='green', alpha=0.5, label='KNN Imputed', bins=30)
plt.legend()
plt.show()
plt.suptitle('Original VS KNN Imputation')

st.pyplot(plt)
plt.clf()
