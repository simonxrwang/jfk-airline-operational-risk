from __future__ import annotations

from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter, PercentFormatter


BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
OUTPUT_DIR = Path(__file__).resolve().parent / "figures"


COLORS = {
    "blue": "#2F6F9F",
    "teal": "#3B8B8C",
    "red": "#B64C4C",
    "gold": "#B58B3B",
    "purple": "#7666A5",
    "gray": "#4A4A4A",
    "light_gray": "#E7E7E7",
    "panel": "#F7F7F7",
}


def fmt_int(value: float) -> str:
    return f"{int(round(value)):,}"


def millions(value: float, _pos: int) -> str:
    return f"{value / 1_000_000:.1f}M"


def build_figure() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    core = pd.read_csv(PROCESSED_DIR / "jfk_airline_delay_core_cleaned.csv")
    monthly = pd.read_csv(PROCESSED_DIR / "jfk_monthly_risk_summary.csv", parse_dates=["period_start"])
    cause = pd.read_csv(PROCESSED_DIR / "jfk_delay_cause_summary.csv")
    airline = pd.read_csv(PROCESSED_DIR / "jfk_airline_risk_profile.csv")

    monthly["cancellation_rate"] = monthly["cancelled_arrivals"] / monthly["total_arrival_flights"]
    core["period_start"] = pd.to_datetime(
        core["year"].astype(str) + "-" + core["month"].astype(str).str.zfill(2) + "-01"
    )

    total_delay_minutes = int(core["total_arrival_delay_minutes"].sum())
    risk_blocks = pd.DataFrame(
        {
            "risk_block": ["Internal\noperating chain", "System /\nNAS", "External\nshock"],
            "delay_minutes": [
                core["airline_delay_minutes"].sum() + core["late_aircraft_delay_minutes"].sum(),
                core["nas_delay_minutes"].sum(),
                core["weather_delay_minutes"].sum() + core["security_delay_minutes"].sum(),
            ],
            "color": [COLORS["blue"], COLORS["gold"], COLORS["purple"]],
        }
    )
    risk_blocks["share"] = risk_blocks["delay_minutes"] / total_delay_minutes

    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["STIXGeneral", "DejaVu Serif", "Times New Roman", "Times"],
            "axes.titlesize": 10.5,
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "figure.dpi": 160,
            "savefig.dpi": 360,
            "axes.edgecolor": COLORS["gray"],
            "axes.linewidth": 0.7,
        }
    )

    fig = plt.figure(figsize=(11.2, 7.6), constrained_layout=False)
    gs = fig.add_gridspec(
        2,
        2,
        left=0.055,
        right=0.985,
        top=0.92,
        bottom=0.08,
        hspace=0.48,
        wspace=0.26,
    )

    fig.suptitle(
        "Data Processing and Descriptive Risk Evidence for JFK Airline Delays, 2020-2025",
        fontsize=14,
        fontweight="bold",
        y=0.975,
    )

    ax0 = fig.add_subplot(gs[0, 0])
    ax0.axis("off")
    ax0.set_title("A. Data-preparation workflow", loc="left", fontweight="bold", pad=6)

    workflow = [
        ("Raw BTS records", "570 JFK airline-month records"),
        ("Quality checks", "drop zero-flight records: 1\nlogic errors: 0"),
        ("Cleaned core panel", "569 records, 72 months,\n12 airlines"),
        ("Model-ready assets", "frequency, severity,\nrisk-block measures"),
    ]
    x_positions = [0.09, 0.36, 0.63, 0.90]
    for idx, ((title, body), x_pos) in enumerate(zip(workflow, x_positions, strict=True)):
        ax0.text(
            x_pos,
            0.62,
            title,
            ha="center",
            va="center",
            fontsize=8.8,
            fontweight="bold",
            color="white",
            bbox={
                "boxstyle": "round,pad=0.45,rounding_size=0.08",
                "facecolor": COLORS["blue"] if idx != 1 else COLORS["teal"],
                "edgecolor": "none",
            },
            transform=ax0.transAxes,
        )
        ax0.text(
            x_pos,
            0.38,
            body,
            ha="center",
            va="center",
            fontsize=8.2,
            color=COLORS["gray"],
            transform=ax0.transAxes,
        )
        if idx < len(workflow) - 1:
            ax0.annotate(
                "",
                xy=(x_positions[idx + 1] - 0.115, 0.62),
                xytext=(x_pos + 0.115, 0.62),
                xycoords=ax0.transAxes,
                arrowprops={"arrowstyle": "->", "lw": 1.2, "color": COLORS["gray"]},
            )
    ax0.text(
        0.02,
        0.08,
        "Core dataset retains airline-month frequency fields and delay-minute severity fields for later loss modeling.",
        ha="left",
        va="center",
        fontsize=8.2,
        color=COLORS["gray"],
        transform=ax0.transAxes,
    )

    ax1 = fig.add_subplot(gs[0, 1])
    ax1.set_title("B. Monthly disruption rates", loc="left", fontweight="bold", pad=6)
    ax1.plot(
        monthly["period_start"],
        monthly["delay_rate"],
        color=COLORS["blue"],
        lw=1.9,
        marker="o",
        ms=2.6,
        label="Delay rate",
    )
    ax1.plot(
        monthly["period_start"],
        monthly["cancellation_rate"],
        color=COLORS["red"],
        lw=1.6,
        marker="o",
        ms=2.2,
        label="Cancellation rate",
    )
    peak_delay = monthly.loc[monthly["delay_rate"].idxmax()]
    peak_cancel_rate = monthly.loc[monthly["cancellation_rate"].idxmax()]
    ax1.annotate(
        f"Peak delay rate\n{peak_delay['year_month']}: {peak_delay['delay_rate']:.1%}",
        xy=(peak_delay["period_start"], peak_delay["delay_rate"]),
        xytext=(-90, 24),
        textcoords="offset points",
        fontsize=7.8,
        arrowprops={"arrowstyle": "->", "lw": 0.9, "color": COLORS["gray"]},
        bbox={"boxstyle": "round,pad=0.28", "facecolor": "white", "edgecolor": COLORS["light_gray"]},
    )
    ax1.annotate(
        f"Peak cancellation rate\n{peak_cancel_rate['year_month']}: {peak_cancel_rate['cancellation_rate']:.1%}",
        xy=(peak_cancel_rate["period_start"], peak_cancel_rate["cancellation_rate"]),
        xytext=(42, -34),
        textcoords="offset points",
        fontsize=7.8,
        arrowprops={"arrowstyle": "->", "lw": 0.9, "color": COLORS["gray"]},
        bbox={"boxstyle": "round,pad=0.28", "facecolor": "white", "edgecolor": COLORS["light_gray"]},
    )
    ax1.yaxis.set_major_formatter(PercentFormatter(1.0))
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax1.set_xlim(monthly["period_start"].min(), monthly["period_start"].max())
    ax1.set_ylim(0, max(monthly["delay_rate"].max(), monthly["cancellation_rate"].max()) * 1.22)
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Share of arrival flights")
    ax1.grid(axis="y", color=COLORS["light_gray"], lw=0.7)
    ax1.legend(frameon=False, loc="upper left")

    ax2 = fig.add_subplot(gs[1, 0])
    ax2.set_title("C. Delay minutes by risk block", loc="left", fontweight="bold", pad=6)
    bars = ax2.barh(
        risk_blocks["risk_block"],
        risk_blocks["delay_minutes"],
        color=risk_blocks["color"],
        height=0.58,
    )
    for bar, (_, row) in zip(bars, risk_blocks.iterrows(), strict=True):
        ax2.text(
            bar.get_width() + total_delay_minutes * 0.012,
            bar.get_y() + bar.get_height() / 2,
            f"{row['share']:.1%}  ({row['delay_minutes'] / 1_000_000:.2f}M min)",
            va="center",
            ha="left",
            fontsize=8.2,
            color=COLORS["gray"],
        )
    ax2.set_xlim(0, risk_blocks["delay_minutes"].max() * 1.25)
    ax2.xaxis.set_major_formatter(FuncFormatter(millions))
    ax2.set_xlabel("Total delay minutes")
    ax2.grid(axis="x", color=COLORS["light_gray"], lw=0.7)
    ax2.invert_yaxis()

    ax3 = fig.add_subplot(gs[1, 1])
    ax3.set_title("D. Airline frequency-severity profile", loc="left", fontweight="bold", pad=6)
    size = 55 + 620 * (airline["total_arrival_flights"] / airline["total_arrival_flights"].max()) ** 0.7
    scatter = ax3.scatter(
        airline["delay_rate"],
        airline["average_delay_minutes_per_delayed_flight"],
        s=size,
        c=airline["cancellation_rate"],
        cmap="viridis",
        edgecolor="white",
        linewidth=0.8,
        alpha=0.92,
    )
    ax3.axvline(airline["delay_rate"].median(), color=COLORS["gray"], lw=0.9, ls="--", alpha=0.75)
    ax3.axhline(
        airline["average_delay_minutes_per_delayed_flight"].median(),
        color=COLORS["gray"],
        lw=0.9,
        ls="--",
        alpha=0.75,
    )
    label_airlines = {
        "JetBlue Airways",
        "Delta Air Lines",
        "American Airlines",
        "Endeavor Air",
        "Hawaiian Airlines",
        "Envoy Air",
        "Republic Airline",
    }
    offsets = {
        "JetBlue Airways": (18, 20),
        "Delta Air Lines": (-88, 6),
        "American Airlines": (-96, 16),
        "Endeavor Air": (-42, 14),
        "Hawaiian Airlines": (-72, 8),
        "Envoy Air": (-4, -23),
        "Republic Airline": (-62, -20),
    }
    for _, row in airline.iterrows():
        if row["airline_name"] in label_airlines:
            dx, dy = offsets[row["airline_name"]]
            ax3.annotate(
                row["airline_name"],
                xy=(row["delay_rate"], row["average_delay_minutes_per_delayed_flight"]),
                xytext=(dx, dy),
                textcoords="offset points",
                fontsize=7.7,
                color=COLORS["gray"],
                arrowprops={"arrowstyle": "-", "lw": 0.7, "color": COLORS["gray"], "alpha": 0.75},
            )
    ax3.xaxis.set_major_formatter(PercentFormatter(1.0))
    ax3.set_ylim(18, 97)
    ax3.set_xlabel("Delay rate")
    ax3.set_ylabel("Average delay minutes per delayed arrival")
    ax3.grid(color=COLORS["light_gray"], lw=0.7)
    cbar = fig.colorbar(scatter, ax=ax3, pad=0.012, fraction=0.046)
    cbar.ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    cbar.set_label("Cancellation rate", fontsize=7.6)

    for axis in [ax1, ax2, ax3]:
        axis.spines["top"].set_visible(False)
        axis.spines["right"].set_visible(False)

    note = (
        "Source: BTS On-Time Performance Airline Delay Cause data, JFK arrivals, 2020-2025. "
        "Bubble size in Panel D reflects total arrival flights."
    )
    fig.text(0.055, 0.025, note, fontsize=7.7, color=COLORS["gray"])

    output_stem = OUTPUT_DIR / "jfk_data_processing_risk_panel"
    fig.savefig(f"{output_stem}.png", bbox_inches="tight", facecolor="white")
    fig.savefig(f"{output_stem}.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    build_figure()
