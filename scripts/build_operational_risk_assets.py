from __future__ import annotations

import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(BASE_DIR / ".cache" / "matplotlib"))

import matplotlib.dates as mdates
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, PowerNorm
from matplotlib.ticker import PercentFormatter
from plotly.offline.offline import get_plotlyjs

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
REPORTS_DIR = BASE_DIR / "reports"
CHART_DIR = REPORTS_DIR / "charts"
DASHBOARD_DIR = REPORTS_DIR / "dashboard"
SUMMARY_DIR = REPORTS_DIR / "summary"

RAW_CSV = RAW_DIR / "Airline_Delay_Cause.csv"
COLUMN_DEFINITIONS_XLSX = RAW_DIR / "Download_Column_Definitions.xlsx"

READABLE_FULL_STEM = "jfk_airline_delay_readable_full"
CLEANED_CORE_STEM = "jfk_airline_delay_core_cleaned"
COLUMN_DICTIONARY_STEM = "jfk_column_dictionary"
MONTHLY_SUMMARY_STEM = "jfk_monthly_risk_summary"
CAUSE_SUMMARY_STEM = "jfk_delay_cause_summary"
AIRLINE_PROFILE_STEM = "jfk_airline_risk_profile"
SUMMARY_NOTE_NAME = "jfk_descriptive_analysis_summary.md"

AIRLINE_NAME_FIXES = {
    "American Airlines Network": "American Airlines",
    "Alaska Airlines Network": "Alaska Airlines",
    "Delta Air Lines Network": "Delta Air Lines",
    "Endeavor Air Inc.": "Endeavor Air",
    "Hawaiian Airlines Network": "Hawaiian Airlines",
    "SkyWest Airlines Inc.": "SkyWest Airlines",
    "United Air Lines Network": "United Airlines",
}

READABLE_COLUMN_MAP = {
    "year": "year",
    "month": "month",
    "carrier_name": "airline_name",
    "airport": "airport_code",
    "airport_name": "airport_name",
    "arr_flights": "total_arrival_flights",
    "arr_del15": "delayed_arrivals_15_plus",
    "carrier_ct": "estimated_delayed_arrivals_due_to_airline",
    "weather_ct": "estimated_delayed_arrivals_due_to_weather",
    "nas_ct": "estimated_delayed_arrivals_due_to_nas",
    "security_ct": "estimated_delayed_arrivals_due_to_security",
    "late_aircraft_ct": "estimated_delayed_arrivals_due_to_late_aircraft",
    "arr_cancelled": "cancelled_arrivals",
    "arr_diverted": "diverted_arrivals",
    "arr_delay": "total_arrival_delay_minutes",
    "carrier_delay": "airline_delay_minutes",
    "weather_delay": "weather_delay_minutes",
    "nas_delay": "nas_delay_minutes",
    "security_delay": "security_delay_minutes",
    "late_aircraft_delay": "late_aircraft_delay_minutes",
}

READABLE_COLUMN_ORDER = [
    "year",
    "month",
    "airline_name",
    "airport_code",
    "airport_name",
    "total_arrival_flights",
    "delayed_arrivals_15_plus",
    "estimated_delayed_arrivals_due_to_airline",
    "estimated_delayed_arrivals_due_to_weather",
    "estimated_delayed_arrivals_due_to_nas",
    "estimated_delayed_arrivals_due_to_security",
    "estimated_delayed_arrivals_due_to_late_aircraft",
    "cancelled_arrivals",
    "diverted_arrivals",
    "total_arrival_delay_minutes",
    "airline_delay_minutes",
    "weather_delay_minutes",
    "nas_delay_minutes",
    "security_delay_minutes",
    "late_aircraft_delay_minutes",
]

CORE_COLUMNS = [
    "year",
    "month",
    "airline_name",
    "total_arrival_flights",
    "cancelled_arrivals",
    "diverted_arrivals",
    "delayed_arrivals_15_plus",
    "total_arrival_delay_minutes",
    "airline_delay_minutes",
    "weather_delay_minutes",
    "nas_delay_minutes",
    "security_delay_minutes",
    "late_aircraft_delay_minutes",
]

INTEGER_LIKE_COLUMNS = [
    "year",
    "month",
    "total_arrival_flights",
    "delayed_arrivals_15_plus",
    "cancelled_arrivals",
    "diverted_arrivals",
    "total_arrival_delay_minutes",
    "airline_delay_minutes",
    "weather_delay_minutes",
    "nas_delay_minutes",
    "security_delay_minutes",
    "late_aircraft_delay_minutes",
]

NUMERIC_COLUMNS = [
    "year",
    "month",
    "arr_flights",
    "arr_del15",
    "carrier_ct",
    "weather_ct",
    "nas_ct",
    "security_ct",
    "late_aircraft_ct",
    "arr_cancelled",
    "arr_diverted",
    "arr_delay",
    "carrier_delay",
    "weather_delay",
    "nas_delay",
    "security_delay",
    "late_aircraft_delay",
]

CAUSE_COLUMNS = [
    "airline_delay_minutes",
    "weather_delay_minutes",
    "nas_delay_minutes",
    "security_delay_minutes",
    "late_aircraft_delay_minutes",
]

CAUSE_LABELS = {
    "airline_delay_minutes": "Airline",
    "weather_delay_minutes": "Weather",
    "nas_delay_minutes": "NAS",
    "security_delay_minutes": "Security",
    "late_aircraft_delay_minutes": "Late Aircraft",
}

CHART_COLORS = {
    "pale_blue": "#D1DFE6",
    "primary": "#3F74A3",
    "accent": "#699BC5",
    "brown": "#794E47",
    "tan": "#9C7B57",
    "mauve": "#A78F95",
    "red": "#B54646",
    "rose": "#D18F90",
    "ink": "#1F1F1F",
    "slate": "#3E3A39",
    "muted": "#794E47",
    "sand": "#FBFAF7",
    "grid": "#D1DFE6",
}

CATEGORY_COLORS = [
    CHART_COLORS["primary"],
    CHART_COLORS["accent"],
    CHART_COLORS["brown"],
    CHART_COLORS["tan"],
    CHART_COLORS["mauve"],
    CHART_COLORS["red"],
    CHART_COLORS["rose"],
    CHART_COLORS["pale_blue"],
]

CAUSE_COLOR_MAP = {
    "Airline": CHART_COLORS["primary"],
    "Weather": CHART_COLORS["accent"],
    "NAS": CHART_COLORS["tan"],
    "Security": CHART_COLORS["red"],
    "Late Aircraft": CHART_COLORS["rose"],
}

AIRLINE_LABEL_OFFSETS = {
    "Alaska Airlines": (-18, -14),
    "American Airlines": (26, 14),
    "Delta Air Lines": (-24, 16),
    "Endeavor Air": (-24, 12),
    "Envoy Air": (0, 16),
    "Frontier Airlines": (22, 12),
    "Hawaiian Airlines": (-28, 0),
    "JetBlue Airways": (0, 16),
    "Piedmont Airlines": (-20, -16),
    "Republic Airline": (-24, -14),
    "SkyWest Airlines": (24, -16),
    "United Airlines": (24, -12),
}

