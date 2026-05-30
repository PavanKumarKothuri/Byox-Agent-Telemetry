import streamlit as st
import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000/events"

st.title("BYOX Agent Telemetry Dashboard")

response = requests.get(API_URL)

data = response.json()

df = pd.DataFrame(data)

st.dataframe(df)

if not df.empty:

    st.subheader("Latency")

    st.line_chart(df["latency"])

    st.subheader("Tokens")

    st.bar_chart(df["tokens"])