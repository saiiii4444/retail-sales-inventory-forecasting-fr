# Retail Sales & Inventory Forecasting — France

I built this project as a hands‑on exercise in turning raw data into insights
for a fictional French retail chain. It’s meant to show a simple end‑to‑end
workflow: starting from daily sales and inventory files, cleaning and
aggregating them, and finally preparing them for interactive visuals in
Power BI. The data and code are here for learning and can be adapted to
real‑world scenarios.

## Project overview

Retailers operate in a dynamic environment where demand can fluctuate
significantly across stores and products. Having a clear view of sales trends
and inventory levels allows managers to identify best‑selling items, plan
replenishments, and avoid stockouts or overstock situations. In this project
I generated two years of daily transactions across ten stores and fifty
products. My focus was on straightforward analytics: cleaning the data,
aggregating it at weekly and monthly frequencies, and preparing it for
interactive dashboards.

### Key features

- **Realistic‑scale data:** The dataset spans 1 January 2023 to
  31 December 2024, capturing hundreds of thousands of daily transactions.
  Each row records `units_sold`, `unit_price`, `revenue` and
  `inventory_level` for a store‑product combination.
- **Straightforward ETL script:** A single script (`src/etl.py`) reads the
  raw CSV, converts dates, and produces weekly and monthly aggregates ready
  for analysis.
- **Dashboard guidance:** Notes on how to assemble Power BI visuals are
  provided to help you build a compelling report with slicers, time series
  charts, and heatmaps.
- **Plain documentation:** All code and explanations are written in
  everyday language. There are no references to AI or automation.

## Folder structure

```
.
├── data
│   ├── raw
│   │   └── sales_data.csv        # Daily sales and inventory data
│   └── processed
│       ├── weekly_sales.csv      # Weekly aggregated metrics
│       └── monthly_sales.csv     # Monthly aggregated metrics
├── src
│   └── etl.py                    # ETL script for processing raw data
├── dashboards
│   └── POWER_BI_NOTES.md         # Suggested visuals for reporting
├── reports
│   └── findings.md               # High‑level observations from the data
├── notebooks
│   └── (placeholder for your own analysis notebooks)
├── requirements.txt
└── .gitignore
```

## Getting started

### 1. Install dependencies

Install the required Python packages (pandas is all you need):

```bash
pip install -r requirements.txt
```

### 2. Run the ETL pipeline

From the project root:

```bash
python src/etl.py
```

This will read `data/raw/sales_data.csv`, compute weekly and monthly
aggregates, and save them in `data/processed/`.

### 3. Build your dashboard

Refer to `dashboards/POWER_BI_NOTES.md` for ideas on how to visualise the
aggregated data in Power BI. At a minimum, consider displaying total revenue
and units sold over time, a heatmap of stores vs. products, and a stock risk
analysis highlighting low inventory levels.

## About the data

The dataset provided here is synthetically generated to resemble the
behaviour of a mid‑sized retailer. While the figures are not tied to any
real company, the scale and structure are representative of real
operational data. In my own exploratory analyses, stores like
**Store 09** and **Store 01** and products such as **Product 040** and
**Product 035** emerged as top performers. Your findings may vary as you
dive deeper into the numbers.

## Contributions

This project is intended as a learning resource. Feel free to explore,
modify, or extend the analysis to suit your needs. PRs, issues, and
suggestions are welcome.