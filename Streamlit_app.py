import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('naive_bayes_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit App Title
st.title("Fraud Detection with Naive Bayes")

# Input Form
st.header("Enter Transaction Details")
amount = st.number_input("Transaction Amount")
oldbalanceOrg = st.number_input("Original Balance Before Transaction")
newbalanceOrig = st.number_input("New Balance After Transaction")
oldbalanceDest = st.number_input("Recipient Original Balance")
newbalanceDest = st.number_input("Recipient New Balance")

# Type of Transaction Dropdown
transaction_type = st.selectbox("Transaction Type", ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])

# Button to Predict
if st.button("Predict Fraud"):
    # Prepare data for prediction (Ensure it matches your model's training format)
    input_data = pd.DataFrame({
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest],
        'type': [transaction_type]
    })

    # Perform prediction
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("Fraudulent Transaction Detected!")
    else:
        

st.success("Transaction is Not Fraudulent.")
        

