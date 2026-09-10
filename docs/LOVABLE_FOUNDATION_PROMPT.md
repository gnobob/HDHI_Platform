# Lovable Foundation Prompt — HDHI Flood & Drainage Monitoring Dashboard

_Paste the prompt below into Lovable as-is to scaffold the initial UI shell. This produces the design/layout foundation only — no real data wiring, no backend, no simulated-device integration. Those are covered in the Tracker (`HDHI_DASHBOARD_TRACKER.md`) as Phase 2 onward, once this foundation exists in the repo._

---

## Prompt to paste into Lovable

```
Build a web dashboard for a highway drainage health monitoring system. This is an
operations/engineering dashboard for civil engineers and DPWH maintenance planners —
not a consumer app. Dark, technical, industrial tone: think network operations center,
not a SaaS marketing dashboard.

DESIGN LANGUAGE
- Dark blue-black background using OKLCH color space (background: oklch(0.16 0.02 240),
  panels: oklch(0.19 0.025 240), elevated panels: oklch(0.23 0.03 235)) — not flat black,
  a cool near-navy dark tone
- Primary accent: teal (oklch(0.82 0.15 195)), used for active states, live data,
  primary actions, with a soft glow effect on key active elements (box-shadow using the
  same teal at low opacity, layered at two blur radii for a subtle halo)
- Full 5-tier severity/status scale, not just 2-3 colors: advisory (soft blue),
  info (teal-green), elevated (amber/gold), high (orange), critical (red) — each status
  badge uses its own color consistently across the whole app (dots, badges, left-edge
  card borders)
- A critical-state glow effect (red box-shadow halo) mirroring the teal glow, reserved
  for critical alerts/status only, so it reads as urgent by contrast with the normal
  teal glow
- Subtle background texture: a faint 32px×32px grid-line pattern across the page
  background (two 1px linear-gradients at ~3% white opacity, one horizontal one
  vertical), plus soft ambient radial-gradient glows in the corners (low-opacity teal/
  cyan blobs, fixed position, barely visible — adds depth without being distracting)
- Fonts: a monospace font for headings/labels/data (e.g. JetBrains Mono, tight letter-
  spacing) giving a technical/terminal feel, a clean sans-serif for body text (e.g. Inter)
- Single theme only, no light mode — this is a control-room tool, always dark
- Card-based layout ("panels"), thin low-opacity hairline borders, rounded corners
  (~0.5rem), no heavy shadows except the teal/critical glow accents above — flat/glass
  panel aesthetic over skeuomorphic depth
- Fully responsive — sidebar collapses to icons-only or a drawer on narrower viewports,
  the Live Monitoring dual-panel layout stacks vertically on mobile, all tables/cards
  reflow rather than overflow

OPTIONAL — FLOATING ASSISTANT PANEL
If straightforward to include, add a collapsible floating assistant panel (bottom-right
corner, toggle button when closed) — a chat-style panel labeled something like
"[Assistant Name] · Drainage Copilot", with a "Simulated · ready to connect" subtitle, a
short intro message, a few suggested-prompt quick-action buttons (e.g. "Check active
critical segments", "Summarize latest flood simulation", "Explain current HDHI score"),
and a text input with a visible "mock mode" indicator. Mock responses only at this
stage — this is a UI placeholder for a future AI assistant feature, not a real
integration.

PAGES (sidebar navigation, top bar shows connection status + active alert count)

1. LIVE MONITORING (default/landing page)
   Two side-by-side 3D panels, equal width, each in its own card:
   - LEFT PANEL: placeholder container for a Cesium 3D terrain/globe view (label it
     "Flood Simulation — LiDAR Terrain", leave as a styled empty container with a
     "connecting to terrain service" loading state — the real Cesium integration is a
     separate build step, not part of this scaffold)
   - RIGHT PANEL: placeholder container for a rotating 3D culvert/pipe model (label it
     "Culvert Status — Real-Time", also a styled empty container with the same loading
     pattern — the real 3D model viewer is wired in separately)
   Below both panels: a horizontal strip of small status cards, one per monitored
   culvert/segment, each showing: segment name, a colored status dot (using the 5-tier
   severity scale above: info/elevated/high/critical as relevant, teal for normal),
   current water level reading, current flow velocity reading — use placeholder mock
   values for now.

2. DASHBOARD (summary/overview page)
   Grid of summary cards at the top: total monitored segments, segments currently
   healthy vs. at-risk, overall average HDHI score (large number, prominent), active
   alerts count. Below that, a card showing "Hydraulic Performance Index (HPI)" per
   segment as a simple horizontal bar list (mock data). Below that, a recent-activity
   feed card (mock entries: "Segment 3 — differential rise detected", timestamps).

3. ANALYTICS
   A page for time-series trends. Include placeholder line-chart cards for: water
   level over time, flow velocity over time, HDHI score over time — one selector
   dropdown to choose which segment to view. Use mock/dummy chart data for now.

4. LOGS
   A simple filterable table: timestamp, segment, event type (normal / rainfall
   loading / possible clog / maintenance note), severity, short description. Include
   a search bar and a severity filter dropdown. Mock rows are fine.

5. SETTINGS
   Form-style page with sections: "Sensor Sensitivity" (sliders or numeric inputs per
   segment for water-level and velocity thresholds), "Alert Preferences" (toggles for
   notification types), "Manual Override" (a control to mark a segment as under
   manual maintenance, pausing its automated alerts). No real save logic needed yet,
   just the UI.

TECH
- React + TypeScript + Tailwind
- Use a component library consistent with shadcn/ui conventions (cards, buttons,
  tables, dropdowns, sliders, badges/status dots)
- Structure pages as real routes (not a single-page mock), sidebar nav persists
  across all pages
- All data on every page should be clearly mock/placeholder data at this stage —
  structure it so it's obviously easy to swap for real API calls later (e.g. a single
  mock-data file or hook per page, not values hardcoded inline all over the JSX)

Do not attempt to integrate real Cesium, real 3D model viewers, or any backend/API
calls in this pass — this is the visual/structural foundation only.
```

---

## After this scaffold exists

Once Lovable generates this and it's pulled into your own repo (per your note — reference the design, don't fork the Lovable repo directly), proceed to `HDHI_DASHBOARD_TRACKER.md` starting at Phase 2, which wires in: the simulated hardware data layer, the Analyzer/Simulator/Predictor/Explainer logic, real Cesium + culvert 3D model integration, and real data flowing into the Dashboard/Analytics/Logs/Settings pages this scaffold already laid out.
