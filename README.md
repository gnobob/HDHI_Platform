# HDHI Flood & Drainage Monitoring Platform

_Working title — rename freely once you and the client settle on branding._

## What this is

A web dashboard that turns raw water-level and flow-velocity sensor data from highway
culverts into a spatial, explained, and forward-looking picture of drainage health —
built to support a masteral thesis on the **Highway Drainage Health Index (HDHI)**, and
structured so it can grow into a real DPWH-facing tool afterward.

## The problem this addresses

Highway drainage failures are currently caught two ways: scheduled manual inspection,
or after the fact, when flooding has already happened. Neither tells a maintenance
planner *which* segment is quietly deteriorating *before* it becomes visible. Water
level alone can't answer that either — a rising level could mean heavy rain, or it
could mean a blockage, and those need completely different responses.

## The core idea

Two non-contact sensors (ultrasonic water-level, Doppler radar velocity) at the inlet
and outlet of a culvert segment provide a continuous differential signal. Compared
against each other and against rainfall data, that differential tells you *why* a
segment's condition is changing — not just *that* it is. This system is the layer that
takes that raw signal and turns it into something a human can act on:

- **Where** a problem is — rendered spatially on a 3D terrain model, not buried in a
  table of numbers
- **Why** it's happening — rainfall load, restricted conveyance, or genuine capacity
  exceedance, distinguished automatically
- **What's likely next** — a short-term projection, not just a current reading
- **What to do about it** — maintenance-prioritization guidance grounded in the above,
  not a raw alert dashboard

## System shape

Two layers, deliberately separated:

- **Hardware (edge):** sensors + microcontroller, transmit-only. No analysis happens
  in the field. Kept simple, low-power, and replicable across additional sites without
  firmware changes.
- **Server (the actual product):** everything that matters happens here — hydraulic
  state classification (Analyzer), flood-extent spatial simulation on the LiDAR terrain
  (Simulator), short-term trend projection (Predictor), and plain-language rationale +
  maintenance guidance (Explainer).

See `docs/HDHI_SYSTEM_ARCHITECTURE.md` for the full technical breakdown of this split.

## Repository structure

This repo is standalone and self-contained — separate from Autobit's own AXONIS
platform (which powers GridSonar/MineSafe), so it can be handed over in full to the
client on final payment, per the contract's ownership-transfer terms. It's shaped the
same way as AXONIS for consistency, but scoped down to only what this project needs —
no ledger, governance, or multi-tenant access-control layers, none of which have a role
in a thesis deliverable.

```
hdhi-monitoring/
├── backend/
│   ├── core/                       # Analyzer, Simulator, Predictor, Explainer
│   ├── ingestion/                  # sensor payload API (Phase 1)
│   ├── samples/simulated_events/   # simulated sensor data generator
│   └── tests/
├── interfaces/
│   └── dashboard/
│       └── hdhi-ui/                # Lovable-generated frontend goes here, wholesale
├── docs/
│   ├── HDHI_SYSTEM_ARCHITECTURE.md
│   ├── HDHI_DASHBOARD_TRACKER.md
│   └── LOVABLE_FOUNDATION_PROMPT.md
└── README.md
```

The Lovable output is imported as a subfolder (`interfaces/dashboard/hdhi-ui/`), not
used as the repo itself and not kept as a separate git remote — this repo is the single
source of truth, matching how `axonis-ui` sits inside AXONIS-Platform-main.

## Why a dashboard, not just an index

The thesis's academic contribution is the HDHI formula itself — a weighted composite
of four sub-indices (Hydraulic Performance, Physical Condition, Rainfall Response,
Maintenance Recurrence). A composite index on its own is still just a number in a
spreadsheet, though. This dashboard is what makes that number usable: two live 3D
panels showing (1) a LiDAR-based flood simulation across the whole terrain and (2) a
real-time status view of the culvert/pipe network itself — the part no LiDAR scan can
see, since it's underground. Paired with a summary dashboard, analytics, activity logs,
and manual override controls, this is the interface an actual maintenance planner
would use, not just a proof-of-concept chart.

## Scope for the thesis vs. scope for later

For thesis purposes, hardware is assumed already built (covered separately under
contract) and is represented here through a **simulated device layer** — Python
scripts injecting realistic sensor payloads — so the full dashboard, Analyzer,
Simulator, and Predictor/Explainer logic can be developed and defended without waiting
on live field deployment.

## Scope for the thesis vs. scope for later

For thesis purposes, hardware is assumed already built (covered separately under
contract) and is represented here through a **simulated device layer** — Python
scripts injecting realistic sensor payloads — so the full dashboard, Analyzer,
Simulator, and Predictor/Explainer logic can be developed and defended without waiting
on live field deployment.

If the client wants to pursue commercialization or DPWH-wide deployment after the
thesis, that's a separate future conversation and, most likely, a separate contract —
at that point the working logic here would be ported into a proper engine inside
Autobit's own AXONIS platform, the same way GridSonar and MineSafe live there now.
This repo intentionally stays self-contained rather than pre-wired for that path, so
the IP handed over to the client on contract completion stays clean and fully hers.

## Status

Early foundation stage — UI scaffold in progress via Lovable (see
`docs/LOVABLE_FOUNDATION_PROMPT.md`), with the full build sequence tracked in
`docs/HDHI_DASHBOARD_TRACKER.md`.
