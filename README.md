# Loan Risk Prediction Application

## Introduction
The **Loan Risk Prediction Application** is a machine learning-powered tool that forecasts the risk profile of loans. It enables lenders to make **data-driven decisions** by predicting whether a loan is at **risk** or **healthy** based on key financial indicators. This application simplifies the loan evaluation process, helping financial institutions minimize risks and improve decision-making.

---

## How the Model Works

### Input Variables (X)
The following variables are used to train the logistic regression model:

- **Loan Size**  
- **Interest Rate**  
- **Borrower Income**  
- **Debt-to-Income Ratio**  
- **Number of Accounts**  
- **Derogatory Marks**  
- **Total Debt**  
![model_training](https://github.com/user-attachments/assets/53eec374-945b-4e51-99b7-19c4f1a2d58a)


### Prediction Target (Y)
- **0**: Healthy Loan (Low-risk)  
- **1**: At-Risk Loan (High-risk)

---

## App Interface
The application is powered by **Gradio** to offer a **user-friendly interface** for seamless interaction.
![app_screenshot](https://github.com/user-attachments/assets/4da6b165-f58e-46ab-987e-6409fa799746)



- **User Input:** Loan officers can enter loan-specific data into the interface.
- **Real-time Prediction:** The app instantly predicts whether the loan is healthy or at risk, supporting efficient decision-making.

---

## Confusion Matrix & Classification Report
![accuracy](https://github.com/user-attachments/assets/bfca264b-37b3-4601-9b05-c9ba52ab7b71)



- **Confusion Matrix Results:**
  - **True Positives (TP):** 583 (Correctly predicted high-risk loans)  
  - **True Negatives (TN):** 18,655 (Correctly predicted healthy loans)  
  - **False Positives (FP):** 110 (Healthy loans incorrectly classified as high-risk)  
  - **False Negatives (FN):** 36 (High-risk loans incorrectly classified as healthy)  

---

## Model Evaluation Metrics

| **Metric**            | **Class 0 (Healthy Loan)** | **Class 1 (High-Risk Loan)** | **Overall**  |
|-----------------------|----------------------------|-----------------------------|--------------|
| Precision             | 1.00                       | 0.84                        | 0.99         |
| Recall                | 0.99                       | 0.94                        | 0.99         |
| F1-Score              | 1.00                       | 0.89                        | 0.99         |
| Accuracy              |                            |                             | **0.99**     |

- **Macro Average:** Precision: 0.92 | Recall: 0.97 | F1-Score: 0.94  
- **Weighted Average:** Precision: 0.99 | Recall: 0.99 | F1-Score: 0.99  

---

## Summary

The **Loan Risk Prediction Application** delivers **high accuracy (0.99)** with excellent precision and recall for healthy loans. However, there is room for improvement in **reducing false negatives** for high-risk loans to further enhance the model's precision and support better risk management.

---

## Next Steps & Improvements

- **Optimize Model Precision:** Focus on reducing false negatives to increase precision for high-risk loans.
- **Continuous Learning:** Update the model periodically with new data to maintain predictive performance.
- **Deployment & Scaling:** Scale the app to evaluate larger loan portfolios and integrate with financial institutions' systems.

---

## Screenshots

1. **Dataframe of Input Variables:**
 ![model_training](https://github.com/user-attachments/assets/dc738f7b-6211-453c-8d9f-086defca7ba3)


2. **App Interface:**
 ![app_screenshot](https://github.com/user-attachments/assets/d90c9d16-72df-4190-a2ea-6ac3185714b1)


3. **Confusion Matrix:**

![accuracy](https://github.com/user-attachments/assets/46a0e2d6-2ae0-4dee-9a2e-00a3ff20b09f)

---
