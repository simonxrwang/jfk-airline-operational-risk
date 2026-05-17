# Figure Review and Redesign Notes

This note records why the final report uses `figures/jfk_data_processing_risk_panel.pdf`
instead of inserting the three earlier chart files separately.

## Existing Chart Review

`reports/charts/chart_1_monthly_trend.png` is useful for presentation because it
clearly marks the July 2023 delay peak and shows the pandemic cancellation shock.
For an academic report, however, the title and annotation are visually oversized,
the filled areas dominate the line evidence, and the count scale makes delay and
cancellation patterns less comparable when flight volume changes sharply.

`reports/charts/chart_2_delay_cause_breakdown.png` communicates the main result
well: Airline, Late Aircraft, and NAS explain most delay minutes. Its limitation
is that the donut and horizontal bars repeat the same information, creating a
wide figure with large blank space. The final report instead uses a compact
risk-block bar chart and leaves detailed cause shares to the table.

`reports/charts/chart_3_airline_risk_profile.png` is analytically valuable
because it combines delay rate, average delay severity, cancellation rate, and
operating scale. For report placement, it is too large as a standalone figure,
and several small-airline observations can visually overstate their importance.
The new figure keeps the frequency-severity scatter but labels only the most
interpretive airlines and explains that bubble size reflects total arrivals.

## Redesign Choice

The replacement figure is a four-panel academic-style figure:

- Panel A: reproducible data-preparation workflow.
- Panel B: monthly delay and cancellation rates, making time variation comparable.
- Panel C: delay minutes by operational risk block.
- Panel D: airline frequency-severity profile.

The figure uses a white background, restrained colors, smaller titles, a serif
font family close to Times, and PDF output for sharper LaTeX rendering.
