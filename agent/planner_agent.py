import requests
import random
import time

API_URL = "http://127.0.0.1:8000/telemetry"

while True:

    workflow_id = "wf-001"

    tokens = random.randint(100, 1000)

    cost_usd = round(
        tokens * 0.000002,
        5
    )

    payload = {
        "agent_name": "planner-agent",
        "event_type": "planning",
        "latency": round(random.uniform(0.5, 2.0), 2),
        "tokens": tokens,
        "cost_usd": cost_usd,
        "workflow_id": workflow_id,
        "status": "success",
        "message": "Planning completed"
    }

    response = requests.post(API_URL, json=payload)

    print("Status:", response.status_code)
    print("Response:", response.text)

    time.sleep(3)