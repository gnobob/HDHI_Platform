"""
Ingestion API — receives sensor payloads (simulated or real) and stores them.

Implemented in Tracker Phase 1, Goal 1.2 (see docs/HDHI_DASHBOARD_TRACKER.md).
This is a minimal FastAPI skeleton — routes are defined but not yet backed
by real storage or read-back logic.
"""

from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="HDHI Ingestion API")


class SensorReading(BaseModel):
    segment_id: str
    sensor_position: str  # "inlet" | "outlet"
    water_level_cm: float
    velocity_ms: float
    timestamp: datetime


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/api/v1/readings")
def submit_reading(reading: SensorReading) -> dict:
    """
    Accept a sensor reading. Storage not yet implemented — see Tracker
    Goal 1.2.
    """
    raise NotImplementedError("Tracker Goal 1.2 — storage not yet implemented")


@app.get("/api/v1/readings/{segment_id}/latest")
def get_latest_reading(segment_id: str) -> dict:
    """
    Return the latest reading for a segment. Not yet implemented — see
    Tracker Goal 1.2.
    """
    raise NotImplementedError("Tracker Goal 1.2 — read-back not yet implemented")
