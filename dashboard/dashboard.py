import streamlit as st
import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000/events"

st.set_page_config(
    page_title="BYOX Agent Telemetry",
    layout="wide"
)

st.title("🚀 BYOX Agent Telemetry Dashboard")

response = requests.get(API_URL)

data = response.json()

df = pd.DataFrame(data)

if not df.empty:

    # ==========================
    # TOP METRICS
    # ==========================

    total_events = len(df)

    total_tokens = df["tokens"].sum()

    total_cost = df["cost_usd"].sum()

    avg_latency = round(
        df["latency"].mean(),
        2
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Events",
        total_events
    )

    col2.metric(
        "Tokens",
        int(total_tokens)
    )

    col3.metric(
        "Cost (USD)",
        f"${total_cost:.4f}"
    )

    col4.metric(
        "Avg Latency",
        avg_latency
    )

    st.divider()

    # ==========================
    # ALL EVENTS
    # ==========================

    st.subheader("All Events")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    # ==========================
    # EVENTS PER AGENT
    # ==========================

    st.subheader("Events Per Agent")

    agent_counts = (
        df["agent_name"]
        .value_counts()
    )

    st.bar_chart(agent_counts)

    st.divider()

    # ==========================
    # LATENCY PER AGENT
    # ==========================

    st.subheader("Average Latency Per Agent")

    latency_df = (
        df.groupby("agent_name")["latency"]
        .mean()
    )

    st.bar_chart(latency_df)

    st.divider()

    # ==========================
    # COST PER AGENT
    # ==========================

    st.subheader("Cost By Agent")

    cost_df = (
        df.groupby("agent_name")["cost_usd"]
        .sum()
    )

    st.bar_chart(cost_df)

    st.divider()

    # ==========================
    # TOP SPENDER
    # ==========================

    top_agent = cost_df.idxmax()

    top_cost = cost_df.max()

    st.success(
        f"Top Spending Agent: {top_agent} (${top_cost:.4f})"
    )

    st.divider()

    # ==========================
    # WORKFLOW ACTIVITY
    # ==========================

    st.subheader("Workflow Activity")

    workflow_counts = (
        df["workflow_id"]
        .value_counts()
    )

    st.bar_chart(workflow_counts)

    st.divider()

    # ==========================
    # WORKFLOW SELECTOR
    # ==========================

    workflow_list = sorted(
        df["workflow_id"].unique()
    )

    selected_workflow = st.selectbox(
        "Select Workflow",
        workflow_list
    )

    workflow_df = df[
        df["workflow_id"] == selected_workflow
    ]

    st.subheader(
        f"Workflow Details: {selected_workflow}"
    )

    st.dataframe(
        workflow_df[
            [
                "agent_name",
                "event_type",
                "latency",
                "tokens",
                "cost_usd",
                "status"
            ]
        ],
        use_container_width=True
    )

    # ==========================
    # WORKFLOW SUMMARY
    # ==========================

    workflow_cost = workflow_df["cost_usd"].sum()

    workflow_tokens = workflow_df["tokens"].sum()

    workflow_latency = round(
        workflow_df["latency"].mean(),
        2
    )

    st.subheader("Workflow Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Workflow Cost",
        f"${workflow_cost:.4f}"
    )

    c2.metric(
        "Workflow Tokens",
        int(workflow_tokens)
    )

    c3.metric(
        "Avg Workflow Latency",
        workflow_latency
    )

else:
    st.warning("No telemetry data found.")