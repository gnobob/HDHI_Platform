# HDHI Dashboard — Goal Tracker

_Format matches your existing card structure: Goal title → Status → prompt block → Description. Copy each block into a new card on the matching board. Prompts marked **lovable:** go into Lovable's chat; prompts marked **claude:** go into Claude Code against your own repo once the Lovable-generated code has been pulled in._

## Phase 0 — Foundation (board: `Phase 0 - Foundation`)
_The Lovable prompt itself is in `LOVABLE_FOUNDATION_PROMPT.md`, not repeated here. Nothing in Phase 1 onward has a real page to attach to until this scaffold exists in the repo._

### Goal 0.1 (Standalone Repo Setup)
**Status:** Done — repo scaffold generated, see `hdhi-monitoring/`
**Description:**
A new, standalone repo — separate from Autobit's own AXONIS platform — shaped the same way for consistency (backend / interfaces / docs) but scoped down to only what this project needs. This is what gets handed over to the client in full on contract completion, so it must not live inside or depend on Autobit's commercial codebase.

### Goal 0.2 (Import Lovable Output)
**Status:** To Do
**Description:**
Run `LOVABLE_FOUNDATION_PROMPT.md` in Lovable, then copy its generated project contents wholesale into `interfaces/dashboard/hdhi-ui/` (already present as a placeholder folder with its own README explaining this). Not used as the repo itself, not kept as a separate git remote or submodule — it becomes a normal subfolder of this repo, matching how `axonis-ui` sits inside AXONIS-Platform-main.

## Phase 1 — Simulated Hardware Layer (board: `Phase 1 - Simulation`)
_Stands in for real field hardware, which is covered separately under the Autobit contract. This lets every later phase be built and demoed without waiting on deployment._

### Goal 1.1 (Simulated Sensor Payload Generator)
**Status:** To Do
**Description:**
A Python script that generates realistic JSN-SR04T (water level) and HGB100 Doppler (velocity) readings for a configurable number of inlet/outlet sensor pairs, on a timed interval, matching the payload shape the real ESP32 nodes will eventually send.
**claude:**
```
I'm building a simulated sensor data generator for a highway drainage monitoring
project. Task: write a Python script that generates realistic water-level (JSN-SR04T,
cm) and flow-velocity (HGB100 Doppler, m/s) readings for a configurable set of
inlet/outlet sensor pairs, one pair per monitored culvert segment.

Each reading should include: segment_id, sensor_position (inlet/outlet), water_level_cm,
velocity_ms, timestamp. Emit readings on a configurable interval (default every few
seconds) via a simple function/generator, and also provide a way to push them to an
HTTP endpoint or a local message queue (your call, keep it simple — this just needs to
feed Goal 1.2's ingestion endpoint).

Also implement three named scenario modes the generator can be switched into:
"normal" (inlet/outlet track closely, low variance), "rainfall" (both inlet and outlet
rise and fall together, tracking a synthetic rainfall curve), and "clog" (inlet rises
while outlet stays flat — the differential clog signal). This is what will let the
Analyzer (Phase 2) and the dashboard be demoed convincingly without real hardware.

Scope: this script only, no server/ingestion code yet — that's a separate goal.
```

### Goal 1.2 (Ingestion Endpoint)
**Status:** To Do
**Description:**
A lightweight API endpoint that receives simulated (and later, real) sensor payloads and stores them for the Analyzer and dashboard to consume.
**claude:**
```
I'm building the ingestion endpoint for a highway drainage monitoring project's backend.
Task: implement a simple API endpoint (FastAPI or similar — your call) that accepts the
sensor payload shape from Goal 1.1 (segment_id, sensor_position, water_level_cm,
velocity_ms, timestamp), validates it, and stores it (a simple time-series-friendly
store is fine for thesis scope — SQLite, a local file-backed store, or an in-memory
store with periodic flush, whichever is simplest to stand up).

Also add a basic read endpoint that returns the latest reading (and recent history) per
segment, since the dashboard and Analyzer both need to read this data back out.

Scope: ingestion + storage + basic read-back only. No analysis logic here — that's
Phase 2.
```

