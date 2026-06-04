import requests
import random
import time

API_URL = "http://127.0.0.1:8000/telemetry"

while True:

    payload = {
        "agent_name": "research-agent",
        "event_type": "research",
        "latency": round(random.uniform(1.0, 3.0), 2),
        "tokens": random.randint(500, 2000),
        "status": "success",
        "message": "Research completed"
    }

    response = requests.post(API_URL, json=payload)

    print("Research:", response.json())

    time.sleep(4)