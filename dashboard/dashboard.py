# import streamlit as st
# import pandas as pd
# import requests

# API_URL = "http://127.0.0.1:8000/events"

# st.title("BYOX Agent Telemetry Dashboard")

# response = requests.get(API_URL)

# data = response.json()

# df = pd.DataFrame(data)

# st.dataframe(df)

# if not df.empty:

#     st.subheader("Latency")

#     st.line_chart(df["latency"])

#     st.subheader("Tokens")

#     st.bar_chart(df["tokens"])


import streamlit as st
import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000/events"

st.title("Agent Telemetry Dashboard")

response = requests.get(API_URL)

data = response.json()

df = pd.DataFrame(data)

if not df.empty:

    st.subheader("All Events")

    st.dataframe(df)

    st.subheader("Events Per Agent")

    agent_counts = (
        df["agent_name"]
        .value_counts()
    )

    st.bar_chart(agent_counts)

    st.subheader("Average Latency")

    latency_df = (
        df.groupby("agent_name")["latency"]
        .mean()
    )

    st.bar_chart(latency_df)

else:
    st.write("No data found")