COLUMN_METADATA = {
    "year": {
        "category": "Time",
        "plain_english_meaning": "Calendar year covered by the monthly airline record.",
        "chinese_meaning": "该条月度航司记录对应的年份。",
        "kept_in_core_dataset": "Yes",
    },
    "month": {
        "category": "Time",
        "plain_english_meaning": "Calendar month of the record, from 1 to 12.",
        "chinese_meaning": "该条记录对应的月份，取值为 1 到 12。",
        "kept_in_core_dataset": "Yes",
    },
    "carrier": {
        "category": "Airline",
        "plain_english_meaning": "DOT airline code. The readable output replaces this code with the full airline name.",
        "chinese_meaning": "美国 DOT 的航司代码。可读版数据已用完整航司名称替代该缩写。",
        "kept_in_core_dataset": "No",
    },
    "carrier_name": {
        "category": "Airline",
        "plain_english_meaning": "Full airline name used as the main airline identifier in the cleaned dataset.",
        "chinese_meaning": "完整航司名称，在清洗后的核心数据中作为主要航司标识使用。",
        "kept_in_core_dataset": "Yes",
    },
    "airport": {
        "category": "Airport",
        "plain_english_meaning": "Airport code for the arrival airport. This dataset only contains JFK.",
        "chinese_meaning": "到达机场代码。本数据集中该字段恒为 JFK。",
        "kept_in_core_dataset": "No",
    },
    "airport_name": {
        "category": "Airport",
        "plain_english_meaning": "Full airport name for the arrival airport. This dataset only contains JFK.",
        "chinese_meaning": "到达机场全称。本数据集中该字段恒为 JFK 机场。",
        "kept_in_core_dataset": "No",
    },
    "arr_flights": {
        "category": "Flight Volume",
        "plain_english_meaning": "Total number of arrival flights operated by the airline at JFK in that month.",
        "chinese_meaning": "该航司在该月于 JFK 的总到达航班量。",
        "kept_in_core_dataset": "Yes",
    },
    "arr_del15": {
        "category": "Delay Frequency",
        "plain_english_meaning": "Number of arrival flights delayed by 15 minutes or more in that month.",
        "chinese_meaning": "该月到达延误超过 15 分钟的航班数量。",
        "kept_in_core_dataset": "Yes",
    },
    "carrier_ct": {
        "category": "Delay Frequency",
        "plain_english_meaning": "Estimated delayed-flight count attributed to airline-caused issues. BTS allocates these counts, so decimals can appear.",
        "chinese_meaning": "因航司自身原因导致的估算延误班次数。由于 BTS 采用分摊口径，所以这里可能出现小数。",
        "kept_in_core_dataset": "No",
    },
    "weather_ct": {
        "category": "Delay Frequency",
        "plain_english_meaning": "Estimated delayed-flight count attributed to weather. Decimals can appear because BTS uses prorated counts.",
        "chinese_meaning": "因天气导致的估算延误班次数。由于 BTS 采用分摊口径，所以这里可能出现小数。",
        "kept_in_core_dataset": "No",
    },
    "nas_ct": {
        "category": "Delay Frequency",
        "plain_english_meaning": "Estimated delayed-flight count attributed to NAS, the National Air System.",
        "chinese_meaning": "因 NAS（National Air System，美国国家空域系统）导致的估算延误班次数。",
        "kept_in_core_dataset": "No",
    },
    "security_ct": {
        "category": "Delay Frequency",
        "plain_english_meaning": "Estimated delayed-flight count attributed to security-related issues.",
        "chinese_meaning": "因安保相关原因导致的估算延误班次数。",
        "kept_in_core_dataset": "No",
    },
    "late_aircraft_ct": {
        "category": "Delay Frequency",
        "plain_english_meaning": "Estimated delayed-flight count caused by inbound aircraft arriving late.",
        "chinese_meaning": "因前序航班飞机晚到而导致的估算延误班次数。",
        "kept_in_core_dataset": "No",
    },
    "arr_cancelled": {
        "category": "Disruption",
        "plain_english_meaning": "Number of arrivals cancelled by the airline in that month.",
        "chinese_meaning": "该航司在该月取消的到达航班数量。",
        "kept_in_core_dataset": "Yes",
    },
    "arr_diverted": {
        "category": "Disruption",
        "plain_english_meaning": "Number of flights diverted away from the planned arrival airport in that month.",
        "chinese_meaning": "该航司在该月发生备降或改降的航班数量。",
        "kept_in_core_dataset": "Yes",
    },
    "arr_delay": {
        "category": "Delay Severity",
        "plain_english_meaning": "Total arrival delay minutes accumulated across all flights in that month.",
        "chinese_meaning": "该航司在该月累计发生的总到达延误分钟数。",
        "kept_in_core_dataset": "Yes",
    },
    "carrier_delay": {
        "category": "Delay Severity",
        "plain_english_meaning": "Delay minutes caused by airline or carrier-controlled issues.",
        "chinese_meaning": "由航司自身可控原因造成的延误分钟数。",
        "kept_in_core_dataset": "Yes",
    },
    "weather_delay": {
        "category": "Delay Severity",
        "plain_english_meaning": "Delay minutes caused by weather conditions.",
        "chinese_meaning": "由天气原因造成的延误分钟数。",
        "kept_in_core_dataset": "Yes",
    },
    "nas_delay": {
        "category": "Delay Severity",
        "plain_english_meaning": "Delay minutes caused by NAS constraints such as air traffic flow or airport congestion.",
        "chinese_meaning": "由 NAS 约束导致的延误分钟数，例如空管流量控制或机场拥堵。",
        "kept_in_core_dataset": "Yes",
    },
    "security_delay": {
        "category": "Delay Severity",
        "plain_english_meaning": "Delay minutes caused by security-related issues.",
        "chinese_meaning": "由安保相关原因造成的延误分钟数。",
        "kept_in_core_dataset": "Yes",
    },
    "late_aircraft_delay": {
        "category": "Delay Severity",
        "plain_english_meaning": "Delay minutes caused by a late inbound aircraft creating knock-on delays.",
        "chinese_meaning": "因前序航班晚到引发连锁反应而造成的延误分钟数。",
        "kept_in_core_dataset": "Yes",
    },
}


def ensure_output_directories() -> None:
    for directory in (PROCESSED_DIR, CHART_DIR, DASHBOARD_DIR, SUMMARY_DIR):
        directory.mkdir(parents=True, exist_ok=True)


def save_dataframe(df: pd.DataFrame, stem: str) -> None:
    df.to_csv(PROCESSED_DIR / f"{stem}.csv", index=False)
    df.to_excel(PROCESSED_DIR / f"{stem}.xlsx", index=False)


