import streamlit as st
import pandas as pd
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
import pickle
# #Loading up the Regression model we created
model = xgb.XGBClassifier()


#Caching the model for faster loading

from PIL import Image

load the model from disk
model = pickle.load(open('model.pkl','rb'))
#Import python scripts

city_mapping = {'Male': 1, 'Female': 0, 'Los Angeles': 2, 'New York': 4, 'Miami': 3, 'Chicago': 0, 'Houston': 1}
def main():
    #Setting Application title
    st.title('Customer Churn Prediction App')

      #Setting Application description
    st.markdown("""
     :dart:  This Streamlit app is made to predict customer churn based on historical customer data.
    The application is functional for  online prediction .
    """)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    #Setting Application sidebar default
    image = Image.open('app.jpg')
    st.sidebar.info('This app is created to predict Customer Churn of data services by Garvit Jain')
    st.sidebar.image(image)

    st.info("Input data below")
    #Based on our optimal features selection
    st.subheader("Customer information")
    gender = st.selectbox('Gender:', ('Male', 'Female'))
    age = st.slider('Age of Customer', min_value=18, max_value=70, value=18)
    location = st.selectbox('Location:', ('Los Angeles' ,'New York' ,'Miami' ,'Chicago' ,'Houston'))
    st.subheader("Subscription data")
    tenure = st.slider('Number of months the customer has stayed with the company', min_value=1, max_value=24, value=1)
    monthlycharges = st.number_input('The amount charged to the customer monthly', min_value=30, max_value=100, value=30)
    totalusage = st.number_input('The total amount of data used by customer in GB',min_value=50, max_value=500, value=50)

    data = {'Age': (age - 18)/52,
            'Gender': city_mapping[gender],
            'Location': city_mapping[location],
            'Subscription_Length_Months':(tenure -1)/23,
            'Monthly_Bill': (monthlycharges - 30)/70,
            'Total_Usage_GB': (totalusage - 50)/500
                }
    features_df = pd.DataFrame.from_dict([data])
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    
    #Preprocess inputs


    prediction = model.predict(features_df)

    if st.button('Predict'):
            if prediction == 1:
                st.warning('Yes, the customer will terminate the service.')
            else:
                st.success('No, the customer is happy with  data Services.')

if __name__ == '__main__':
        main()
