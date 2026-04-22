# JFK Airline Delay Operational Risk Project

## Overview | 项目概述

This repository contains a reproducible data-preparation and descriptive-analysis workflow for an operational risk management project on airline delays, cancellations, and diversions at John F. Kennedy International Airport (JFK). The current dataset covers monthly JFK airline operations from 2020 to 2025.

本仓库用于支持一个关于纽约肯尼迪国际机场（JFK）航班延误、取消与改降风险的运营风险管理项目，包含可复现的数据整理、描述性分析、图表输出与交互式看板。当前数据集覆盖 2020 年至 2025 年的 JFK 航司月度运营数据。

## Research focus | 研究主题

- Frequency risk: how often delay and cancellation events occur.
- Severity risk: how many delay minutes are generated when disruption happens.
- Aggregate operational risk: how frequency and severity can later be combined for modeling.

- 频率风险：延误和取消事件发生得有多频繁。
- 严重程度风险：一旦发生扰动，会带来多少延误分钟。
- 聚合运营风险：后续如何将频率和严重程度结合起来做建模。

## Data source | 数据来源

- BTS On-Time Performance dataset
- Scope used in this project: multi-year JFK arrival data from 2020 to 2025 covering all airlines in the selected sample

- 数据集来源：BTS On-Time Performance
- 本项目使用范围：2020 年至 2025 年 JFK 机场多年份到达航班数据，覆盖样本中的全部航司

## Repository structure | 仓库结构

```text
.
├── data
│   ├── raw
│   │   ├── Airline_Delay_Cause.csv
│   │   └── Download_Column_Definitions.xlsx
│   └── processed
│       ├── jfk_airline_delay_readable_full.csv
│       ├── jfk_airline_delay_core_cleaned.csv
│       ├── jfk_column_dictionary.csv
│       ├── jfk_monthly_risk_summary.csv
│       ├── jfk_delay_cause_summary.csv
│       └── jfk_airline_risk_profile.csv
├── reports
│   ├── charts
│   ├── dashboard
│   ├── data_preparation_chapter
│   │   ├── zh
│   │   └── en
│   ├── presentation_chapter
│   │   ├── zh
│   │   ├── en
│   │   └── shared
│   └── summary
├── scripts
│   └── build_operational_risk_assets.py
├── environment.yml
└── README.md
```

## What is included | 仓库内容

- `data/raw/`
  Original BTS source data and the official column-definition file.
- `data/processed/`
  Cleaned and analysis-ready datasets.
- `reports/charts/`
  High-resolution PNG charts and SVG vector charts for reports or slides.
- `reports/dashboard/jfk_operational_risk_dashboard.html`
  A standalone offline interactive dashboard that can be opened directly in a browser.
- `reports/data_preparation_chapter/`
  Bilingual LaTeX source files and compiled PDFs for the data-preparation report chapter, separated into `zh/` and `en/`.
- `reports/presentation_chapter/`
  Bilingual LaTeX Beamer source files and compiled PDFs for the 4-minute presentation segment, separated into `zh/` and `en/` and using the HKU Beamer template style.
- `reports/summary/jfk_descriptive_analysis_summary.md`
  A short written summary of cleaning results and key descriptive findings.

- `data/raw/`
  原始 BTS 数据与官方字段说明文件。
- `data/processed/`
  清洗后、可直接用于分析的数据。
- `reports/charts/`
  可用于报告或 PPT 的高清 PNG 图和 SVG 矢量图。
- `reports/dashboard/jfk_operational_risk_dashboard.html`
  可直接在浏览器中打开的离线交互式看板。
- `reports/data_preparation_chapter/`
  数据准备章节报告的中英文 LaTeX 源文件与已编译 PDF，已按 `zh/` 与 `en/` 分开存放。
- `reports/presentation_chapter/`
  约 4 分钟汇报内容的中英文 LaTeX Beamer 源文件与已编译 PDF，已按 `zh/` 与 `en/` 分开存放，当前使用 HKU Beamer 模板风格。
- `reports/summary/jfk_descriptive_analysis_summary.md`
  数据清洗结果与关键发现的简要文字总结。

## Quick start | 快速开始

### 1. Create the environment | 创建环境

```bash
conda env create -f environment.yml
conda activate operational_risk
```

### 2. Rebuild all outputs | 重新生成全部结果

```bash
python scripts/build_operational_risk_assets.py
```

### 3. Open the dashboard | 打开交互看板

Open `reports/dashboard/jfk_operational_risk_dashboard.html` in any modern browser.

使用任意现代浏览器打开 `reports/dashboard/jfk_operational_risk_dashboard.html` 即可。

### 4. Rebuild the chapter PDFs | 重新编译章节 PDF

The chapter report and slides are written in LaTeX. Compile them with XeLaTeX:

章节报告与汇报 slides 使用 LaTeX 编写。可用 XeLaTeX 重新编译：

```bash
cd reports/data_preparation_chapter/zh
latexmk -xelatex data_preparation_report_zh.tex
latexmk -c

cd ../en
latexmk -xelatex data_preparation_report_en.tex
latexmk -c

cd ../../presentation_chapter/zh
latexmk -xelatex data_preparation_slides_zh.tex
latexmk -c
rm -f *.nav *.snm

cd ../en
latexmk -xelatex data_preparation_slides_en.tex
latexmk -c
rm -f *.nav *.snm
```

