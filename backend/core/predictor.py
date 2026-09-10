"""
Predictor — short-term trend projection.

Given a segment's recent reading history and rainfall data, projects the
likely near-term water-level trend (direction, rough rate, confidence).

Implemented in Tracker Phase 5 (see docs/HDHI_DASHBOARD_TRACKER.md).
Not yet implemented — this is a scaffold placeholder.
"""

from dataclasses import dataclass
from enum import Enum


class TrendDirection(str, Enum):
    RISING = "rising"
    FALLING = "falling"
    STABLE = "stable"


@dataclass
class TrendProjection:
    segment_id: str
    direction: TrendDirection
    rate_cm_per_hour: float
    confidence: float


def project_trend(
    segment_id: str,
    recent_history: list,
    rainfall_data: list | None = None,
) -> TrendProjection:
    """
    Project a segment's short-term water-level trend.

    See Tracker Goal 5.1: a proportionate statistical/trend-based approach
    (e.g. weighted recent-slope extrapolation) is appropriate for
    thesis-scope data — not a full hydrodynamic forecast model.
    """
    raise NotImplementedError("Tracker Goal 5.1 — not yet implemented")
