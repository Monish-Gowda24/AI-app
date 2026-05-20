import streamlit as st
import pandas as pd
from main import run_pipeline

st.title("AI Dashboard Generator")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
user_prompt = st.text_input("What dashboard do you want?")

if uploaded_file and user_prompt:
    df = pd.read_csv(uploaded_file)

    st.write("### Raw Data Preview")
    st.dataframe(df.head())

    results = run_pipeline(df, user_prompt)

    st.write("### KPIs")
    for kpi, value in results["kpis"].items():
        st.metric(kpi, value)

    st.write("### Charts")
    for chart in results["charts"]:
        st.plotly_chart(chart)

    st.write("### Insights")
    st.write(results["insights"])
