# Diabetes Prediction Model and App

Welcome to this repository which will contain summative tasks for my ML Specialization. This repository contains a summative folder that holds Three Folders: a machine learning api that predicts diabetes using datasets from scikit-learn, a Flutter app that uses the api to predict diabetes and a folder for the Colab Notebooks on Univariate linear regression and multi-variate linear regression. 

## Screenshot of the Diabetes Prediction Flutter App

![app-photo](https://github.com/user-attachments/assets/84bb7c3d-c286-4cad-9600-d6f75b4e06f9)

## Table of Contents

- [Screenshots](#Screenshot-of-the-Diabetes-Prediction-Flutter App)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Model Overview](#model-overview)
- [Flutter App Overview](#The-flutter-app)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Repository Structure

The repository is structured as follows:
- `summative/` : This is the folder that holds the three below folders:
- `diabetes_app/`: Contains the Flutter app files.
- `fastapi/`: Contains the files related to the machine learning model, including the file used for training the model and the requirements file for dependencies.
- `linear_regression/`: Contains the Univariate and multi-variate files.

## Requirements

To install the necessary dependencies for the machine learning model, navigate to the `fastapi/` directory and use the following command:

- pip install -r requirements.txt

- python run predict.py
- The model will be saved as a .joblib file

## Set up and Installation

After setting up the Backend, run fastapi run dev main to take you to a local host.
Navigate to /docs/predict and try out the end point

cd ..
cd into fastapi
run `flutter run` to build the Flutter project.

## Model Overview
This `diabetes` machine learning model predicts diabetes progression based on 10 medical features such as age, BMI, and blood pressure. It uses a linear regression algorithm to make the predictions. The model was trained using the scikit-learn `load_diabetes` dataset and is deployed as an API endpoint on Render.com. (https://linear-regression-b45r.onrender.com)

## The Flutter App
The Flutter app interacts with the deployed model through an HTTP POST request. Users input their medical data, including features like age, BMI, and blood pressure. The app sends these inputs to the model's endpoint, which then returns the predicted diabetes progression, displayed in the app. The app offers an intuitive interface for predicting diabetes progression. Users input their medical data, and with a button click, receive predictions about diabetes risk.

Endpoint
- The  deployed on rendee API endpoint for the model is: `https://linear-regression-b45r.onrender.com/predict`

Testing

You can test the API paltforms using Postman. Create a POST request, enter the URL above. In the body, select raw and JSON and enter the JSON object: { "features": [22.0, 33.0, 21.0, 44.0, 29.0, 45.0, 21.0, 99.0, 35.0, 21.0] } The response should be something like: { "prediction": 73467.34487944 }

### Key Features
- Input fields for Age, BMI, Glucose Level, Blood Pressure, Total Cholesterol, Insulin, Triglycerides Level, High-Density Lipoproteins, Low-Density Lipoproteins, and Creatinine.
- Button to trigger diabetes risk prediction.
- Display of predicted diabetes risk level.

## Demo Video
Here's the demo video:

#  Contributor:

- 