## Phase 2 — Analyzer (board: `Phase 2 - Analyzer`)
_The hydraulic-state classification layer. This is what feeds HPI and RRI, and is the concrete answer to "where is the AI" that the client's current draft doesn't yet have._

### Goal 2.1 (Differential Classification Logic)
**Status:** To Do
**Description:**
Core function that compares inlet vs. outlet readings for a segment and classifies the current hydraulic state.
**claude:**
```
I'm implementing the core classification logic for a highway drainage monitoring
system's Analyzer module. Task: write a function that takes a segment's current and
recent inlet/outlet readings (water level + velocity, both positions) and classifies
the segment's state into one of: "normal", "rainfall_loading" (level and velocity rise
together at both inlet and outlet), or "possible_clog" (inlet level rises while outlet
stays comparatively flat — a differential mismatch).

Base the thresholds and comparison logic on the differential-monitoring approach
described in the project's DLSU proposal: under normal conditions inlet/outlet track
closely; a blockage produces a mismatch where input diverges from output.

Return a classification result with: state, confidence/severity, and the raw
differential values that led to the classification (needed later by the Explainer).

Scope: this function only, pure logic, no API wiring yet.
```

### Goal 2.2 (Analyzer API Wiring)
**Status:** To Do
**Description:**
Wire Goal 2.1's classification into an endpoint the dashboard can poll, and have it run automatically against incoming Goal 1.2 data.
**claude:**
```
I'm wiring the Analyzer classification function (Goal 2.1) into the backend built in
Phase 1. Task: run the classification function automatically whenever new readings
arrive for a segment (or on a short polling interval, whichever fits the Phase 1
storage approach better), and expose an endpoint returning each segment's current
classification, confidence, and the contributing raw values.

This endpoint is what the dashboard's Live Monitoring status strip and Dashboard
summary cards (from the Lovable foundation) will call instead of showing mock data.

Scope: wiring only, reuse Goal 2.1's logic unmodified.
```

## Phase 3 — Simulator (board: `Phase 3 - Simulator`)
_The spatial flood-extent layer. Cesium renders; this phase computes what it renders, using the bathtub-model approach against the LiDAR DTM._

### Goal 3.1 (Bathtub-Model Flood Extent Calculation)
**Status:** To Do
**Description:**
Given a segment's current water-level reading and the LiDAR-derived terrain model, compute which nearby terrain cells fall below the current water-surface elevation.
**claude:**
```
I'm implementing flood-extent calculation for a highway drainage monitoring system.
Task: write a function that takes a water-surface elevation (derived from a segment's
current water-level sensor reading plus that segment's known reference elevation) and
a LiDAR-derived DTM (digital terrain model, assume a standard raster/grid format such
as GeoTIFF, or ask for the actual format the LiDAR processing pipeline will output),
and returns the set of terrain cells/points whose elevation is below the water surface
— the "bathtub model" approach.

Output should be in a format Cesium can consume directly: either a polygon/extent
(GeoJSON) or a set of coordinates with depth values, whichever integrates more cleanly
with Goal 4.1's Cesium wiring.

Scope: this calculation only. Assume the DTM file/data is already available (LiDAR
processing itself is a separate, earlier pipeline step, not part of this goal).
```

### Goal 3.2 (Time-Animated Flood Overlay Data)
**Status:** To Do
**Description:**
Extend Goal 3.1 so flood extent can be computed across a time range (not just current moment), producing the sequence Cesium's timeline/clock can animate through.
**claude:**
```
I'm extending the flood-extent calculation (Goal 3.1) to support time-animation.
Task: given a time range and a segment's historical water-level readings over that
range (from Phase 1's storage), compute a flood-extent result (Goal 3.1's output
format) for each time step, producing a time-tagged sequence suitable for Cesium's
time-dynamic GeoJsonDataSource / Clock and Timeline widgets.

Scope: sequencing/time-indexing logic only, reuses Goal 3.1's per-timestep calculation
unmodified.
```

