# Operational Risk Workflow

This folder now contains a reusable workflow for the JFK airline delay and cancellation project.

## Conda environment

Environment name: `operational_risk`

If you want to activate it manually:

```bash
source /home/simon033/miniconda3/bin/activate operational_risk
```

For reproducibility on another machine, use:

```bash
conda env create -f environment_operational_risk.yml
```

## Run the full pipeline again

```bash
/home/simon033/miniconda3/envs/operational_risk/bin/python scripts/build_operational_risk_assets.py
```

## Main outputs

- `outputs/data/jfk_airline_delay_readable_full.csv`
  A readable full dataset with airline codes replaced by full airline names and clearer column names.
- `outputs/data/jfk_airline_delay_core_cleaned.csv`
  The cleaned core dataset for later modeling work.
- `outputs/data/jfk_column_dictionary.csv`
  A data dictionary with original columns, readable column names, and plain-language meanings.
- `outputs/data/jfk_monthly_risk_summary.csv`
  Monthly totals used for trend analysis.
- `outputs/data/jfk_delay_cause_summary.csv`
  Total delay minutes by cause.
- `outputs/data/jfk_airline_risk_profile.csv`
  Airline-level risk metrics including delay rate and average delay severity.
- `outputs/charts/*.png`
  High-resolution static charts for reports and slides.
- `outputs/charts/*.svg`
  Vector charts for PowerPoint and print-quality use.
- `outputs/dashboard/jfk_operational_risk_dashboard.html`
  A standalone offline interactive dashboard with charts and a readable data table.

## Notes

- The raw BTS source file is preserved unchanged.
- The cleaning logic removes rows with zero or missing arrival flights and rows where delayed arrivals exceed total arrivals.
- In this JFK dataset, no rows were removed by those rules, but the pipeline keeps them in place for reproducibility.