def load_raw_data() -> pd.DataFrame:
    df = pd.read_csv(RAW_CSV)
    df["carrier_name"] = df["carrier_name"].replace(AIRLINE_NAME_FIXES)
    df["airport_name"] = df["airport_name"].replace(
        {"New York, NY: John F. Kennedy International": "John F. Kennedy International Airport (JFK)"}
    )

    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df["year"] = df["year"].astype("Int64")
    df["month"] = df["month"].astype("Int64")
    df = df.sort_values(["year", "month", "carrier_name"]).reset_index(drop=True)
    return df


def build_column_dictionary() -> pd.DataFrame:
    definitions = pd.read_excel(COLUMN_DEFINITIONS_XLSX)
    definitions.columns = ["original_column", "bts_definition"]
    definitions["readable_column"] = definitions["original_column"].map(
        lambda column: READABLE_COLUMN_MAP.get(column, "replaced_by_airline_name" if column == "carrier" else column)
    )
    definitions["category"] = definitions["original_column"].map(lambda column: COLUMN_METADATA[column]["category"])
    definitions["plain_english_meaning"] = definitions["original_column"].map(
        lambda column: COLUMN_METADATA[column]["plain_english_meaning"]
    )
    definitions["chinese_meaning"] = definitions["original_column"].map(
        lambda column: COLUMN_METADATA[column]["chinese_meaning"]
    )
    definitions["kept_in_core_dataset"] = definitions["original_column"].map(
        lambda column: COLUMN_METADATA[column]["kept_in_core_dataset"]
    )
    return definitions[
        [
            "original_column",
            "readable_column",
            "category",
            "kept_in_core_dataset",
            "plain_english_meaning",
            "chinese_meaning",
            "bts_definition",
        ]
    ]


def build_readable_full_dataset(raw_df: pd.DataFrame) -> pd.DataFrame:
    readable_df = raw_df.drop(columns=["carrier"]).rename(columns=READABLE_COLUMN_MAP)
    readable_df = readable_df[READABLE_COLUMN_ORDER].copy()
    readable_df[INTEGER_LIKE_COLUMNS] = readable_df[INTEGER_LIKE_COLUMNS].astype("Int64")
    return readable_df


def clean_core_dataset(readable_full_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, int]]:
    cleaned = readable_full_df[CORE_COLUMNS].copy()

    initial_rows = len(cleaned)
    flights_zero_or_missing = cleaned["total_arrival_flights"].isna() | (cleaned["total_arrival_flights"] <= 0)
    removed_for_no_operations = int(flights_zero_or_missing.sum())
    cleaned = cleaned.loc[~flights_zero_or_missing].copy()

    fill_zero_columns = [
        "cancelled_arrivals",
        "diverted_arrivals",
        "delayed_arrivals_15_plus",
        "total_arrival_delay_minutes",
        "airline_delay_minutes",
        "weather_delay_minutes",
        "nas_delay_minutes",
        "security_delay_minutes",
        "late_aircraft_delay_minutes",
    ]
    cleaned[fill_zero_columns] = cleaned[fill_zero_columns].fillna(0)

    invalid_delay_rows = cleaned["delayed_arrivals_15_plus"] > cleaned["total_arrival_flights"]
    removed_for_logic_issue = int(invalid_delay_rows.sum())
    cleaned = cleaned.loc[~invalid_delay_rows].copy()

    cleaned[INTEGER_LIKE_COLUMNS] = cleaned[INTEGER_LIKE_COLUMNS].astype(int)
    cleaned = cleaned.sort_values(["year", "month", "airline_name"]).reset_index(drop=True)

    summary = {
        "initial_rows": int(initial_rows),
        "removed_for_no_operations": removed_for_no_operations,
        "removed_for_logic_issue": removed_for_logic_issue,
        "final_rows": int(len(cleaned)),
    }
    return cleaned, summary


def build_summaries(cleaned_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    monthly_summary = (
        cleaned_df.groupby(["year", "month"], as_index=False)[
            ["delayed_arrivals_15_plus", "cancelled_arrivals", "total_arrival_flights", "total_arrival_delay_minutes"]
        ]
        .sum()
        .sort_values(["year", "month"])
    )
    monthly_summary["year_month"] = (
        monthly_summary["year"].astype(str) + "-" + monthly_summary["month"].astype(str).str.zfill(2)
    )
    monthly_summary["period_start"] = pd.to_datetime(
        monthly_summary["year_month"] + "-01",
        format="%Y-%m-%d",
    )
    monthly_summary["delay_rate"] = (
        monthly_summary["delayed_arrivals_15_plus"] / monthly_summary["total_arrival_flights"]
    )

    cause_summary = pd.DataFrame(
        {
            "cause": [CAUSE_LABELS[column] for column in CAUSE_COLUMNS],
            "delay_minutes": [cleaned_df[column].sum() for column in CAUSE_COLUMNS],
        }
    )
    cause_summary["share_of_total_delay_minutes"] = (
        cause_summary["delay_minutes"] / cause_summary["delay_minutes"].sum()
    )
    cause_summary = cause_summary.sort_values("delay_minutes", ascending=False).reset_index(drop=True)

    airline_profile = (
        cleaned_df.groupby("airline_name", as_index=False)[
            [
                "total_arrival_flights",
                "delayed_arrivals_15_plus",
                "cancelled_arrivals",
                "diverted_arrivals",
                "total_arrival_delay_minutes",
                "airline_delay_minutes",
                "weather_delay_minutes",
                "nas_delay_minutes",
                "security_delay_minutes",
                "late_aircraft_delay_minutes",
            ]
        ]
        .sum()
        .sort_values("airline_name")
    )
    airline_profile["delay_rate"] = (
        airline_profile["delayed_arrivals_15_plus"] / airline_profile["total_arrival_flights"]
    )
    airline_profile["cancellation_rate"] = (
        airline_profile["cancelled_arrivals"] / airline_profile["total_arrival_flights"]
    )
    airline_profile["average_delay_minutes_per_delayed_flight"] = np.where(
        airline_profile["delayed_arrivals_15_plus"] > 0,
        airline_profile["total_arrival_delay_minutes"] / airline_profile["delayed_arrivals_15_plus"],
        0,
    )
    return monthly_summary, cause_summary, airline_profile


def apply_chart_style() -> None:
    sns.set_theme(
        style="whitegrid",
        rc={
            "axes.facecolor": "none",
            "figure.facecolor": "none",
            "grid.color": CHART_COLORS["grid"],
            "axes.edgecolor": CHART_COLORS["grid"],
            "axes.labelcolor": CHART_COLORS["slate"],
            "xtick.color": CHART_COLORS["slate"],
            "ytick.color": CHART_COLORS["slate"],
            "text.color": CHART_COLORS["slate"],
            "font.family": "DejaVu Sans",
            "axes.titlesize": 16,
            "axes.labelsize": 11,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "legend.fontsize": 11,
        },
    )
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "svg.fonttype": "path",
            "pdf.fonttype": 42,
            "axes.titlecolor": CHART_COLORS["ink"],
        }
    )


