import requests
import random
import time

API_URL = "http://127.0.0.1:8000/telemetry"

while True:

    workflow_id = "wf-001"

    tokens = random.randint(1000, 3000)

    cost_usd = round(
        tokens * 0.000002,
        5
    )

    payload = {
        "agent_name": "coder-agent",
        "event_type": "coding",
        "latency": round(random.uniform(1.0, 4.0), 2),
        "tokens": tokens,
        "cost_usd": cost_usd,
        "workflow_id": workflow_id,
        "status": "success",
        "message": "Code generated"
    }

    response = requests.post(API_URL, json=payload)

    print("Coder:", response.json())

    time.sleep(5)