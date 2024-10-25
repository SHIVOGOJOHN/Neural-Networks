import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(r"D:\csv data\drug.csv")

# Set the title of the app
st.title('Drug Prescription Data Analysis')

# Display dataset
if st.checkbox('Show dataset'):
    st.write(data)

# Age distribution plot
st.subheader('Age Distribution')
fig, ax = plt.subplots()
sns.histplot(data['age'], kde=True, ax=ax)
st.pyplot(fig)

# Na_to_K distribution plot
st.subheader('Na_to_K Ratio Distribution')
fig, ax = plt.subplots()
sns.histplot(data['Na_to_K'], kde=True, ax=ax)
st.pyplot(fig)

# Distribution by drug
st.subheader('Drug Prescription Counts')
fig, ax = plt.subplots()
sns.countplot(x='drug', data=data)
st.pyplot(fig)

# Distribution by sex
st.subheader('Distribution by Sex')
fig, ax = plt.subplots()
sns.countplot(x='sex', data=data)
st.pyplot(fig)

# Blood Pressure distribution
st.subheader('Blood Pressure Distribution')
fig, ax = plt.subplots()
sns.countplot(x='bp', data=data)
st.pyplot(fig)

# Cholesterol levels distribution
st.subheader('Cholesterol Levels Distribution')
fig, ax = plt.subplots()
sns.countplot(x='cholesterol', data=data)
st.pyplot(fig)
