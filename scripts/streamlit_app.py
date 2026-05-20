import streamlit as st
import pandas as pd
from run_backtest import run_backtest

st.title("Systematic Trading Dashboard")

uploaded_file = st.file_uploader("Upload CSV")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    df, equity = run_backtest(df)

    st.line_chart(equity)
    st.write(df.tail())
