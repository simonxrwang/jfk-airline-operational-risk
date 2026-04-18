# JFK Airline Delay Operational Risk Project

## Overview | 项目概述

This repository contains a reproducible data-preparation and descriptive-analysis workflow for an operational risk management project on airline delays, cancellations, and diversions at John F. Kennedy International Airport (JFK).

本仓库用于支持一个关于纽约肯尼迪国际机场（JFK）航班延误、取消与改降风险的运营风险管理项目，包含可复现的数据整理、描述性分析、图表输出与交互式看板。

## Research focus | 研究主题

- Frequency risk: how often delay and cancellation events occur.
- Severity risk: how many delay minutes are generated when disruption happens.
- Aggregate operational risk: how frequency and severity can later be combined for modeling.

- 频率风险：延误和取消事件发生得有多频繁。
- 严重程度风险：一旦发生扰动，会带来多少延误分钟。
- 聚合运营风险：后续如何将频率和严重程度结合起来做建模。

## Data source | 数据来源

- BTS On-Time Performance dataset
- Scope used in this project: one year of JFK arrival data covering all airlines in the selected sample

- 数据集来源：BTS On-Time Performance
- 本项目使用范围：JFK 机场一年期到达航班数据，覆盖样本中的全部航司

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

## Collaboration workflow | 协作开发流程

If someone wants to continue building on this repository with write access, the recommended workflow is:

如果其他人获得了这个仓库的写权限，推荐按下面的流程继续开发：

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

If someone does not have write access, they should fork the repository first, then work from their own fork and submit a Pull Request back to this repository.

如果对方没有写权限，应该先 fork 本仓库，再在自己的 fork 上开发，最后向本仓库发起 Pull Request。

## Access management | 权限管理

### How to know who can edit this repository | 如何查看谁有编辑权限

For a personal repository on GitHub, people with collaborator access can edit and push to the repository.

对于个人账户下的 GitHub 仓库，拥有 collaborator 权限的人可以直接编辑并推送代码。

To check who currently has access:

你可以通过下面方式查看当前谁有权限：

1. Open the repository on GitHub.
2. Click `Settings`.
3. In the left sidebar, open `Collaborators`.
4. Review the people listed there and any pending invitations.

1. 打开仓库主页。
2. 点击 `Settings`。
3. 在左侧边栏进入 `Collaborators`。
4. 查看已添加人员和待接受邀请。

### How to let someone edit the repository | 如何让别人获得编辑权限

1. Open the repository on GitHub.
2. Click `Settings`.
3. In the left sidebar, click `Collaborators`.
4. Click `Add people`.
5. Enter the person's GitHub username or email.
6. Send the invitation.
7. Once they accept, they will be able to push changes directly if you invited them to your personal repository as a collaborator.

1. 打开仓库主页。
2. 点击 `Settings`。
3. 在左侧边栏点击 `Collaborators`。
4. 点击 `Add people`。
5. 输入对方的 GitHub 用户名或邮箱。
6. 发送邀请。
7. 对方接受后，就可以作为协作者直接向仓库推送修改。

### Recommended collaboration model | 推荐协作方式

- Give direct collaborator access only to people you trust to push code responsibly.
- Ask collaborators to work on feature branches instead of pushing directly to `main`.
- Use Pull Requests to review changes before merging.

- 只给你信任的人直接协作者权限。
- 让协作者在功能分支上开发，不要直接推送到 `main`。
- 用 Pull Request 审查修改后再合并。

## Main outputs | 主要输出文件

- `jfk_airline_delay_readable_full`
  Full readable dataset with airline abbreviations replaced by full airline names and clearer field names.
- `jfk_airline_delay_core_cleaned`
  Core cleaned dataset for later frequency and severity modeling.
- `jfk_column_dictionary`
  Data dictionary linking original BTS fields to readable names and plain-language definitions.
- `jfk_monthly_risk_summary`
  Monthly totals for delays, cancellations, flights, and delay minutes.
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
  各月份的延误、取消、航班量与总延误分钟汇总。
- `jfk_delay_cause_summary`
  各类延误原因对应的总延误分钟与占比。
- `jfk_airline_risk_profile`
  各航司层面的风险指标，如延误率、取消率和平均延误严重程度。

## Data-cleaning logic | 数据清洗逻辑

- Drop rows where total arrival flights are missing or equal to zero.
- Fill missing delay-minute fields with `0` when the airline operated flights in that month.
- Drop rows where delayed arrivals exceed total arrival flights.

- 删除 `total_arrival_flights` 缺失或等于 0 的记录。
- 当航司在该月存在运营时，将缺失的延误分钟字段填充为 `0`。
- 删除“延误航班数大于总到达航班数”的逻辑异常记录。

For this JFK sample, no rows were removed by these rules, but the checks are retained for reproducibility and future modeling work.

在这份 JFK 样本中，以上规则最终没有删除任何记录，但这些规则会保留下来，以保证流程可复现，并服务于后续建模。

## Visual outputs | 可视化输出

- Chart 1: Monthly delayed arrivals vs cancelled arrivals
- Chart 2: Delay-cause donut chart with total delay minutes at the center
- Chart 3: Airline risk profiling scatter plot
- Offline dashboard with filtering, interactive charts, and a readable data table

- 图 1：月度延误航班与取消航班趋势图
- 图 2：带中心总延误分钟的延误原因环形图
- 图 3：航司风险画像散点图
- 离线交互式看板，支持筛选、交互图表与数据表浏览

## Next step | 下一步

This repository currently focuses on data cleaning and descriptive analysis. It prepares the dataset for later work on loss frequency, loss severity, and aggregate risk modeling, but it does not yet build the statistical models themselves.

当前仓库主要聚焦于数据清洗与描述性分析，为后续的损失频率、损失严重程度和聚合风险建模打基础，但暂未包含统计模型本身。
