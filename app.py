import numpy as np
import pickle
import streamlit as st
# loading the saved model
loaded_model = pickle.load(open('model.pkl', 'rb'))
# creating a function for Prediction
def prediction(input_data):
        # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The Transaction is not Fraud'
    else:
      return 'The Transaction is  Fraud'
def main():
    
    
    # giving a title
    st.title('Credit Card Fraud Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Unnamed = st.text_input('Unnamed')
    cc_num = st.text_input('Credit Card No.')
    category = st.text_input('Category')
    amt = st.text_input('Amount')
    gender= st.text_input('Gender')
    zip = st.text_input('Zip Code')
    lat = st.text_input('Lattitude')
    long=st.text_input('Longitude')
    city_pop = st.text_input('City Population')
    unix_time = st.text_input('Unix Time')
    merch_lat = st.text_input('Merchant Latitude')
    merch_long= st.text_input('Merchant Longitude')
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Fraud Result'):
        diagnosis = prediction([Unnamed, cc_num, category, amt, gender, zip, lat,
        long, city_pop, unix_time, merch_lat, merch_long])
       
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()