import requests
import random
import time

API_URL = "http://127.0.0.1:8000/telemetry"

while True:

    payload = {
        "agent_name": "planner-agent",
        "event_type": "planning",
        "latency": round(random.uniform(0.5, 2.0), 2),
        "tokens": random.randint(100, 1000),
        "status": "success",
        "message": "Planning completed"
    }

    response = requests.post(API_URL, json=payload)

    print("Planner:", response.json())

    time.sleep(3)