## Collaboration workflow | 协作开发流程

To continue building on this repository, use a feature branch and keep changes reproducible:

如需在本仓库基础上继续开发，建议使用功能分支，并保持结果可复现：

```bash
git clone https://github.com/simonxrwang/jfk-airline-operational-risk.git
cd jfk-airline-operational-risk
conda env create -f environment.yml
conda activate operational_risk
git checkout -b feat/your-change
```

After making changes:

完成修改后可以使用：

```bash
git add .
git commit -m "Describe your change"
git push -u origin feat/your-change
```

Then open a Pull Request on GitHub to merge the branch back into `main`.

之后在 GitHub 上发起 Pull Request，再把该分支合并回 `main`。

## Main outputs | 主要输出文件

- `jfk_airline_delay_readable_full`
  Full readable dataset with airline abbreviations replaced by full airline names and clearer field names.
- `jfk_airline_delay_core_cleaned`
  Core cleaned dataset for later frequency and severity modeling.
- `jfk_column_dictionary`
  Data dictionary linking original BTS fields to readable names and plain-language definitions.
- `jfk_monthly_risk_summary`
  Year-month totals for delays, cancellations, flights, and delay minutes.
- `jfk_delay_cause_summary`
  Delay-minute totals and shares by cause.
- `jfk_airline_risk_profile`
  Airline-level risk metrics such as delay rate, cancellation rate, and average delay severity.

- `jfk_airline_delay_readable_full`
  可读版完整数据表，已将航司缩写替换为全称，并改为更直观的字段名。
- `jfk_airline_delay_core_cleaned`
  后续频率与严重程度建模可直接使用的核心清洗数据。
- `jfk_column_dictionary`
  原始 BTS 字段、可读字段名与通俗解释之间的对应表。
- `jfk_monthly_risk_summary`
  各年月的延误、取消、航班量与总延误分钟汇总。
- `jfk_delay_cause_summary`
  各类延误原因对应的总延误分钟与占比。
- `jfk_airline_risk_profile`
  各航司层面的风险指标，如延误率、取消率和平均延误严重程度。

## Schema note | 字段说明

The core cleaned dataset keeps the same analysis-ready field names used in the earlier single-year workflow. Because the project now covers multiple years, `jfk_monthly_risk_summary` includes `year`, `year_month`, and `period_start` so monthly trends are not incorrectly merged across different years.

核心清洗数据表保留了此前单一年份流程中使用的分析字段名。由于当前项目已经扩展为多年份数据，`jfk_monthly_risk_summary` 额外保留 `year`、`year_month` 与 `period_start`，避免不同年份的同一月份在趋势分析中被错误合并。

## Data-cleaning logic | 数据清洗逻辑

- Drop rows where total arrival flights are missing or equal to zero.
- Fill missing delay-minute fields with `0` when the airline operated flights in that month.
- Drop rows where delayed arrivals exceed total arrival flights.

- 删除 `total_arrival_flights` 缺失或等于 0 的记录。
- 当航司在该月存在运营时，将缺失的延误分钟字段填充为 `0`。
- 删除“延误航班数大于总到达航班数”的逻辑异常记录。

For the current 2020-2025 JFK sample, one row was removed because total arrival flights were missing or zero. The checks are retained for reproducibility and future modeling work.

在当前 2020-2025 JFK 样本中，有 1 条记录因总到达航班数缺失或为 0 被删除。这些规则会保留下来，以保证流程可复现，并服务于后续建模。

## Visual outputs | 可视化输出

- Chart 1: Multi-year monthly delayed arrivals vs cancelled arrivals
- Chart 2: Compact horizontal delay-cause breakdown with a donut summary and share bars
- Chart 3: Airline risk profiling scatter plot
- Offline dashboard with filtering, interactive charts, and a readable data table
- Data-preparation chapter report in Chinese and English
- Data-preparation presentation segment in Chinese and English
- Static charts are exported as both PNG and SVG with transparent backgrounds. The current chart style uses a muted presentation-friendly palette and system-safe fonts so PNG and SVG stay visually consistent across environments and can be placed cleanly into reports or slides.

- 图 1：多年份月度延误航班与取消航班趋势图
- 图 2：紧凑横向延误原因结构图，包含环形总览与占比条形图
- 图 3：航司风险画像散点图
- 离线交互式看板，支持筛选、交互图表与数据表浏览
- 中英文数据准备章节报告
- 中英文数据准备汇报 slides
- 静态图表同时导出透明背景的 PNG 与 SVG。当前图表使用更适合展示的柔和配色，并采用系统安全字体，以保证 PNG 与 SVG 在不同环境中尽量保持一致，也方便嵌入报告或 slides。

## Next step | 下一步

This repository currently focuses on data cleaning and descriptive analysis. It prepares the dataset for later work on loss frequency, loss severity, and aggregate risk modeling, but it does not yet build the statistical models themselves.

当前仓库主要聚焦于数据清洗与描述性分析，为后续的损失频率、损失严重程度和聚合风险建模打基础，但暂未包含统计模型本身。
