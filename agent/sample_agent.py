import requests
import random
import time

API_URL = "http://127.0.0.1:8000/telemetry"

events = [
    "prompt_received",
    "llm_response",
    "tool_call",
    "memory_lookup"
]

while True:

    latency = round(random.uniform(0.5, 3.0), 2)

    payload = {
        "agent_name": "research-agent",
        "event_type": random.choice(events),
        "latency": latency,
        "tokens": random.randint(100, 3000),
        "status": "success",
        "message": "AI event processed"
    }

    response = requests.post(API_URL, json=payload)

    print(response.json())

    time.sleep(2)