# SmartLoanPredictor

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-green?logo=streamlit&logoColor=white)](https://smartloanpredictor.streamlit.app)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  

---

## Introduction

**SmartLoanPredictor** is a Streamlit application designed to predict **loan default risk** for financial institutions.  

The app uses **customer behavioral and financial information** to:  
- Predict **loan default risk (Yes/No)**  
- Show **probability of default** via a visual probability plot  
- Provide a **client summary** for easier interpretation  

Interactive, **color-coded results** help lenders make informed decisions quickly:  
- Red = Default / High Risk  
- Green = Non-default / Low Risk  

---

## Dataset Definition

Three datasets were merged for analysis:  

1. **Performance Dataset:** Loan outcomes (repaid vs defaulted)  
2. **Demographic Dataset:** Customer characteristics  
3. **Previous Loan Dataset:** Historical loans per customer  

**Target Variable:**  
- `loan_default` → Binary outcome:  
  - 1 = Default  
  - 0 = Non-default  

**Features:**

**Numeric Columns (`num_cols`):**  
- `loannumber`, `loanamount`, `termdays`, `monthly_payment`, `debt_to_income_ratio`, `loan_to_income_ratio`, `approval_lag_days`, `first_payment_delay_days`, `past_due_days`, `loan_age_days`, `early_payment_flag`, `credit_score`, `age`  

**Categorical Columns (`cat_cols`):**  
- `bank_account_type`  
- `bank_name_clients`  
- `employment_status_clients`  

---

## 1. Exploratory Data Analysis (EDA)

- **Distribution Analysis:** Visualized numeric features (`loanamount`, `credit_score`, `monthly_payment`, `repayment delays`, `loan_age_days`) using:  
  - **Histograms** → raw frequency distributions  
  - **Box plots** → identify spread, quartiles, and outliers  
  - **Violin plots** → distribution + summary statistics  

- **Correlation Analysis:** Identified strongest predictors of default.  
- **Class Imbalance:** More non-default cases; applied **SMOTE** for balancing.  
- **Outliers & Skewness:**  
  - Outliers treated using **Winsorization/Capping**  
  - Highly skewed features transformed using **log transformation**  

---

## 2. Data Preprocessing & Feature Engineering

- **Missing Values:**  
  - Numeric → Mean/Median  
  - Categorical → Mode or “Unknown”  

- **Feature Engineering:**  
  - Debt-to-Income Ratio (DTI)  
  - Outstanding ratio  
  - High-risk flag  
  - Approval lag / Processing time  
  - First payment lag  
  - Past due days  
  - Loan age days  
  - Early payment flag  
  - Risk score  
  - Credit score  

- **Encoding & Scaling:**  
  - Categorical → One-Hot Encoding  
  - Numeric → StandardScaler  
  - Target → Label Encoding  

---

## 3. Train-Test Split

- Features (`X`) and target (`y`) separated.  
- Split into **training (80%)** and **testing (20%)** sets.  

---

## 4. Model Selection & Evaluation

- Models tested: **Logistic Regression, Random Forest, Gradient Boosting, XGBoost, AdaBoost**  
- Metrics: **Accuracy, Precision, Recall, F1-score, ROC-AUC, Confusion Matrix**  

---

## 5. Hyperparameter Tuning

- Optimized model parameters using **GridSearchCV**  
- Adjusted classification thresholds for **better Recall, F1-score, and ROC-AUC**  
- Selected **AdaBoost** as the best model  

---

## 6. Feature Importance & Interpretation

- Important features guide business insights:  
  - Loan amount, risk score, credit score, approval lag days, past due days, etc.  

---

## 7. Final Model & Deployment

- **Model:** AdaBoost  
  - Optimized for **Recall** & **ROC-AUC**  
  - Effective in identifying potential defaulters  

- **Deployment:** Streamlit app with:  
  - **Sidebar:** Client inputs (numeric + categorical) + About App  
  - **Main Page:** Introduction, Verify Client Details, Prediction, Client Summary, Probability Plot  
  - **Color-coded results:** Red = Default, Green = Non-default  

- **Live App:** [smartloanpredictor.streamlit.app](https://smartloanpredictor.streamlit.app)
