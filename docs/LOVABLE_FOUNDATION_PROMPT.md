# Lovable Foundation Prompt — HDHI Flood & Drainage Monitoring Dashboard

_Paste the prompt below into Lovable as-is. Written in the same discipline as your AXONIS GridSonar prompt: narrative brand direction instead of exact hex/token values, no prescribed tech stack, one clearly-prioritized screen, vivid mock content — leaving Lovable room to reach for its own modern implementation rather than copying a spec. Expect a follow-up conversation to refine details (panel glass effect, spacing, etc.), same as AXONIS needed._

---

## Prompt to paste into Lovable

```
Design a dark, high-tech enterprise dashboard called HDHI Monitor, a highway drainage
health monitoring platform for civil engineers and DPWH maintenance planners. This is
a UI/visual design exercise only: use mock/placeholder data throughout, no real
backend, no live data connections, no real Cesium or 3D engine integration — represent
the 3D panels as high-fidelity static visual placeholders that convey what they'll
eventually show, not functional 3D viewers. Focus entirely on layout, typography,
color, spacing, and micro-animations.

BRAND IDENTITY (match this, don't invent a new style):

Dark near-black or deep navy background, electric teal accent color for active states
and live data, a subtle grid-line texture across the background reminiscent of
technical survey grids or blueprints, soft ambient glow effects behind key panels and
active elements, clean sans-serif or monospace-leaning typography for a technical,
instrumentation feel. A serious civil-engineering/infrastructure-monitoring tone,
not a playful consumer app feel. Think: a hydrological command center for flood-risk
planning, not a weather app.

LAYOUT:

Left sidebar navigation, collapsible, with a top bar showing a MODE indicator
(LIVE/SIMULATED toggle-style), active monitored-segment count, and active alert count
as small stat chips.

SIDEBAR NAV ITEMS, split into two visually distinct groups:

Active group (fully clickable, normal styling):
- Live Monitoring
- Dashboard
- Analytics
- Logs
- Settings

Locked group (visually present but styled as disabled/muted, each with a small
"Coming in v2" badge, still show an icon and label, just clearly not active):
- Multi-Site Comparison
- DPWH Records Sync
- Predictive Maintenance Scheduler
- Public Flood Alert Broadcast
- Historical Flood Archive
- Mobile Field Companion

SCREEN 1, Live Monitoring (this is the most important screen, spend the most design
effort here):

Two side-by-side high-fidelity panels forming the centerpiece of the dashboard:
- LEFT PANEL: a stylized 3D terrain/topography view labeled "Flood Simulation —
  LiDAR Terrain," showing a translucent blue flood-extent overlay spreading across
  a mocked terrain mesh near a road/culvert — convey the impression of water rising
  across real ground, not a flat map.
- RIGHT PANEL: a rotating 3D culvert/pipe network view labeled "Culvert Status —
  Real-Time," with individual pipe segments color-coded by condition.
Design one specific segment in the right panel as clearly at risk — glowing amber or
red with a subtle pulse animation and a short annotation like "Segment 3 — inlet/
outlet differential rising, possible restriction" — while the other segments stay
calm teal/green and visually quiet. The visual point is that a viewer should
immediately understand, at a glance and without reading a table, which segment needs
attention and that the rest of the network is healthy.

Below both panels: a horizontal strip of small status cards, one per monitored
segment, each showing a segment name, a colored status dot, current water level, and
current flow velocity, using believable mock values.

SCREEN 2, Dashboard (overview/summary):

Summary cards across the top: total monitored segments, healthy vs. at-risk count, an
overall HDHI score shown as a large, prominent number, and active alert count. Below
that, a horizontal bar list showing Hydraulic Performance Index per segment. Below
that, a recent-activity feed with realistic mock entries phrased like real system
output, e.g. "Segment 3 — inlet/outlet differential rising, possible restriction,"
"Segment 7 — rainfall loading detected, normal response," each with a timestamp and
severity indicator consistent with Screen 1's color language.

Please provide both screens as part of one cohesive dashboard flow, not two
disconnected mockups — visual language (colors, panel style, iconography, the status/
severity color scale) must stay consistent across both, and should extend naturally
to the remaining nav items (Analytics, Logs, Settings) even though this pass only
designs the two screens above in detail.
```

---

## After this scaffold exists

Once Lovable generates this and it's pulled into your own repo (per your note — reference the design, don't fork the Lovable repo directly, drop the output into `interfaces/dashboard/hdhi-ui/`), proceed to `HDHI_DASHBOARD_TRACKER.md` starting at Phase 2, which wires in: the simulated hardware data layer, the Analyzer/Simulator/Predictor/Explainer logic, real Cesium + culvert 3D model integration, and real data flowing into the Dashboard/Analytics/Logs/Settings pages this scaffold already laid out.

Expect this to take a few follow-up messages in Lovable to land exactly right — your AXONIS prompt needed a "make it glass" round after the first pass too. Worth iterating live rather than trying to pre-specify everything here.
