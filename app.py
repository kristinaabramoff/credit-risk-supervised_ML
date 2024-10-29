import gradio as gr
import joblib
import pandas as pd

# Load the trained Logistic Regression and XGBoost models
logistic_model = joblib.load('logistic_model.pkl')
xgb_model = joblib.load('xgboost_model.pkl')

# Load the scaler that was applied during training
scaler = joblib.load('scaler.pkl')

# Define the feature names (must match the columns used during training)
feature_names = ['loan_size', 'interest_rate', 'borrower_income', 'debt_to_income', 'num_of_accounts', 'derogatory_marks', 'total_debt']

# Define the prediction function
def predict(model_choice, loan_amount, interest_rate, borrowers_income, debt_to_income, num_of_accounts, derogatory_marks, total_debt):
    # Prepare the input data in the same format as during training
    input_data = pd.DataFrame([[loan_amount, interest_rate, borrowers_income, debt_to_income, num_of_accounts, derogatory_marks, total_debt]],
                              columns=feature_names)
    
    # Scale the input data using the saved scaler
    input_data_scaled = scaler.transform(input_data)  # Apply scaling
    
    # Select the model based on user choice
    if model_choice == "Logistic Regression":
        prediction = logistic_model.predict(input_data_scaled)
    elif model_choice == "XGBoost":
        prediction = xgb_model.predict(input_data_scaled)
    
    # Return the prediction result
    return "At Risk Loan" if prediction[0] == 1 else "Healthy Loan"

# Define input components for the Gradio interface
input_features = [
    gr.Dropdown(label="Select Model", choices=["Logistic Regression", "XGBoost"], value="Logistic Regression"),
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
    title="Loan Risk Predictor",
    description="Enter loan and financial details to predict loan risk."
)

# Launch the Gradio interface
interface.launch(share=True)
