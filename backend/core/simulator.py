"""
Simulator — spatial flood-extent calculation (bathtub model).

Given a segment's current water-surface elevation and the LiDAR-derived
terrain model, computes which terrain cells fall below that elevation, in a
format Cesium can render as a flood-extent overlay. Cesium itself only
renders; this module is what actually computes the flood extent.

Implemented in Tracker Phase 3 (see docs/HDHI_DASHBOARD_TRACKER.md).
Not yet implemented — this is a scaffold placeholder.
"""

from dataclasses import dataclass


@dataclass
class FloodExtentResult:
    segment_id: str
    timestamp: str
    water_surface_elevation_m: float
    extent_geojson: dict


def compute_flood_extent(
    segment_id: str,
    water_surface_elevation_m: float,
    dtm_path: str,
) -> FloodExtentResult:
    """
    Compute flood extent for a single point in time (bathtub model).

    See Tracker Goal 3.1: returns terrain cells/points below the given
    water-surface elevation as a GeoJSON extent, consumable directly by
    the Cesium frontend.
    """
    raise NotImplementedError("Tracker Goal 3.1 — not yet implemented")


def compute_flood_extent_series(
    segment_id: str,
    dtm_path: str,
    start_time: str,
    end_time: str,
) -> list[FloodExtentResult]:
    """
    Compute a time-tagged sequence of flood extents for animation.

    See Tracker Goal 3.2: reuses compute_flood_extent() per time step over
    a historical range, producing the sequence Cesium's Timeline/Clock
    widgets animate through.
    """
    raise NotImplementedError("Tracker Goal 3.2 — not yet implemented")
