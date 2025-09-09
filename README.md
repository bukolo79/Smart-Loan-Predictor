# 🤖 Smart Loan Predictor (Python + Streamlit)

## 🔹 Introduction
**Smart Loan Predictor** is a Streamlit app designed to predict loan default risk.  
It uses customer behaviour and financial attributes to:  
- Predict loan default (Yes/No)  
- Show default probability via a visual probability plot  
- Provide client summaries for decision support  


## 📂 Dataset Definition
Datasets merged:  
- **Performance Dataset** → Loan outcomes (default vs repaid)  
- **Demographic Dataset** → Customer characteristics  
- **Previous Loan Dataset** → Loan history  

**Target Variable:**  
- `loan_default` → (1 = Default, 0 = Non-default)  

**Features:**  
- *Numeric:* loanamount, termdays, monthly_payment, credit_score, debt_to_income_ratio, risk_score, etc.  
- *Categorical:* bank_account_type, bank_name_clients, employment_status_clients  


## 🔎 Workflow
### 1. Exploratory Data Analysis (EDA)
- Histograms, box plots, violin plots → numeric distributions  
- Correlation analysis → strongest predictors  
- SMOTE applied for class imbalance  
- Outliers treated (winsorization/log transformation)  

### 2. Data Preprocessing & Feature Engineering
- Missing values handled (mean/median/mode)  
- Features engineered: DTI, outstanding ratio, risk score, lag features, flags  
- One-hot encoding + StandardScaler  

### 3. Modeling
- Models tested: Logistic Regression, RF, XGBoost, Gradient Boosting, AdaBoost  
- Metrics: Accuracy, Precision, Recall, F1, ROC-AUC  
- **Best Model:** AdaBoost (optimized via GridSearchCV)  

### 4. Deployment
- **Streamlit App Features**:  
  - Sidebar: client inputs + About App  
  - Main Page: Prediction, Probability Plot, Client Summary  
  - Color-coded results (Red = High Risk, Green = Low Risk)
    

## 🚀 Live Demo
👉 https://smart-loan-predictor.streamlit.app/