def save_chart(fig: plt.Figure, filename: str, *, bbox_inches: str | None = "tight") -> None:
    fig.patch.set_alpha(0)
    for axis in fig.axes:
        axis.patch.set_alpha(0)
    fig.savefig(CHART_DIR / f"{filename}.png", dpi=320, bbox_inches=bbox_inches, transparent=True)
    fig.savefig(CHART_DIR / f"{filename}.svg", bbox_inches=bbox_inches, transparent=True)
    plt.close(fig)


def create_monthly_trend_chart(monthly_summary: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(15, 7))
    period_dates = monthly_summary["period_start"]

    ax.plot(
        period_dates,
        monthly_summary["delayed_arrivals_15_plus"],
        color=CHART_COLORS["primary"],
        marker="o",
        markersize=4.5,
        linewidth=2.6,
        label="Delayed arrivals (15+ min)",
    )
    ax.plot(
        period_dates,
        monthly_summary["cancelled_arrivals"],
        color=CHART_COLORS["red"],
        marker="o",
        markersize=4.5,
        linewidth=2.6,
        label="Cancelled arrivals",
    )
    ax.fill_between(period_dates, monthly_summary["delayed_arrivals_15_plus"], color=CHART_COLORS["primary"], alpha=0.10)
    ax.fill_between(period_dates, monthly_summary["cancelled_arrivals"], color=CHART_COLORS["red"], alpha=0.12)

    peak_delay = monthly_summary.loc[monthly_summary["delayed_arrivals_15_plus"].idxmax()]
    median_period = monthly_summary["period_start"].median()
    text_offset = (-104, 12) if peak_delay["period_start"] > median_period else (30, 12)
    horizontal_alignment = "right" if peak_delay["period_start"] > median_period else "left"
    ax.set_ylim(
        bottom=0,
        top=max(
            monthly_summary["delayed_arrivals_15_plus"].max(),
            monthly_summary["cancelled_arrivals"].max(),
        )
        * 1.16,
    )
    ax.annotate(
        f"Peak delays: {peak_delay['year_month']}\n{int(round(peak_delay['delayed_arrivals_15_plus'])):,}",
        xy=(peak_delay["period_start"], peak_delay["delayed_arrivals_15_plus"]),
        xytext=text_offset,
        textcoords="offset points",
        fontsize=10.5,
        ha=horizontal_alignment,
        va="bottom",
        color=CHART_COLORS["slate"],
        arrowprops={"arrowstyle": "->", "color": CHART_COLORS["slate"], "lw": 1.3},
        bbox={"boxstyle": "round,pad=0.4", "facecolor": "white", "edgecolor": CHART_COLORS["grid"]},
    )

    ax.set_title("Chart 1. Monthly Delay and Cancellation Trend at JFK", fontsize=18, fontweight="bold", loc="left")
    ax.set_xlabel("Year-Month")
    ax.set_ylabel("Flights")
    ax.set_xlim(period_dates.min(), period_dates.max())
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=3))
    ax.legend(frameon=False, loc="upper left")
    sns.despine(ax=ax)
    fig.autofmt_xdate(rotation=0)
    save_chart(fig, "chart_1_monthly_trend")


def create_delay_cause_chart(cause_summary: pd.DataFrame) -> None:
    chart_data = cause_summary.sort_values("delay_minutes", ascending=True)
    fig = plt.figure(figsize=(12.2, 4.6))
    fig.subplots_adjust(left=0.06, right=0.97, top=0.86, bottom=0.14, wspace=0.18)
    grid = fig.add_gridspec(1, 2, width_ratios=[0.88, 1.7])
    donut_ax = fig.add_subplot(grid[0, 0])
    bar_ax = fig.add_subplot(grid[0, 1])

    palette = [CAUSE_COLOR_MAP[cause] for cause in cause_summary["cause"]]
    total_delay_minutes = int(cause_summary["delay_minutes"].sum())
    _, _, autotexts = donut_ax.pie(
        cause_summary["delay_minutes"],
        colors=palette,
        radius=0.9,
        startangle=110,
        counterclock=False,
        autopct=lambda pct: f"{pct:.1f}%" if pct >= 5 else "",
        pctdistance=0.72,
        wedgeprops={"width": 0.33, "edgecolor": "white", "linewidth": 2.4},
        textprops={"color": CHART_COLORS["slate"], "fontsize": 10, "fontweight": "bold"},
    )

    for autotext in autotexts:
        autotext.set_color("white")
        autotext.set_fontsize(9.5)
        autotext.set_fontweight("bold")

    donut_ax.text(
        0,
        0.05,
        f"{total_delay_minutes / 1_000_000:.2f}M",
        ha="center",
        va="center",
        fontsize=18,
        fontweight="bold",
        color=CHART_COLORS["primary"],
    )
    donut_ax.text(
        0,
        -0.14,
        "total delay\nminutes",
        ha="center",
        va="center",
        fontsize=9.5,
        color=CHART_COLORS["slate"],
        linespacing=1.25,
    )
    donut_ax.set_aspect("equal", adjustable="box")
    donut_ax.set_title("Delay minutes", fontsize=11.5, fontweight="bold", color=CHART_COLORS["slate"], pad=8)

    shares = chart_data["share_of_total_delay_minutes"]
    bar_colors = [CAUSE_COLOR_MAP[cause] for cause in chart_data["cause"]]
    bars = bar_ax.barh(chart_data["cause"], shares, color=bar_colors, height=0.58)
    bar_ax.set_title("Chart 2. Delay Cause Breakdown by Share of Delay Minutes", fontsize=14.5, fontweight="bold", loc="left")
    bar_ax.set_xlim(0, shares.max() * 1.24)
    bar_ax.xaxis.set_major_formatter(PercentFormatter(1.0))
    bar_ax.tick_params(axis="y", labelsize=10.5)
    bar_ax.tick_params(axis="x", labelsize=9.5, colors=CHART_COLORS["slate"])
    bar_ax.grid(axis="x", color=CHART_COLORS["grid"], linewidth=0.8, alpha=0.6)
    bar_ax.set_axisbelow(True)
    for bar, (_, row) in zip(bars, chart_data.iterrows(), strict=True):
        x_position = bar.get_width()
        bar_ax.text(
            x_position + shares.max() * 0.025,
            bar.get_y() + bar.get_height() / 2,
            f"{row['share_of_total_delay_minutes']:.1%}  ({row['delay_minutes'] / 1_000_000:.2f}M min)",
            va="center",
            ha="left",
            fontsize=10,
            color=CHART_COLORS["slate"],
        )
    sns.despine(ax=bar_ax, left=True, bottom=False)
    save_chart(fig, "chart_2_delay_cause_breakdown")


