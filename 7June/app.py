import joblib 
import streamlit as st;
import pandas as pd

model = joblib.load('model_joblib')

st.title("House Price Prediction")

area = st.number_input("Enter the Area")

def prediction(area):
    prediction = model.predict([[area]])
    return prediction

if(st.button("Predict")):
    result = prediction(area)  
    st.success("The Predicted price is {}".format(result))