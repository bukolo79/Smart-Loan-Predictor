# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 23:33:56 2025

@author: Oluwaseun Adeyemi
"""

import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# ---------------------- Load Model ----------------------
model = joblib.load("adaboost_pipeline.pkl")

# ---------------------- Page Config ----------------------
st.set_page_config(page_title="Loan Default Prediction App", layout="wide", page_icon="💳")

# ---------------------- Custom CSS ----------------------
st.markdown("""
<style>
body { background-color: #f9f9f9; font-family: 'Segoe UI', sans-serif; }
h1, h2, h3 { color: #2E86C1; }
/* Buttons */
.stButton>button { border-radius:12px; height:3em; width:100%; font-size:16px; font-weight:bold;
                   background: linear-gradient(to right, #2E86C1, #3498DB); color:white; border:none; }
.stButton>button:hover { background: linear-gradient(to right, #117A65, #1ABC9C); color:white; }
/* Result Box */
.result-box { padding:25px; border-radius:12px; text-align:center; font-size:28px; font-weight:bold; margin-top:20px; }
/* Client Summary Card */
.summary-card { padding:15px; border-radius:12px; background-color:#f1f8ff; margin-top:20px; box-shadow:0px 4px 8px rgba(0,0,0,0.1);}
/* Reduce top margin of main page */
.block-container { padding-top: 1rem; padding-left: 2rem; padding-right: 2rem; }
</style>
""", unsafe_allow_html=True)

# ---------------------- Sidebar ----------------------
st.sidebar.title("👤 Client Inputs")

# Sidebar About the App
st.sidebar.markdown("""
### ℹ️ About This App
This application helps financial institutions **assess loan risk efficiently** using key customer behavioral and financial features.  

It delivers **instant, actionable insights** to guide lending decisions and reduce potential financial losses.  

**Model predicts risk of default (Yes/No)**.
""")

# Numeric Inputs
with st.sidebar.expander("🔢 Numeric Features", expanded=True):
    loannumber = st.number_input("Loan Number", min_value=0, step=1)
    loanamount = st.number_input("Loan Amount", min_value=0.0, step=100.0)
    termdays = st.number_input("Loan Term (days)", min_value=0, step=1)
    monthly_payment = st.number_input("Monthly Payment", min_value=0.0, step=10.0)
    debt_to_income_ratio = st.number_input("Debt-to-Income Ratio", min_value=0.0, step=0.01)
    loan_to_income_ratio = st.number_input("Loan-to-Income Ratio", min_value=0.0, step=0.01)
    approval_lag_days = st.number_input("Approval Lag (days)", min_value=0, step=1)
    first_payment_delay_days = st.number_input("First Payment Delay (days)", min_value=0, step=1)
    past_due_days = st.number_input("Past Due Days", min_value=0, step=1)
    loan_age_days = st.number_input("Loan Age (days)", min_value=0, step=1)
    early_payment_flag = st.selectbox("Early Payment Flag", [0, 1])
    credit_score = st.number_input("Credit Score", min_value=0, step=1)
    age = st.number_input("Age", min_value=18, max_value=100, step=1)

# Categorical Inputs
with st.sidebar.expander("🏦 Categorical Features", expanded=True):
    bank_account_type = st.selectbox("Bank Account Type", ["Current", "Other", "Savings"])
    bank_name_clients = st.selectbox(
        "Bank Name",
        ["Access Bank", "Diamond Bank", "Ecobank", "FCMB", "Fidelity Bank", "First Bank", "GT Bank",
         "Heritage Bank", "Keystone Bank", "Skye Bank", "Stanbic IBTC", "Standard Chartered",
         "Sterling Bank", "UBA", "Union Bank", "Unity Bank", "Wema Bank", "Zenith Bank"]
    )
    employment_status_clients = st.selectbox(
        "Employment Status",
        ["Contract", "Permanent", "Retired", "Self Employed", "Student", "Unemployed", "Unknown"]
    )

# Sidebar Prediction Button
if st.sidebar.button("🔮 Predict Loan Default Risk", key="sidebar_predict"):
    st.session_state['predict'] = True
else:
    if 'predict' not in st.session_state:
        st.session_state['predict'] = False

# ---------------------- Main Page ----------------------
st.title("💳 Loan Default Prediction App")

# Main Page Introduction
st.markdown("""
### Welcome!
Use this application to **predict the risk of loan default** based on client behavioral and financial data.  

Powered by **machine learning**, it provides **quick, reliable, and actionable insights** to help lenders make confident decisions while minimizing potential losses.
""")

# Verify client details message immediately after introduction
st.info("⚠️ Please verify the client details below before making a prediction.")

# Store client data
client_data = {
    "loannumber": loannumber, "loanamount": loanamount, "termdays": termdays,
    "monthly_payment": monthly_payment, "debt_to_income_ratio": debt_to_income_ratio,
    "loan_to_income_ratio": loan_to_income_ratio, "approval_lag_days": approval_lag_days,
    "first_payment_delay_days": first_payment_delay_days, "past_due_days": past_due_days,
    "loan_age_days": loan_age_days, "early_payment_flag": early_payment_flag,
    "credit_score": credit_score, "age": age, "bank_account_type": bank_account_type,
    "bank_name_clients": bank_name_clients, "employment_status_clients": employment_status_clients
}
st.session_state["client_data"] = client_data

# Tabs for Client Summary and Prediction
tab1, tab2 = st.tabs(["📋 Client Summary", "📊 Prediction"])

# ---------------------- Client Summary ----------------------
with tab1:
    st.subheader("📋 Client Summary")
    client_df = pd.DataFrame([st.session_state["client_data"]])
    st.markdown('<div class="summary-card">', unsafe_allow_html=True)
    st.dataframe(client_df.T.rename(columns={0:"Value"}))
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------- Prediction ----------------------
with tab2:
    st.subheader("📊 Loan Default Risk Prediction")
    input_data = pd.DataFrame([st.session_state["client_data"]])

    if st.session_state['predict'] or st.button("🔮 Predict Loan Default Risk", key="main_predict"):
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        # Color-coded result with Yes/No
        if prediction == 1:
            st.markdown(
                f"<div class='result-box' style='background-color:#F1948A; color:white;'>"
                f"🚨 Prediction: Yes (Default)<br>Probability: {probability:.2%}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='result-box' style='background-color:#58D68D; color:white;'>"
                f"✅ Prediction: No (Non-Default)<br>Probability: {probability:.2%}</div>",
                unsafe_allow_html=True
            )

        # Probability Bar Plot
        fig = go.Figure(go.Bar(
            x=["Non-Default", "Default"],
            y=[1-probability, probability],
            marker_color=["#58D68D", "#F1948A"]
        ))
        fig.update_layout(
            title="Probability Distribution",
            yaxis_title="Probability",
            xaxis_title="Outcome",
            plot_bgcolor="#f9f9f9"
        )
        st.plotly_chart(fig, use_container_width=True)
