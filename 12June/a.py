import joblib
import streamlit as st

# Load the logistic regression model
a = joblib.load('job')

# Set the title of the app
st.title('Logistic Regression')

# Get user input
x = st.number_input('Enter a height in cm')

# Define the prediction function
def test(x):
    y = a.predict([[x]])
    if y == 1:
        return 'Male'
    else:
        return 'Female'

# Trigger prediction on button press
if st.button('Predict'):
    result = test(x)
    st.write(result)
