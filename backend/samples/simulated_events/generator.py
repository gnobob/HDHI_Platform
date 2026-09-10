"""
Simulated sensor payload generator.

Stands in for real ESP32 + JSN-SR04T + HGB100 Doppler field hardware
(covered separately under the hardware contract), so the backend and
dashboard can be built and demoed end-to-end without waiting on field
deployment.

Implemented in Tracker Phase 1, Goal 1.1 (see docs/HDHI_DASHBOARD_TRACKER.md).
Not yet implemented — this is a scaffold placeholder.
"""

from enum import Enum


class ScenarioMode(str, Enum):
    NORMAL = "normal"
    RAINFALL = "rainfall"
    CLOG = "clog"


class SimulatedSegment:
    """
    Simulates one culvert segment's inlet/outlet sensor pair.

    See Tracker Goal 1.1 for the three required scenario modes:
    - normal: inlet/outlet track closely, low variance
    - rainfall: both inlet and outlet rise/fall together, tracking a
      synthetic rainfall curve
    - clog: inlet rises while outlet stays flat (the differential
      clog signal)
    """

    def __init__(self, segment_id: str, mode: ScenarioMode = ScenarioMode.NORMAL):
        self.segment_id = segment_id
        self.mode = mode

    def next_reading_pair(self) -> tuple[dict, dict]:
        """Return (inlet_reading, outlet_reading) for the current tick."""
        raise NotImplementedError("Tracker Goal 1.1 — not yet implemented")


def run_generator(segments: list[SimulatedSegment], interval_seconds: float = 5.0) -> None:
    """
    Continuously generate readings for all segments and push them to the
    ingestion API. Not yet implemented — see Tracker Goal 1.1.
    """
    raise NotImplementedError("Tracker Goal 1.1 — not yet implemented")
