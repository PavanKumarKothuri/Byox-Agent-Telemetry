from pydantic import BaseModel

class TelemetryCreate(BaseModel):
    agent_name: str
    event_type: str
    latency: float
    tokens: int
    status: str
    message: str