def create_airline_risk_chart(airline_profile: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(13.5, 8))
    max_flights = airline_profile["total_arrival_flights"].max()
    marker_sizes = 280 + (airline_profile["total_arrival_flights"] / max_flights) * 1000
    risk_cmap = LinearSegmentedColormap.from_list(
        "jfk_risk_palette",
        [
            CHART_COLORS["accent"],
            CHART_COLORS["primary"],
            CHART_COLORS["tan"],
            CHART_COLORS["brown"],
            CHART_COLORS["red"],
        ],
    )
    color_norm = PowerNorm(
        gamma=0.55,
        vmin=airline_profile["cancellation_rate"].min(),
        vmax=airline_profile["cancellation_rate"].max(),
    )

    scatter = ax.scatter(
        airline_profile["delay_rate"],
        airline_profile["average_delay_minutes_per_delayed_flight"],
        s=marker_sizes,
        c=airline_profile["cancellation_rate"],
        cmap=risk_cmap,
        norm=color_norm,
        alpha=0.96,
        edgecolor=CHART_COLORS["ink"],
        linewidth=1.1,
    )

    median_delay_rate = airline_profile["delay_rate"].median()
    median_avg_minutes = airline_profile["average_delay_minutes_per_delayed_flight"].median()
    ax.axvline(median_delay_rate, color=CHART_COLORS["slate"], linestyle="--", linewidth=1.3, alpha=0.8)
    ax.axhline(median_avg_minutes, color=CHART_COLORS["slate"], linestyle="--", linewidth=1.3, alpha=0.8)

    for _, row in airline_profile.iterrows():
        offset = AIRLINE_LABEL_OFFSETS.get(row["airline_name"], (0, 12))
        label = ax.annotate(
            row["airline_name"],
            xy=(row["delay_rate"], row["average_delay_minutes_per_delayed_flight"]),
            xytext=offset,
            textcoords="offset points",
            fontsize=8.0,
            ha="center",
            va="center",
            color=CHART_COLORS["slate"],
            fontweight="bold",
            clip_on=False,
            arrowprops={
                "arrowstyle": "-",
                "color": CHART_COLORS["grid"],
                "lw": 0.85,
                "alpha": 0.9,
            },
            bbox={
                "boxstyle": "round,pad=0.16",
                "facecolor": "white",
                "edgecolor": "none",
                "alpha": 0.82,
            },
        )
        label.set_path_effects([pe.withStroke(linewidth=1.8, foreground="white")])

    ax.set_title("Chart 3. Airline Risk Profiling at JFK", fontsize=18, fontweight="bold", loc="left")
    ax.set_xlabel("Delay rate = delayed arrivals / total arrivals")
    ax.set_ylabel("Average delay minutes per delayed flight")
    ax.xaxis.set_major_formatter(PercentFormatter(1.0))
    ax.margins(x=0.13, y=0.18)

    colorbar = fig.colorbar(scatter, ax=ax, pad=0.02)
    colorbar.ax.set_title("Cancellation rate", color=CHART_COLORS["slate"], fontsize=10, pad=10)
    colorbar.ax.yaxis.set_major_formatter(PercentFormatter(1.0))

    sns.despine(ax=ax)
    save_chart(fig, "chart_3_airline_risk_profile")


