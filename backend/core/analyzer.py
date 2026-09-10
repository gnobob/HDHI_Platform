"""
Analyzer — hydraulic state classification.

Compares inlet vs. outlet sensor readings for a segment and classifies the
current hydraulic state as one of: "normal", "rainfall_loading", or
"possible_clog". This is the module that feeds the study's Hydraulic
Performance Index (HPI) and, via correlation with rainfall data, the
Rainfall Response Index (RRI).

Implemented in Tracker Phase 2 (see docs/HDHI_DASHBOARD_TRACKER.md).
Not yet implemented — this is a scaffold placeholder.
"""

from dataclasses import dataclass
from enum import Enum


class HydraulicState(str, Enum):
    NORMAL = "normal"
    RAINFALL_LOADING = "rainfall_loading"
    POSSIBLE_CLOG = "possible_clog"


@dataclass
class ClassificationResult:
    segment_id: str
    state: HydraulicState
    confidence: float
    inlet_level_cm: float
    outlet_level_cm: float
    inlet_velocity_ms: float
    outlet_velocity_ms: float


def classify_segment(
    segment_id: str,
    inlet_level_cm: float,
    outlet_level_cm: float,
    inlet_velocity_ms: float,
    outlet_velocity_ms: float,
    recent_history: list | None = None,
) -> ClassificationResult:
    """
    Classify a segment's current hydraulic state from inlet/outlet readings.

    See Tracker Goal 2.1 for the full specification: under normal conditions
    inlet/outlet readings track closely; rainfall loading shows both rising
    together; a possible clog shows inlet rising while outlet stays flat.
    """
    raise NotImplementedError("Tracker Goal 2.1 — not yet implemented")
