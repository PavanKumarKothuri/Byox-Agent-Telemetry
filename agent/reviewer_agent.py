import requests
import random
import time

API_URL = "http://127.0.0.1:8000/telemetry"

while True:

    payload = {
        "agent_name": "reviewer-agent",
        "event_type": "review",
        "latency": round(random.uniform(0.5, 2.5), 2),
        "tokens": random.randint(200, 1500),
        "status": "success",
        "message": "Review completed"
    }

    response = requests.post(API_URL, json=payload)

    print("Reviewer:", response.json())

    time.sleep(4)