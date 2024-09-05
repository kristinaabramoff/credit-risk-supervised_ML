import gradio as gr
import numpy as np
import joblib
import pandas as pd

# Load the trained model
classifier = joblib.load('logistic_model.pkl')

# Define the feature names (these must match the column names used during training)
feature_names = ['loan_size', 'interest_rate', 'borrower_income', 'debt_to_income', 'num_of_accounts', 'derogatory_marks', 'total_debt']


# Define the prediction function
def predict(loan_amount, interest_rate, borrowers_income, debt_to_income, num_of_accounts, derogatory_marks, total_debt):
    input_data = pd.DataFrame([[loan_amount, interest_rate, borrowers_income, debt_to_income, num_of_accounts, derogatory_marks, total_debt]], 
                              columns=feature_names)  # Use a DataFrame with the same feature names
    prediction = classifier.predict(input_data)
    return "At Risk Loan" if prediction[0] == 1 else "Healthy Loan"

# Define input components for the Gradio interface using the updated syntax
input_features = [
    gr.Number(label="Loan Amount"),
    gr.Number(label="Interest Rate"),
    gr.Number(label="Borrowers Income (Annual)"),
    gr.Number(label="Debt-to-Income Ratio"),
    gr.Number(label="Number of Accounts"),
    gr.Number(label="Derogatory Marks (0 or 1)"),
    gr.Number(label="Total Debt")
]

# Create the Gradio interface
interface = gr.Interface(
    fn=predict, 
    inputs=input_features, 
    outputs="text",
    title="Logistic Regression Loan Predictor",
    description="Enter the loan and financial details to get a prediction on the loan's risk."
)

# Launch the interface with the option to share publicly
interface.launch(share=True)

