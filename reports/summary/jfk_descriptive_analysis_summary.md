# JFK Operational Risk Descriptive Summary

## Data cleaning

- Data coverage after cleaning: 2020-01 to 2025-12
- Raw rows: 570
- Removed because total arrival flights were missing or zero: 1
- Removed because delayed arrivals exceeded total arrivals: 0
- Final cleaned rows used for analysis: 569

## Descriptive insights

- Peak monthly delay volume occurred in 2023-07 with 3,657 delayed arrivals.
- Peak monthly cancellation volume occurred in 2020-03 with 1,900 cancelled arrivals.
- The largest delay-severity driver was Airline, contributing 36.2% of total delay minutes.
- The highest delay-rate airline was Hawaiian Airlines at 34.9%.
- The highest average delay severity was Envoy Air at 90.7 minutes per delayed flight.

## Output update note

- The core cleaned dataset keeps the same field names as the earlier single-year workflow.
- The monthly summary includes `year`, `year_month`, and `period_start` to support the current multi-year timeline.
- The static charts and offline dashboard use a softer presentation palette and system-safe fonts for consistent PNG and SVG rendering.
- Chart 2 is now exported as a compact horizontal layout with transparent PNG and SVG backgrounds for cleaner report and slide placement.

## Modeling handoff note

- The cleaned core dataset preserves frequency variables such as delayed arrivals and cancellations.
- It also preserves severity variables through total delay minutes and delay-cause minutes.
- These outputs are ready to support later work on frequency models, severity models, and aggregate loss modeling.
