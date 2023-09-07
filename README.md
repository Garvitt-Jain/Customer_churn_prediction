# Customer_churn_prediction
Enhancing Customer Retention: Exploring  Machine Learning and Deep Learning Models with Optimized Hyperparameters for Churn Prediction

Customer Churn Prediction Project Overview:

Project Demo Link: https://customerchurnpredictiongarvitjain.streamlit.app/

Understanding Churn:

Churn prediction involves identifying customers who are likely to cancel their subscription or service based on their usage patterns. This prediction is crucial for businesses as acquiring new customers is often more expensive than retaining existing ones. Once you can pinpoint customers at risk of leaving, you can take tailored marketing actions to maximize the chances of retaining them.

Importance of Churn Prediction:

Customer churn is a widespread challenge across various industries. To grow as a company, you must continuously invest in acquiring new customers. When a customer leaves, it represents a significant loss in terms of time and resources invested in acquiring and servicing them. Predicting when a customer is likely to leave and offering incentives to retain them can result in substantial cost savings for a business.

Project Highlights:

In our dataset, we have about 49.5% of people who churned. Therefore, it's crucial to predict which customers are likely to churn, as this information is vital for both acquiring new customers and retaining existing ones.

Steps in Model Deployment:

Data Analysis (EDA): Exploratory Data Analysis to understand the dataset. Understanding the distribution of data.

Data Preprocessing: Preparing the data for analysis and modelling. Encoding categorical variables, Outlier detection and  correction,

Feature Engineering: Creating new features or modifying existing ones for better model performance. Doing Min_Max scaling

Algorithm Selection: Using Machine Learning algorithms for prediction.

Hyperparameter Tuning (RandomSearchCV): Fine-tuning model hyperparameters for optimal performance.
Applying Deep Learning models and hyperparameter  tuning using various regularization techniques,Batch normalization,Early Stopping etc. 

Model Saving: Saving the best-trained model using Pickle.

Web Application Creation with Streamlit: Developing a web application for ease of use.

Deployment on Streamlit community cloud: Deploy the application on the community cloud platform for accessibility.

Packages Used:

This project relies on Python and the following packages:

Numpy
Pandas
Matplotlib
Seaborn
Scikit-learn
Scipy
tensorflow
keras
keras-tuner
Streamlit
How to Run:

To run the project, follow these steps:

Download the dataset 'customer_churn_large_dataset.xlsx'.
Open The file in Google Collab
import or install the necessary packages.
Download the 'app.py' files.
Execute 'Customer_churn.ipynb'.
Provide inputs to assess the model's accuracy in predicting customer churn.
Objective:

The primary objective of this project is to predict whether a customer is likely to churn or not. This prediction is achieved using a Hyperparameter tuned  XG Boost Classifier.

Project Demo Link: Click Here
