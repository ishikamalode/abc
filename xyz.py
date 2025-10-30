import streamlit as st
import pandas as pd

st.set_page_config(page_title="Investment Asset Classes", layout="wide")

# Low risk asset table data
low_risk_data = [
    ["Savings Account", "Very Low", "2–4%", "0–1 year", "5–10%"],
    ["Bank Fixed Deposit (FD)", "Low", "5–7%", "1–5 years", "10–20%"],
    ["Recurring Deposit (RD)", "Low", "5–7%", "1–3 years", "5–10%"],
    ["Treasury Bills (T-Bills)", "Very Low", "6–7%", "3–12 months", "5–10%"],
    ["Government Bonds (G-Secs)", "Very Low", "6–8%", "3–10 years", "10–20%"],
    ["RBI Floating Rate Bonds", "Very Low", "~7–8%", "5–7 years", "5–10%"],
    ["Post Office MIS", "Very Low", "6–8%", "5 years", "3–8%"],
    ["Public Provident Fund (PPF)", "Very Low", "7–8%", "15 years", "5–10%"],
    ["Employees Provident Fund (EPF)", "Very Low", "~8%", "Long term", "5–10%"],
    ["Sukanya Samriddhi Yojana", "Very Low", "~8%", "15–21 years", "3–5% (if applicable)"],
    ["Senior Citizen Savings Scheme", "Very Low", "~8%", "5 years", "5–15% (if applicable)"],
    ["Short-Term Debt Mutual Funds", "Low", "5–7%", "6–36 months", "5–10%"],
    ["Overnight / Liquid Mutual Funds", "Very Low", "4–6%", "1–6 months", "5–10%"],
    ["Ultra-Short Term Debt Funds", "Low", "5–7%", "3–12 months", "5–10%"],
    ["Sovereign Gold Bonds (SGBs)", "Low", "2.5% + gold returns", "5–8 years", "5–10%"],
    ["Life Insurance Endowment Policies", "Low", "4–6%", "10–20 years", "3–5%"]
]

columns = ["Asset Class", "Risk Level", "Expected Return", "Ideal Time Horizon", "Suggested Allocation %"]
df_low = pd.DataFrame(low_risk_data, columns=columns)

# UI
st.title("Investment Asset Class Dashboard")

risk_type = st.selectbox("Select Risk Category", ["Low Risk"], index=0)

if risk_type == "Low Risk":
    st.subheader("Low Risk Investment Options")
    st.dataframe(df_low, use_container_width=True)

st.write("This Streamlit app displays low-risk investment asset classes. Future versions will include mid and high risk options.")
