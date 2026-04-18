# JFK Operational Risk Descriptive Summary

## Data cleaning

- Raw rows: 101
- Removed because total arrival flights were missing or zero: 0
- Removed because delayed arrivals exceeded total arrivals: 0
- Final cleaned rows used for analysis: 101

## Descriptive insights

- Peak monthly delay volume occurred in month 7 with 3,228 delayed arrivals.
- Peak monthly cancellation volume occurred in month 7 with 874 cancelled arrivals.
- The largest delay-severity driver was Late Aircraft, contributing 34.1% of total delay minutes.
- The highest delay-rate airline was Alaska Airlines at 29.0%.
- The highest average delay severity was Endeavor Air at 97.2 minutes per delayed flight.

## Modeling handoff note

- The cleaned core dataset preserves frequency variables such as delayed arrivals and cancellations.
- It also preserves severity variables through total delay minutes and delay-cause minutes.
- These outputs are ready to support later work on frequency models, severity models, and aggregate loss modeling.
