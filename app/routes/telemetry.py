from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import json

from app.redis_client import r
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
def create_event(payload: TelemetryCreate):

    r.lpush(
        "telemetry_queue",
        json.dumps(payload.dict())
    )

    return {
        "message": "Event queued"
    }


@router.get("/events")
def get_events(db: Session = Depends(get_db)):
    return db.query(TelemetryEvent).all()


@router.get("/queue-size")
def queue_size():

    return {
        "queue_size": r.llen("telemetry_queue")
    }