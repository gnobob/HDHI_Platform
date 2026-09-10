# System Architecture: Edge Sensing and Server-Side Analytics for Highway Drainage Monitoring

## Overview

The monitoring system follows a two-layer architecture: a **hardware (edge) layer** responsible solely for data acquisition and transmission, and a **server (analytics) layer** responsible for interpretation, spatial simulation, prediction, and decision support. This separation ensures that the field-deployed units remain low-cost, low-power, and low-maintenance, while all computational complexity — anomaly detection, flood simulation, and predictive analysis — is centralized where it can be validated, updated, and audited independently of the physical hardware.

## 1. Hardware Layer (Edge Nodes)

Each monitoring node consists of a JSN-SR04T non-contact ultrasonic sensor (water level) and an HGB100 Doppler radar sensor (surface flow velocity), interfaced through an ESP32 microcontroller. Nodes are deployed in pairs at the inlet and outlet of each monitored culvert or canal segment, powered by a solar-charged battery system for continuous field operation.

The edge layer performs no local analysis or decision-making. Its sole function is to sample water-level and surface-velocity readings at fixed intervals and transmit them, with timestamps, to the server layer. This keeps the field hardware simple, power-efficient, and easily replicable across additional sites without requiring firmware changes to accommodate new analytical logic.

## 2. Server Layer (Analysis, Simulation, and Prediction)

The server layer receives raw sensor streams and performs four functions:

**a. Analyzer.** Compares inlet and outlet readings in real time to classify the current hydraulic state of each segment: normal flow, rainfall-driven loading (level and velocity rise together at both ends), or restricted conveyance (input rises while output remains comparatively flat — the differential clog signal). This classification forms the empirical basis for the study's Hydraulic Performance Index (HPI) and contributes to the Rainfall Response Index (RRI) when correlated with weather-API rainfall data.

**b. Simulator.** Projects the analyzed hydraulic state onto a drone-acquired LiDAR-derived 3D terrain model, rendered in Cesium. Rather than presenting sensor output as isolated numeric alerts, the simulator generates a spatial flood-extent overlay showing which specific low-lying or hydraulically compromised areas are affected, and how conditions at one segment may propagate to adjacent terrain.

**c. Predictor.** Uses current and recent sensor readings, together with rainfall data, to project near-term water-level and flow trends per segment, providing an early indication of developing risk rather than only reporting present conditions.

**d. Explainer.** Converts the Analyzer's classification and the Predictor's projection into a plain-language rationale (e.g., identifying whether a rising level is attributable to rainfall loading or to restricted conveyance) and logs this as a progressive, time-series record rather than a single static snapshot. This output layer directly supports the study's preventive-maintenance objective by providing maintenance-prioritization guidance grounded in observed hydraulic behavior, rather than reactive response to visible flooding.

## 3. Data Flow Summary

```
[JSN-SR04T + Doppler Radar] → [ESP32: sample + transmit]
            ↓
[Server: Analyzer] → hydraulic state classification (HPI, RRI input)
            ↓
[Server: Simulator] → LiDAR/Cesium spatial flood overlay
            ↓
[Server: Predictor] → short-term trend projection
            ↓
[Server: Explainer] → plain-language rationale + maintenance guidance
```

## 4. Relevance to the HDHI Framework

This architecture directly operationalizes two of the study's four HDHI dimensions: the Analyzer's hydraulic-state classification provides the continuous input for **HPI**, while its correlation with rainfall data provides the dynamic-response input for **RRI**. The Simulator and Explainer layers do not compute HDHI itself, but serve as the spatial decision-support interface through which HDHI scores and their contributing anomalies are communicated to maintenance planners — distinguishing this system from index-only approaches that report a numeric score without spatial or explanatory context.
