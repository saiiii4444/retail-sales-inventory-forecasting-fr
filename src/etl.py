"""
Simple ETL for the retail forecasting project.

This script reads the raw daily sales file, resamples it to weekly and
monthly periods, and writes the summaries to the `data/processed`
directory. It’s intentionally straightforward so that it’s easy to follow
along and extend if needed.
"""

import pandas as pd
from pathlib import Path


def aggregate_sales(data: pd.DataFrame, freq: str) -> pd.DataFrame:
    """
    Resample and summarise units sold, revenue and inventory.

    Parameters
    ----------
    data : pandas.DataFrame
        Daily sales data with a `date` column and fields such as
        `store_id`, `product_id`, `units_sold`, `unit_price`, `revenue`
        and `inventory_level`.
    freq : str
        Resampling frequency like `'W-MON'` for weekly (week starting
        Monday) or `'M'` for monthly.

    Returns
    -------
    pandas.DataFrame
        Aggregated metrics including total units sold, total revenue,
        average unit price and average inventory level, grouped by period,
        store and product.
    """
    # Make sure the date column is parsed
    data['date'] = pd.to_datetime(data['date'])
    # Set date as index for resampling
    data = data.set_index('date')
    # Group by resampled date, store and product and compute metrics
    grouped = (
        data.groupby([pd.Grouper(freq=freq), 'store_id', 'product_id'])
        .agg(
            total_units_sold=('units_sold', 'sum'),
            total_revenue=('revenue', 'sum'),
            avg_unit_price=('unit_price', 'mean'),
            avg_inventory_level=('inventory_level', 'mean'),
        )
        .reset_index()
    )
    # Rename the resampled date column to period_start for clarity
    grouped = grouped.rename(columns={'date': 'period_start'})
    return grouped


def main():
    # Define where the files live
    root = Path(__file__).resolve().parents[1]
    raw_file = root / 'data' / 'raw' / 'sales_data.csv'
    out_dir = root / 'data' / 'processed'
    out_dir.mkdir(parents=True, exist_ok=True)

    # Load the raw data
    print(f"Reading data from {raw_file}")
    raw_df = pd.read_csv(raw_file, parse_dates=['date'])

    # Build weekly summary (week starts on Monday)
    print("Creating weekly summary...")
    weekly = aggregate_sales(raw_df.copy(), 'W-MON')
    weekly.to_csv(out_dir / 'weekly_sales.csv', index=False)

    # Build monthly summary
    print("Creating monthly summary...")
    monthly = aggregate_sales(raw_df.copy(), 'M')
    monthly.to_csv(out_dir / 'monthly_sales.csv', index=False)

    print("Done.")


if __name__ == '__main__':
    main()