def build_dashboard(
    readable_full_df: pd.DataFrame,
    cleaned_df: pd.DataFrame,
    airline_profile: pd.DataFrame,
    cleaning_summary: dict[str, int],
) -> None:
    plotly_js = get_plotlyjs()
    table_columns = list(readable_full_df.columns)

    table_records = json.loads(readable_full_df.to_json(orient="records", force_ascii=False))
    core_records = json.loads(cleaned_df.to_json(orient="records", force_ascii=False))
    airline_records = json.loads(airline_profile.to_json(orient="records", force_ascii=False))
    cleaned_periods = cleaned_df.assign(
        year_month=cleaned_df["year"].astype(str) + "-" + cleaned_df["month"].astype(str).str.zfill(2)
    )["year_month"]
    data_scope = f"All airlines at JFK, {cleaned_periods.min()} to {cleaned_periods.max()}"

    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>JFK Operational Risk Dashboard</title>
  <style>
    :root {
      --bg: #fbfaf7;
      --panel: #fffdf8;
      --ink: #1f1f1f;
      --muted: #794e47;
      --line: #d1dfe6;
      --primary: #3f74a3;
      --secondary: #b54646;
      --accent: #699bc5;
      --gold: #9c7b57;
      --mauve: #a78f95;
      --red: #b54646;
      --rose: #d18f90;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: linear-gradient(180deg, rgba(209, 223, 230, 0.42) 0%, #fbfaf7 62%);
      color: var(--ink);
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    }
    .page {
      max-width: 1480px;
      margin: 0 auto;
      padding: 28px 24px 40px;
    }
    .hero {
      display: grid;
      grid-template-columns: 2.2fr 1fr;
      gap: 18px;
      margin-bottom: 18px;
    }
    .hero-panel,
    .panel {
      background: rgba(255, 253, 248, 0.92);
      border: 1px solid var(--line);
      border-radius: 20px;
      box-shadow: 0 14px 28px rgba(50, 50, 50, 0.08);
    }
    .hero-panel {
      padding: 28px 30px;
      background:
        radial-gradient(circle at top right, rgba(209, 143, 144, 0.20), transparent 30%),
        radial-gradient(circle at bottom left, rgba(63, 116, 163, 0.16), transparent 34%),
        rgba(255, 253, 248, 0.94);
    }
    h1 {
      margin: 0 0 10px;
      font-size: 2.1rem;
      line-height: 1.08;
      letter-spacing: -0.02em;
    }
    .hero-copy {
      margin: 0;
      color: var(--muted);
      line-height: 1.6;
      font-size: 1rem;
    }
    .meta-panel {
      padding: 24px 26px;
      display: grid;
      gap: 14px;
      align-content: center;
    }
    .meta-item .label {
      display: block;
      color: var(--muted);
      font-size: 0.88rem;
      margin-bottom: 4px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    .meta-item .value {
      font-size: 1.05rem;
      font-weight: 600;
    }
    .controls {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
      margin-bottom: 18px;
    }
    .control-panel {
      padding: 18px 20px;
    }
    .control-row {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
    }
    label {
      font-size: 0.92rem;
      font-weight: 600;
      color: var(--muted);
    }
    select,
    input {
      padding: 11px 12px;
      border-radius: 12px;
      border: 1px solid var(--line);
      background: white;
      min-width: 220px;
      font-size: 0.96rem;
      color: var(--ink);
    }
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(5, minmax(0, 1fr));
      gap: 14px;
      margin-bottom: 18px;
    }
    .kpi-card {
      padding: 18px 18px 16px;
      border-radius: 18px;
      border: 1px solid var(--line);
      background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(250,247,241,0.95));
      box-shadow: 0 10px 20px rgba(15, 76, 92, 0.05);
    }
    .kpi-label {
      color: var(--muted);
      font-size: 0.86rem;
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .kpi-value {
      font-size: 1.6rem;
      font-weight: 700;
      line-height: 1.1;
    }
    .kpi-sub {
      margin-top: 7px;
      color: var(--muted);
      font-size: 0.88rem;
    }
    .chart-grid {
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 18px;
      margin-bottom: 18px;
    }
    .chart-grid-bottom {
      display: grid;
      grid-template-columns: 1fr;
      gap: 18px;
      margin-bottom: 18px;
    }
    .panel-header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      gap: 12px;
      padding: 18px 20px 0;
    }
    .panel-header h2 {
      margin: 0;
      font-size: 1.1rem;
    }
    .panel-note {
      color: var(--muted);
      font-size: 0.88rem;
    }
    .plot {
      min-height: 420px;
      padding: 4px 8px 12px;
    }
    .plot.tall {
      min-height: 520px;
    }
    .table-panel {
      padding: 0 20px 20px;
    }
    .table-wrap {
      margin-top: 12px;
      border: 1px solid var(--line);
      border-radius: 16px;
      overflow: auto;
      max-height: 520px;
      background: white;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 1200px;
    }
    thead {
      position: sticky;
      top: 0;
      z-index: 1;
    }
    th {
      background: #f0eadf;
      color: var(--ink);
      padding: 11px 10px;
      text-align: left;
      border-bottom: 1px solid var(--line);
      white-space: nowrap;
    }
    td {
      padding: 10px;
      border-bottom: 1px solid #efe7d8;
      color: var(--ink);
      white-space: nowrap;
    }
    tbody tr:nth-child(even) {
      background: #fcfaf5;
    }
    .footer-note {
      color: var(--muted);
      font-size: 0.88rem;
      margin-top: 10px;
    }
    @media (max-width: 1100px) {
      .hero,
      .controls,
      .chart-grid,
      .kpi-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
  <script>__PLOTLY_JS__</script>
</head>
<body>
  <div class="page">
    <section class="hero">
      <div class="hero-panel">
        <h1>JFK Airline Delay and Cancellation Dashboard</h1>
        <p class="hero-copy">
          Offline interactive dashboard built from BTS On-Time Performance data for JFK.
          Use the airline filter to inspect monthly disruption frequency, delay-cause severity,
          airline risk positioning, and the readable source table without needing a Python runtime.
        </p>
      </div>
      <div class="hero-panel meta-panel">
        <div class="meta-item">
          <span class="label">Dataset scope</span>
          <span class="value">__DATA_SCOPE__</span>
        </div>
        <div class="meta-item">
          <span class="label">Rows after cleaning</span>
          <span class="value">__FINAL_ROWS__</span>
        </div>
        <div class="meta-item">
          <span class="label">Cleaning result</span>
          <span class="value">Removed no-op rows: __REMOVED_NO_OPS__; logic issues: __REMOVED_LOGIC__</span>
        </div>
      </div>
    </section>

    <section class="controls">
      <div class="panel control-panel">
        <div class="control-row">
          <label for="airlineFilter">Airline filter</label>
          <select id="airlineFilter"></select>
        </div>
      </div>
      <div class="panel control-panel">
        <div class="control-row">
          <label for="tableSearch">Search readable data table</label>
          <input id="tableSearch" type="text" placeholder="Type airline, month, or metric name">
        </div>
      </div>
    </section>

    <section class="kpi-grid" id="kpiGrid"></section>

    <section class="chart-grid">
      <div class="panel">
        <div class="panel-header">
          <h2>Monthly disruption trend</h2>
          <span class="panel-note">Delayed arrivals vs cancelled arrivals</span>
        </div>
        <div id="monthlyTrend" class="plot"></div>
      </div>
      <div class="panel">
        <div class="panel-header">
          <h2>Delay cause mix</h2>
          <span class="panel-note">Share of total delay minutes</span>
        </div>
        <div id="causeBreakdown" class="plot"></div>
      </div>
    </section>

    <section class="chart-grid-bottom">
      <div class="panel">
        <div class="panel-header">
          <h2>Airline risk profile</h2>
          <span class="panel-note">Bubble size reflects total arrival flights</span>
        </div>
        <div id="airlineRisk" class="plot tall"></div>
      </div>
    </section>

    <section class="panel table-panel">
      <div class="panel-header">
        <h2>Readable source data table</h2>
        <span class="panel-note" id="tableCount"></span>
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr id="tableHead"></tr></thead>
          <tbody id="tableBody"></tbody>
        </table>
      </div>
      <div class="footer-note">
        This HTML file is fully self-contained and can be opened directly in a browser without Python.
      </div>
    </section>
  </div>

  <script>
    const readableData = __TABLE_DATA__;
    const coreData = __CORE_DATA__;
    const airlineRiskData = __AIRLINE_RISK_DATA__;
    const tableColumns = __TABLE_COLUMNS__;
    const chartFont = "Segoe UI, Helvetica Neue, Arial, sans-serif";
    const airlinePalette = ["#3F74A3", "#699BC5", "#794E47", "#9C7B57", "#A78F95", "#B54646", "#D18F90", "#D1DFE6"];
    const causeColumns = [
      { key: "airline_delay_minutes", label: "Airline", color: "#3F74A3" },
      { key: "weather_delay_minutes", label: "Weather", color: "#699BC5" },
      { key: "nas_delay_minutes", label: "NAS", color: "#9C7B57" },
      { key: "security_delay_minutes", label: "Security", color: "#B54646" },
      { key: "late_aircraft_delay_minutes", label: "Late Aircraft", color: "#D18F90" }
    ];
    const airlineFilter = document.getElementById("airlineFilter");
    const tableSearch = document.getElementById("tableSearch");

    function getPeriod(row) {
      return `${row.year}-${String(row.month).padStart(2, "0")}`;
    }

    const allPeriods = [...new Set(coreData.map(row => getPeriod(row)))].sort();

    function formatInteger(value) {
      return Math.round(value).toLocaleString("en-US");
    }

    function formatMinutes(value) {
      return `${Math.round(value).toLocaleString("en-US")} min`;
    }

    function formatPercent(value) {
      return `${(value * 100).toFixed(1)}%`;
    }

    function getUniqueAirlines() {
      const airlines = [...new Set(coreData.map(row => row.airline_name))];
      return airlines.sort((a, b) => a.localeCompare(b));
    }

    function populateFilter() {
      const options = ["All airlines", ...getUniqueAirlines()];
      options.forEach(name => {
        const option = document.createElement("option");
        option.value = name;
        option.textContent = name;
        airlineFilter.appendChild(option);
      });
    }

    function filterCoreRows() {
      const selected = airlineFilter.value;
      if (selected === "All airlines") {
        return coreData;
      }
      return coreData.filter(row => row.airline_name === selected);
    }

    function filterReadableRows() {
      const selected = airlineFilter.value;
      const search = tableSearch.value.trim().toLowerCase();
      return readableData.filter(row => {
        const airlinePass = selected === "All airlines" || row.airline_name === selected;
        if (!airlinePass) {
          return false;
        }
        if (!search) {
          return true;
        }
        return tableColumns.some(column => String(row[column]).toLowerCase().includes(search));
      });
    }

    function buildKPIs(rows) {
      const flights = rows.reduce((sum, row) => sum + row.total_arrival_flights, 0);
      const delayed = rows.reduce((sum, row) => sum + row.delayed_arrivals_15_plus, 0);
      const cancelled = rows.reduce((sum, row) => sum + row.cancelled_arrivals, 0);
      const diverted = rows.reduce((sum, row) => sum + row.diverted_arrivals, 0);
      const totalDelayMinutes = rows.reduce((sum, row) => sum + row.total_arrival_delay_minutes, 0);
      const delayRate = flights ? delayed / flights : 0;
      const avgDelayMinutes = delayed ? totalDelayMinutes / delayed : 0;

      return [
        { label: "Total arrival flights", value: formatInteger(flights), sub: "Operational exposure" },
        { label: "Delayed arrivals", value: formatInteger(delayed), sub: `Delay rate ${formatPercent(delayRate)}` },
        { label: "Cancelled arrivals", value: formatInteger(cancelled), sub: `Cancellation rate ${formatPercent(flights ? cancelled / flights : 0)}` },
        { label: "Diverted arrivals", value: formatInteger(diverted), sub: "Diversions / reroutes" },
        { label: "Total delay minutes", value: formatMinutes(totalDelayMinutes), sub: `Average ${avgDelayMinutes.toFixed(1)} min per delayed flight` }
      ];
    }

    function renderKPIs(rows) {
      const kpiGrid = document.getElementById("kpiGrid");
      kpiGrid.innerHTML = "";
      buildKPIs(rows).forEach(card => {
        const element = document.createElement("div");
        element.className = "kpi-card";
        element.innerHTML = `
          <div class="kpi-label">${card.label}</div>
          <div class="kpi-value">${card.value}</div>
          <div class="kpi-sub">${card.sub}</div>
        `;
        kpiGrid.appendChild(element);
      });
    }

    function aggregateMonthly(rows) {
      const periodMap = new Map(allPeriods.map(period => [period, { period, delayed: 0, cancelled: 0 }]));
      rows.forEach(row => {
        const period = getPeriod(row);
        if (!periodMap.has(period)) {
          periodMap.set(period, { period, delayed: 0, cancelled: 0 });
        }
        const bucket = periodMap.get(period);
        bucket.delayed += row.delayed_arrivals_15_plus;
        bucket.cancelled += row.cancelled_arrivals;
      });
      return [...periodMap.values()].sort((a, b) => a.period.localeCompare(b.period));
    }

    function renderMonthlyTrend(rows) {
      const monthly = aggregateMonthly(rows);
      const layout = {
        margin: { l: 60, r: 20, t: 20, b: 50 },
        paper_bgcolor: "rgba(0,0,0,0)",
        plot_bgcolor: "rgba(0,0,0,0)",
        font: { family: chartFont, color: "#3E3A39" },
        legend: { orientation: "h", y: 1.12 },
        xaxis: { title: "Year-Month", tickangle: -45, nticks: 14 },
        yaxis: { title: "Flights", rangemode: "tozero", gridcolor: "#D1DFE6" }
      };
      const data = [
        {
          x: monthly.map(d => d.period),
          y: monthly.map(d => d.delayed),
          mode: "lines+markers",
          name: "Delayed arrivals (15+ min)",
          line: { color: "#3F74A3", width: 4 },
          marker: { size: 9 }
        },
        {
          x: monthly.map(d => d.period),
          y: monthly.map(d => d.cancelled),
          mode: "lines+markers",
          name: "Cancelled arrivals",
          line: { color: "#B54646", width: 4 },
          marker: { size: 9 }
        }
      ];
      Plotly.react("monthlyTrend", data, layout, { responsive: true, displaylogo: false });
    }

    function renderCauseBreakdown(rows) {
      const totals = causeColumns.map(cause => ({
        ...cause,
        value: rows.reduce((sum, row) => sum + row[cause.key], 0)
      }));
      const totalDelayMinutes = totals.reduce((sum, item) => sum + item.value, 0);
      const layout = {
        margin: { l: 20, r: 20, t: 20, b: 20 },
        paper_bgcolor: "rgba(0,0,0,0)",
        plot_bgcolor: "rgba(0,0,0,0)",
        font: { family: chartFont, color: "#3E3A39" },
        legend: { orientation: "h", y: -0.15 },
        annotations: [{
          x: 0.5,
          y: 0.5,
          xref: "paper",
          yref: "paper",
          showarrow: false,
          align: "center",
          text: `<span style="font-size:23px;font-weight:700;color:#3F74A3">${Math.round(totalDelayMinutes).toLocaleString("en-US")}</span><br><span style="font-size:12px;color:#794E47">Total delay minutes</span>`
        }]
      };
      const data = [{
        type: "pie",
        hole: 0.66,
        domain: { x: [0.08, 0.92], y: [0.08, 0.92] },
        values: totals.map(item => item.value),
        labels: totals.map(item => item.label),
        marker: { colors: totals.map(item => item.color) },
        textinfo: "label+percent",
        hovertemplate: "%{label}<br>%{value:,.0f} delay minutes<extra></extra>"
      }];
      Plotly.react("causeBreakdown", data, layout, { responsive: true, displaylogo: false });
    }

    function renderAirlineRisk() {
      const selected = airlineFilter.value;
      const maxFlights = Math.max(...airlineRiskData.map(row => row.total_arrival_flights));
      const layout = {
        margin: { l: 70, r: 20, t: 20, b: 60 },
        paper_bgcolor: "rgba(0,0,0,0)",
        plot_bgcolor: "rgba(0,0,0,0)",
        font: { family: chartFont, color: "#3E3A39" },
        xaxis: {
          title: "Delay rate",
          tickformat: ".0%",
          gridcolor: "#D1DFE6"
        },
        yaxis: {
          title: "Average delay minutes per delayed flight",
          rangemode: "tozero",
          gridcolor: "#D1DFE6"
        },
        showlegend: false
      };
      const data = [{
        type: "scatter",
        mode: "markers+text",
        x: airlineRiskData.map(row => row.delay_rate),
        y: airlineRiskData.map(row => row.average_delay_minutes_per_delayed_flight),
        text: airlineRiskData.map(row => row.airline_name),
        textposition: "top center",
        hovertemplate:
          "<b>%{text}</b><br>" +
          "Delay rate: %{x:.1%}<br>" +
          "Avg delay minutes: %{y:.1f}<br>" +
          "Flights: %{customdata[0]:,.0f}<br>" +
          "Cancelled: %{customdata[1]:,.0f}<extra></extra>",
        customdata: airlineRiskData.map(row => [row.total_arrival_flights, row.cancelled_arrivals]),
        marker: {
          size: airlineRiskData.map(row => 18 + (row.total_arrival_flights / maxFlights) * 32),
          color: airlineRiskData.map((row, index) => selected === "All airlines" ? airlinePalette[index % airlinePalette.length] : (row.airline_name === selected ? "#B54646" : "#A78F95")),
          line: { color: "#1F1F1F", width: 1.4 },
          opacity: airlineRiskData.map(row => selected === "All airlines" ? 0.94 : (row.airline_name === selected ? 0.98 : 0.42))
        },
        textfont: { family: chartFont, size: 9, color: "#3E3A39" }
      }];
      Plotly.react("airlineRisk", data, layout, { responsive: true, displaylogo: false });
    }

    function renderTable(rows) {
      const tableHead = document.getElementById("tableHead");
      const tableBody = document.getElementById("tableBody");
      const tableCount = document.getElementById("tableCount");

      tableHead.innerHTML = "";
      tableColumns.forEach(column => {
        const th = document.createElement("th");
        th.textContent = column;
        tableHead.appendChild(th);
      });

      tableBody.innerHTML = "";
      rows.forEach(row => {
        const tr = document.createElement("tr");
        tableColumns.forEach(column => {
          const td = document.createElement("td");
          const value = row[column];
          td.textContent = typeof value === "number" ? (Number.isInteger(value) ? formatInteger(value) : value.toFixed(2)) : value;
          tr.appendChild(td);
        });
        tableBody.appendChild(tr);
      });

      tableCount.textContent = `${rows.length.toLocaleString("en-US")} rows visible`;
    }

    function updateDashboard() {
      const filteredCoreRows = filterCoreRows();
      const filteredReadableRows = filterReadableRows();
      renderKPIs(filteredCoreRows);
      renderMonthlyTrend(filteredCoreRows);
      renderCauseBreakdown(filteredCoreRows);
      renderAirlineRisk();
      renderTable(filteredReadableRows);
    }

    populateFilter();
    airlineFilter.addEventListener("change", updateDashboard);
    tableSearch.addEventListener("input", updateDashboard);
    updateDashboard();
  </script>
</body>
</html>
"""

    html = (
        html_template.replace("__PLOTLY_JS__", plotly_js)
        .replace("__TABLE_DATA__", json.dumps(table_records, ensure_ascii=False))
        .replace("__CORE_DATA__", json.dumps(core_records, ensure_ascii=False))
        .replace("__AIRLINE_RISK_DATA__", json.dumps(airline_records, ensure_ascii=False))
        .replace("__TABLE_COLUMNS__", json.dumps(table_columns, ensure_ascii=False))
        .replace("__DATA_SCOPE__", data_scope)
        .replace("__FINAL_ROWS__", str(cleaning_summary["final_rows"]))
        .replace("__REMOVED_NO_OPS__", str(cleaning_summary["removed_for_no_operations"]))
        .replace("__REMOVED_LOGIC__", str(cleaning_summary["removed_for_logic_issue"]))
    )

    (DASHBOARD_DIR / "jfk_operational_risk_dashboard.html").write_text(html, encoding="utf-8")


def build_summary_markdown(
    cleaned_df: pd.DataFrame,
    monthly_summary: pd.DataFrame,
    cause_summary: pd.DataFrame,
    airline_profile: pd.DataFrame,
    cleaning_summary: dict[str, int],
) -> None:
    peak_delay_month = monthly_summary.loc[monthly_summary["delayed_arrivals_15_plus"].idxmax()]
    peak_cancel_month = monthly_summary.loc[monthly_summary["cancelled_arrivals"].idxmax()]
    top_cause = cause_summary.iloc[0]
    highest_delay_rate = airline_profile.loc[airline_profile["delay_rate"].idxmax()]
    highest_severity = airline_profile.loc[airline_profile["average_delay_minutes_per_delayed_flight"].idxmax()]
    cleaned_periods = cleaned_df.assign(
        year_month=cleaned_df["year"].astype(str) + "-" + cleaned_df["month"].astype(str).str.zfill(2)
    )["year_month"]
    coverage_start = cleaned_periods.min()
    coverage_end = cleaned_periods.max()

    summary = f"""# JFK Operational Risk Descriptive Summary

## Data cleaning

- Data coverage after cleaning: {coverage_start} to {coverage_end}
- Raw rows: {cleaning_summary["initial_rows"]}
- Removed because total arrival flights were missing or zero: {cleaning_summary["removed_for_no_operations"]}
- Removed because delayed arrivals exceeded total arrivals: {cleaning_summary["removed_for_logic_issue"]}
- Final cleaned rows used for analysis: {cleaning_summary["final_rows"]}

## Descriptive insights

- Peak monthly delay volume occurred in {peak_delay_month["year_month"]} with {int(round(peak_delay_month["delayed_arrivals_15_plus"])):,} delayed arrivals.
- Peak monthly cancellation volume occurred in {peak_cancel_month["year_month"]} with {int(round(peak_cancel_month["cancelled_arrivals"])):,} cancelled arrivals.
- The largest delay-severity driver was {top_cause["cause"]}, contributing {top_cause["share_of_total_delay_minutes"]:.1%} of total delay minutes.
- The highest delay-rate airline was {highest_delay_rate["airline_name"]} at {highest_delay_rate["delay_rate"]:.1%}.
- The highest average delay severity was {highest_severity["airline_name"]} at {highest_severity["average_delay_minutes_per_delayed_flight"]:.1f} minutes per delayed flight.

## Output update note

- The core cleaned dataset keeps the same field names as the earlier single-year workflow.
- The monthly summary includes `year`, `year_month`, and `period_start` to support the current multi-year timeline.
- The static charts and offline dashboard use a softer presentation palette and system-safe fonts for consistent PNG and SVG rendering.
- Chart 2 is now exported as a compact horizontal layout with transparent PNG and SVG backgrounds for cleaner report and slide placement.

## Modeling handoff note

- The cleaned core dataset preserves frequency variables such as delayed arrivals and cancellations.
- It also preserves severity variables through total delay minutes and delay-cause minutes.
- These outputs are ready to support later work on frequency models, severity models, and aggregate loss modeling.
"""

    (SUMMARY_DIR / SUMMARY_NOTE_NAME).write_text(summary, encoding="utf-8")


def main() -> None:
    ensure_output_directories()
    apply_chart_style()

    raw_df = load_raw_data()
    column_dictionary = build_column_dictionary()
    readable_full_df = build_readable_full_dataset(raw_df)
    cleaned_df, cleaning_summary = clean_core_dataset(readable_full_df)
    monthly_summary, cause_summary, airline_profile = build_summaries(cleaned_df)

    save_dataframe(column_dictionary, COLUMN_DICTIONARY_STEM)
    save_dataframe(readable_full_df, READABLE_FULL_STEM)
    save_dataframe(cleaned_df, CLEANED_CORE_STEM)
    save_dataframe(monthly_summary, MONTHLY_SUMMARY_STEM)
    save_dataframe(cause_summary, CAUSE_SUMMARY_STEM)
    save_dataframe(airline_profile, AIRLINE_PROFILE_STEM)

    create_monthly_trend_chart(monthly_summary)
    create_delay_cause_chart(cause_summary)
    create_airline_risk_chart(airline_profile)
    build_dashboard(readable_full_df, cleaned_df, airline_profile, cleaning_summary)
    build_summary_markdown(cleaned_df, monthly_summary, cause_summary, airline_profile, cleaning_summary)

    print("Outputs written to:")
    print(f"  Processed data: {PROCESSED_DIR}")
    print(f"  Charts: {CHART_DIR}")
    print(f"  Dashboard: {DASHBOARD_DIR}")


if __name__ == "__main__":
    main()
