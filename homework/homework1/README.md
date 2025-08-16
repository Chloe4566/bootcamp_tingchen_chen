# Project Title
Citi Bike Usage Analysis and Station Demand Forecasting in New York City

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Citi Bike is New York City’s largest bike-sharing system, and balancing bikes across stations is a daily operational challenge. Users often encounter empty or full docks during peak periods, while operations teams rely on historical averages and manual rules that may not reflect weather, seasonality, or special events.

The primary stakeholder is the Citi Bike operations management team; end users include rebalancing staff, NYC DoT planners, and researchers. A useful answer combines descriptive insights (when/where demand spikes) with predictive forecasts at the station level. We will deliver visual summaries (e.g., heatmaps by station/time) and a forecasting model to support rebalancing decisions, evaluated by MAE/RMSE.

## Stakeholder & User
**Primary Stakeholder:** Citi Bike operations management team  
**End Users:** (1) Rebalancing staff who deploy trucks, (2) NYC DoT planners, (3) Researchers in urban mobility  
**Timing & Workflow Context:** Used to plan daily rebalancing schedules, identify high-demand stations before peaks, and evaluate long-term station expansion.

## Useful Answer & Decision
**Type:** Descriptive + Predictive  
**Metric / Artifact:** MAE/RMSE for station-level demand forecasts; deliverables include EDA visuals (heatmaps/charts) and a forecasting model that outputs expected pickups/returns by station and time window.

## Assumptions & Constraints
- Historical Citi Bike trip data contains timestamps, start/end stations, and user types.
- Weather data (e.g., temperature, precipitation) can be joined by date/time.
- Forecasts should run on a standard laptop within ~10 minutes for a citywide batch.
- Outputs support operations but are not guaranteed real-time predictions.

## Known Unknowns / Risks
- Sudden demand shifts from policy changes, extreme weather, or major events.
- Missing data or station capacity changes not captured in historical logs.
- Spatial confounders (bike lanes, hills, tourist hotspots) not fully modeled initially.

## Lifecycle Mapping
Goal → Stage → Deliverable
- Frame stakeholder-centered problem → Problem Framing & Scoping (Stage 01) → Scoping paragraph + README.md
- Acquire and clean trip + station + weather data → Data Collection & Preparation (Stage 02) → `/data/merged_citibike.csv`
- Describe demand patterns & drivers → EDA (Stage 03) → `/notebooks/citibike_eda.ipynb`
- Forecast station-level demand → Modeling (Stage 04) → `/notebooks/citibike_forecast.ipynb`
- Share insights & tool → Deployment (Stage 05) → Interactive dashboard/map + documentation

## Repo Plan
`/data/`, `/src/`, `/notebooks/`, `/docs/` ; weekly updates during development