## Phase 4 — Live Monitoring Page Wiring (board: `Phase 4 - Visualization`)
_Replacing the Lovable foundation's placeholder panels with the real Cesium and culvert 3D views._

### Goal 4.1 (Cesium Terrain + Flood Overlay Integration)
**Status:** To Do
**Description:**
Replace the left placeholder panel from the Lovable scaffold with a real CesiumJS viewer loading the LiDAR terrain and rendering Goal 3.2's flood-extent sequence.
**lovable:**
```
In the Live Monitoring page, replace the left panel placeholder ("Flood Simulation —
LiDAR Terrain") with a real CesiumJS viewer. Load our LiDAR-derived terrain (terrain
tileset URL will be provided via an environment variable, use a placeholder env var
name for now: VITE_TERRAIN_URL). Render the flood-extent overlay data (GeoJSON, time-
tagged) coming from our backend's Simulator endpoint as a translucent blue extruded
polygon or draped overlay on the terrain, animated through Cesium's built-in Timeline
and Clock widgets so the flood extent changes over the selected time range.

Keep the loading state that was already built for this panel, shown until the terrain
and initial flood data have both loaded. Don't touch the right panel (culvert 3D
model) — that's a separate task.
```

### Goal 4.2 (Culvert 3D Model with Real-Time Status)
**Status:** To Do
**Description:**
Replace the right placeholder panel with a rotating 3D culvert/pipe model, colored/animated per segment based on the Analyzer's live classification.
**lovable:**
```
In the Live Monitoring page, replace the right panel placeholder ("Culvert Status —
Real-Time") with a rotating 3D model of the culvert/pipe network (model file will be
provided, use a placeholder path for now: /models/culvert.glb). Color-code or apply a
blinking highlight to specific segments of the model based on live classification data
from our Analyzer endpoint: green/steady for "normal", amber/pulsing for
"rainfall_loading", red/pulsing for "possible_clog".

Keep the existing loading state until both the model and the first classification
data have loaded. Reuse the same status-dot color convention already used in the
status-card strip below both panels, for visual consistency.
```

### Goal 4.3 (Status Strip + Summary Cards — Real Data)
**Status:** To Do
**Description:**
Swap the Lovable scaffold's mock data (status strip, Dashboard summary cards, HPI bar list) for real calls to the Phase 2 Analyzer endpoint.
**lovable:**
```
Replace the mock data currently powering the Live Monitoring status-card strip and the
Dashboard page's summary cards and HPI bar list with real data fetched from our
Analyzer API endpoint (base URL via env var VITE_API_URL). Keep the existing visual
design and loading states exactly as built — this is a data-source swap only, not a
redesign. Poll on a reasonable interval (a few seconds) or wire up a live connection if
one is available; either is fine for now.
```

## Phase 5 — Predictor & Explainer (board: `Phase 5 - Prediction`)
_The forward-looking and interpretability layer — the part that makes this more than a live dashboard._

### Goal 5.1 (Short-Term Trend Projection)
**Status:** To Do
**Description:**
Given a segment's recent reading history, project likely near-term water-level trend.
**claude:**
```
I'm implementing the Predictor module for a highway drainage monitoring system.
Task: write a function that takes a segment's recent water-level and velocity reading
history (from Phase 1 storage) plus recent rainfall data, and produces a short-term
trend projection — direction (rising/falling/stable), rough rate, and a simple
confidence indicator. Keep the method proportionate to available data (thesis-scope
sensor history, not a full hydrodynamic forecast) — a reasonable statistical/trend-
based approach (e.g. weighted recent-slope extrapolation) is appropriate; don't over-
engineer this into a full forecasting model unless later data volume clearly supports it.

Scope: this function only, no API wiring yet.
```

