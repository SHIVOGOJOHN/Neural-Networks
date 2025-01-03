# -*- coding: utf-8 -*-
"""Real Estate.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-HTstWjFTTwJFLJOPBzYxhq6DSe0kyTI
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from  tensorflow.keras.callbacks import EarlyStopping
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn  as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical

#load dataset
data=pd.read_csv("/content/Real estate.csv")
data.info()

data

#separate variables
x=data.drop(columns=['Y house price of unit area', 'X1 transaction date','No'], axis=1)
y=data['Y house price of unit area']

xtrain,xtest, ytrain,ytest=train_test_split(x,y,test_size=0.2, random_state=42)

#standerdize the numerical features
sc=StandardScaler()
xtrain=sc.fit_transform(xtrain)
xtest=sc.transform(xtest)

#Define the neural network architecture
model=Sequential()
model.add(Dense(64,input_dim=5, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
#output layer
model.add(Dense(1, activation='linear'))
#compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Define early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=5)

#train the model
model.fit(xtrain,ytrain, epochs=50,validation_split=0.2,callbacks=[early_stopping])

#Evaluate the model's performance
test_loss = model.evaluate(xtest, ytest)
print(f"Test loss (MSE): {test_loss}")

# Sample data based on the provided dataset structure
data1 = {
    "X2 house age": [13.3],            # X2
    "X3 distance to the nearest MRT station": [561.9845],  # X3
    "X4 number of convenience stores": [5],    # X4
    "X5 latitude": [24.98746],         # X5
    "X6 longitude": [121.54391],       # X6
}

# Create a DataFrame
df = pd.DataFrame(data1)

#standerdize the data
df=sc.transform(df)

# Step 6: Make a prediction
prediction = model.predict(df)

print(f"The predicted price for the new house is: ${prediction[0][0]:,.2f}")