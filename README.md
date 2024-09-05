# Loan Risk Prediction Application

## About the Application

The **Loan Risk Prediction Application** is a machine learning-based tool designed to predict the likelihood of a loan being at risk or healthy. It employs a logistic regression model to assess the loan's risk profile based on critical financial indicators, enabling financial institutions, loan officers, and decision-makers to make more informed lending decisions. The app simplifies and streamlines the process of assessing loan risk using key financial metrics.

### Key Features:
- **Data Cleaning & Preprocessing**: The app handles missing data, normalizes input features, and converts categorical variables into numerical values to ensure model accuracy.
- **Feature Engineering**: The logistic regression model uses carefully selected financial features, including loan size, interest rate, borrower income, debt-to-income ratio, number of accounts, derogatory marks, and total debt.
- **Machine Learning**: The app is powered by a LogisticRegression model, optimized and evaluated with metrics like precision, recall, and F1-score to predict loan risk.
- **User-Friendly Interface**: The Gradio interface allows users to input loan details quickly and receive instant predictions on whether a loan is healthy or at risk.

### How It Works:
- **Healthy Loan (0)**: Represents a low-risk loan where the borrower is likely to meet repayment obligations.
- **At Risk Loan (1)**: Represents a higher-risk loan where the borrower may struggle to meet their financial commitments.

Users can input financial details such as loan size, borrower income, interest rate, and other key variables into the application. Based on these inputs, the app provides a prediction, helping financial institutions make well-informed decisions regarding loan approvals and risk management.

---

## Results

The model's performance is based on a logistic regression algorithm, evaluated using a confusion matrix and classification metrics:

**Confusion Matrix:**
- **True Positives (TP)**: 583 (Correctly predicted high-risk loans)
- **True Negatives (TN)**: 18,655 (Correctly predicted healthy loans)
- **False Positives (FP)**: 110 (Healthy loans predicted as high-risk)
- **False Negatives (FN)**: 36 (High-risk loans predicted as healthy)

### Classification Report:
**Class 0 (Healthy Loan)**:
- **Precision**: 1.00
- **Recall**: 0.99
- **F1-Score**: 1.00
- **Support**: 18,765 instances

**Class 1 (High-Risk Loan)**:
- **Precision**: 0.84
- **Recall**: 0.94
- **F1-Score**: 0.89
- **Support**: 619 instances

**Overall Metrics**:
- **Accuracy**: 0.99
- **Macro Average**:
  - Precision: 0.92
  - Recall: 0.97
  - F1-Score: 0.94
- **Weighted Average**:
  - Precision: 0.99
  - Recall: 0.99
  - F1-Score: 0.99

---

## Summary

**Best Performing Model**: The logistic regression model delivers a high overall accuracy of 0.99, with particularly strong performance in identifying healthy loans (Class 0). It achieves perfect precision and near-perfect recall for healthy loans, making it highly reliable for low-risk predictions.

**Performance Importance**: The model's ability to identify high-risk loans (Class 1) is crucial for mitigating financial risks. While the recall for high-risk loans is strong at 0.94, the precision for this class is lower at 0.84. This suggests that some high-risk loans are incorrectly classified as healthy (36 false negatives), which could pose a risk to lenders.

**Recommendation**: Although the model performs well overall, there is room for improvement in reducing false negatives, which would enhance its precision in detecting high-risk loans. Future iterations of the model should focus on increasing precision for high-risk loans to improve risk management and financial decision-making.
