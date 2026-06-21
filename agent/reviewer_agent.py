import requests
import random
import time

API_URL = "http://127.0.0.1:8000/telemetry"

while True:

    workflow_id = "wf-001"

    tokens = random.randint(200, 1500)

    cost_usd = round(
        tokens * 0.000002,
        5
    )

    payload = {
        "agent_name": "reviewer-agent",
        "event_type": "review",
        "latency": round(random.uniform(0.5, 2.5), 2),
        "tokens": tokens,
        "cost_usd": cost_usd,
        "workflow_id": workflow_id,
        "status": "success",
        "message": "Review completed"
    }

    response = requests.post(API_URL, json=payload)

    print("Reviewer:", response.json())

    time.sleep(4)