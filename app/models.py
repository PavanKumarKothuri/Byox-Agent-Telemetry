from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class TelemetryEvent(Base):
    __tablename__ = "telemetry_events"

    id = Column(Integer, primary_key=True, index=True)

    agent_name = Column(String)
    event_type = Column(String)

    latency = Column(Float)
    tokens = Column(Integer)

    cost_usd = Column(Float)   # NEW
    workflow_id = Column(String)

    status = Column(String)
    message = Column(String)