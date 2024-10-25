# Drug Classification Model

This project implements a neural network to predict the type of drug recommended for a patient based on demographic and medical data. Using TensorFlow and Keras, the model classifies drugs based on features like age, sex, blood pressure (BP), and cholesterol levels. 

## 💡Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Training the Model](#training-the-model)
- [Making Predictions](#making-predictions)
- [Evaluation](#evaluation)
- [Future Work](#future-work)

## 💡Project Overview
This project builds a classification model to predict the correct drug type for a given patient using demographic and medical details. The model is trained to distinguish between multiple drug classes and is designed to handle both numerical and categorical features. 

## 💡Dataset
The dataset used in this project, `drug.csv`, contains the following columns:
- **Age**: Age of the patient.
- **Sex**: Gender of the patient (`F` for Female, `M` for Male).
- **BP**: Blood pressure level (`HIGH`, `NORMAL`, `LOW`).
- **Cholesterol**: Cholesterol level (`HIGH`, `NORMAL`).
- **Na_to_K**: Sodium-to-potassium ratio in blood.
- **Drug**: Target variable indicating the drug type prescribed.

## 💡Code


## 💡Model Architecture
A neural network is built with TensorFlow's Keras API, containing the following layers:
1. Input layer with 64 nodes, `relu` activation
2. Two hidden layers with 32 and 16 nodes, respectively, with `relu` activation
3. Output layer with `softmax` activation for multi-class classification


