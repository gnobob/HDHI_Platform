"""
Explainer — plain-language rationale and maintenance-priority guidance.

Converts an Analyzer classification and a Predictor projection into a short
human-readable explanation plus a maintenance-priority tag. This is the
module that makes the system's output usable by a maintenance planner,
rather than a raw classification code or a number.

Implemented in Tracker Phase 5 (see docs/HDHI_DASHBOARD_TRACKER.md).
Not yet implemented — this is a scaffold placeholder.
"""

from dataclasses import dataclass
from enum import Enum

from .analyzer import ClassificationResult
from .predictor import TrendProjection


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


@dataclass
class Explanation:
    segment_id: str
    summary: str
    priority: Priority


def explain(
    classification: ClassificationResult,
    projection: TrendProjection,
) -> Explanation:
    """
    Produce a plain-language explanation and priority tag.

    See Tracker Goal 5.2: language must stay template-based and strictly
    grounded in the actual classification/projection values passed in —
    no invented specifics.
    """
    raise NotImplementedError("Tracker Goal 5.2 — not yet implemented")
