from fastapi import FastAPI

from app.database import Base, engine
from app.routes.telemetry import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BYOX Agent Telemetry Collector"
)

app.include_router(router)