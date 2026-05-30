from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import TelemetryEvent
from app.schemas import TelemetryCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/telemetry")
def create_event(
    payload: TelemetryCreate,
    db: Session = Depends(get_db)
):

    event = TelemetryEvent(
        agent_name=payload.agent_name,
        event_type=payload.event_type,
        latency=payload.latency,
        tokens=payload.tokens,
        status=payload.status,
        message=payload.message
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return {
        "message": "Telemetry stored",
        "event_id": event.id
    }

@router.get("/events")
def get_events(db: Session = Depends(get_db)):
    return db.query(TelemetryEvent).all()