### Goal 5.2 (Plain-Language Explainer)
**Status:** To Do
**Description:**
Converts Analyzer classification + Predictor projection into a short, human-readable rationale and maintenance-priority suggestion.
**claude:**
```
I'm implementing the Explainer module for a highway drainage monitoring system.
Task: write a function that takes a segment's current Analyzer classification (Goal
2.1's output, including the raw differential values) and Predictor projection (Goal
5.1's output), and produces a short plain-language explanation string (e.g. "Segment 3:
inlet level rising while outlet remains flat — consistent with restricted conveyance,
not rainfall. Recommend inspection within 48 hours.") plus a maintenance-priority tag
(low/medium/high/urgent).

Keep the language template-based and grounded strictly in the actual classification and
values passed in — no invented specifics, no claims not supported by the input data.

Scope: this function only. Wiring it into the Logs page and Dashboard activity feed
(replacing their mock entries) is a follow-up goal once this is working standalone.
```

### Goal 5.3 (Wire Explainer into Logs + Dashboard Feed)
**Status:** To Do
**Description:**
Swap the Lovable scaffold's mock Logs table rows and Dashboard activity feed for real Explainer output.
**lovable:**
```
Replace the mock rows in the Logs page table and the Dashboard page's recent-activity
feed with real entries generated by our Explainer API endpoint (base URL via env var
VITE_API_URL). Keep the existing table/feed design, filters, and search exactly as
built. Each real entry should populate: timestamp, segment, event type (map from the
Analyzer's state field), severity/priority (from the Explainer's priority tag), and
description (the Explainer's plain-language string).
```

## Phase 6 — Analytics & Settings Wiring (board: `Phase 6 - Data & Controls`)

### Goal 6.1 (Analytics Charts — Real Data)
**Status:** To Do
**Description:**
Swap the Analytics page's placeholder charts for real historical data per segment.
**lovable:**
```
Replace the Analytics page's placeholder line charts (water level, velocity, HDHI
score over time) with real historical data from our backend's history endpoint (base
URL via env var VITE_API_URL), filtered by the existing segment-selector dropdown.
Keep the existing chart styling and layout exactly as built — data-source swap only.
```

### Goal 6.2 (Settings — Sensitivity & Override, Persisted)
**Status:** To Do
**Description:**
Wire the Settings page's sensitivity sliders and manual-override toggle to real backend storage, so they actually affect Analyzer thresholds and alerting.
**claude:**
```
I'm wiring the Settings page's controls to the backend. Task: add endpoints to get/set
per-segment sensor sensitivity thresholds (the values Goal 2.1's classification logic
uses) and a per-segment manual-override flag (when set, the segment is excluded from
automated alerting, per the Lovable scaffold's "mark as under manual maintenance"
control). Persist these alongside the rest of the Phase 1 storage.

Update Goal 2.1's classification function to read live thresholds and the override
flag instead of using fixed constants, so changes made in Settings actually take
effect.

Scope: backend only. The Settings page UI itself was already built in the Lovable
foundation — this goal is the persistence + wiring layer underneath it.
```

## Phase 7 — Demo & Defense Readiness (board: `Phase 7 - Defense Prep`)
_Not required for the academic contribution itself, but this is what makes the system demoable live during her proposal/final defense._

### Goal 7.1 (Scenario Trigger Controls)
**Status:** To Do
**Description:**
A way to trigger the Phase 1 simulator's named scenarios (normal/rainfall/clog) on demand during a live demo, without needing to edit code mid-presentation.
**claude:**
```
I'm adding demo controls for a highway drainage monitoring system. Task: add an
endpoint that lets the Phase 1 simulated sensor generator be switched between its
named scenarios ("normal", "rainfall", "clog") for a chosen segment, on demand.

Then add a small demo-control panel (can be a simple internal page, doesn't need to
match the main dashboard's polish) with a scenario dropdown per segment and a trigger
button, so scenarios can be switched live during a thesis defense without touching code.

Scope: demo tooling only, not part of the main client-facing dashboard pages.
```

### Goal 7.2 (Reset-State Button)
**Status:** To Do
**Description:**
One-click reset of all simulated data back to a clean baseline, for repeatable demo runs.
**claude:**
```
I'm adding a reset control for demo purposes. Task: add an endpoint (and a button on
the Goal 7.1 demo-control panel) that clears all stored simulated readings and
classifications and restarts every segment back in "normal" scenario mode, so the demo
can be run repeatably from a clean state.
```
