# Stakeholder Memo: Citi Bike Usage & Station Demand Forecasting

## Background
Citi Bike is a core part of NYC’s mobility network. Riders often face empty or full docks during peaks, while operations teams plan rebalancing largely from historical averages and manual rules that may miss weather, seasonality, and special events.

## Stakeholders & Users
- **Primary stakeholder:** Citi Bike operations management team  
- **End users:** (1) Rebalancing staff who deploy trucks, (2) NYC DoT planners, (3) Urban mobility researchers  
- **Workflow context:** Daily rebalancing planning, pre-peak station targeting, and long-term station expansion assessment.

## Problem
How can we describe when/where demand spikes occur and **forecast station-level demand** to reduce shortages/surpluses and improve rider experience?

## Proposed Solution
1. **Descriptive insights:** Heatmaps/charts of usage by station, hour, weekday/weekend, and season.  
2. **Predictive model:** Forecast expected pickups/returns per station and time window, incorporating weather and calendar effects.

## Data & Assumptions
- Historical trip logs with timestamps, start/end stations, and user types.  
- Weather features (temperature, precipitation) joinable by date/time.  
- Forecasts should run citywide on a standard laptop in ~10 minutes.

## Deliverables
- EDA visuals (heatmaps, peak-hour charts, station leaderboards).  
- Station-level forecasting model with **MAE/RMSE** reporting.  
- (Stretch) Interactive map/dashboard to explore demand by station/time.

## Risks & Unknowns
- Sudden demand shifts (policy, extreme weather, major events).  
- Missing data or station capacity changes not logged.  
- Spatial confounders (lanes, hills, tourist hotspots) not fully modeled initially.
