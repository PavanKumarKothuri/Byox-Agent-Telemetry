from pydantic import BaseModel

class TelemetryCreate(BaseModel):
    agent_name: str
    event_type: str
    latency: float
    tokens: int
    cost_usd: float
    workflow_id: str
    status: str
    message: str