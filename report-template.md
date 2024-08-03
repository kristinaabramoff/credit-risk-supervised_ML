# Module 12 Report Template

## Overview of the Analysis

In this analysis, we evaluated the performance of a logistic regression model used for predicting loan risk. The goal was to assess how well the model identifies healthy loans versus high-risk loans to aid in financial decision-making.

* Purpose of the Analysis: To evaluate the performance of a logistic regression model in classifying loans as either healthy or high-risk.
* Data Description: The dataset includes loan information where each loan is labeled as either 0 (healthy loan) or 1 (high-risk loan). We aimed to predict these labels based on various financial features.
* Variables: The variables to predict are value_counts of labels 0 and 1.

* Machine Learning Process:
Data Preparation: Cleaned and preprocessed the data.
Model Training: Used the LogisticRegression algorithm to train the model.
Model Evaluation: Assessed model performance using a confusion matrix and classification report.
## Results

Machine Learning Model: Logistic Regression

Confusion Matrix:

True Positives (TP) for High-Risk Loans: 583
True Negatives (TN) for Healthy Loans: 18,655
False Positives (FP) for High-Risk Loans: 110
False Negatives (FN) for High-Risk Loans: 36
Classification Report:

Class 0 (Healthy Loan):
Precision: 1.00
Recall: 0.99
F1-Score: 1.00
Support: 18,765
Class 1 (High-Risk Loan):
Precision: 0.84
Recall: 0.94
F1-Score: 0.89
Support: 619
Accuracy: 0.99
Macro Average:
Precision: 0.92
Recall: 0.97
F1-Score: 0.94
Weighted Average:
Precision: 0.99
Recall: 0.99
F1-Score: 0.99

## Summary

* Best Performing Model: The logistic regression model performs well with an overall accuracy of 0.99 and high precision and recall for healthy loans (Class 0). The model is effective in correctly identifying healthy loans with a precision of 1.00 and a recall of 0.99.

* Performance Importance: Identifying high-risk loans (Class 1) is critical for managing financial risk. While the model has a high recall of 0.94 for high-risk loans, the precision is lower at 0.84. This means that some high-risk loans are incorrectly classified as healthy (false negatives), which could lead to financial losses. Although the model effectively identifies most high-risk loans, the presence of 36 false negatives is a concern.

* Recommendation: Despite the strong overall performance, the lower precision for high-risk loans and the presence of false negatives highlight a need for model improvement. Reducing false negatives is crucial for better risk management. Enhancing the model to increase precision for high-risk loans would make it more reliable for identifying and managing high-risk situations. Therefore, while the model is currently effective, further tuning is recommended to improve its performance in high-risk loan detection.
