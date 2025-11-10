"""
ETL script for the Retail Sales & Inventory Forecasting project.

This script reads raw daily sales and inventory data, performs simple
transformations, and writes aggregated outputs to the ``data/processed``
directory. The goal is to prepare data for downstream analytics and
dashboarding, using only open‑source libraries and straightforward
transformations.

Usage::

    python etl.py

Outputs:
    - weekly_sales.csv: aggregated weekly metrics by store and product
    - monthly_sales.csv: aggregated monthly metrics by store and product

The raw data is expected to be located at
``data/raw/sales_data.csv`` relative to the project root.

"""

import pandas as pd
from pathlib import Path


def aggregate_sales(df: pd.DataFrame, freq: str) -> pd.DataFrame:
    """Aggregate sales and inventory data at a given frequency.

    Parameters
    ----------
    df : pandas.DataFrame
        Raw daily sales data with columns
        ``date``, ``store_id``, ``product_id``, ``units_sold``,
        ``unit_price``, ``revenue``, and ``inventory_level``.
    freq : str
        Resampling frequency (e.g. 'W-MON' for weekly, 'M' for monthly).

    Returns
    -------
    pandas.DataFrame
        Aggregated metrics with grouped columns and summary statistics.
    """
    # Ensure ``date`` column is datetime
    df['date'] = pd.to_datetime(df['date'])

    # Set multi‑index for resampling
    df = df.set_index('date')

    # Resample by frequency and group by store and product
    grouped = (
        df.groupby([pd.Grouper(freq=freq), 'store_id', 'product_id'])
        .agg(
            total_units_sold=('units_sold', 'sum'),
            total_revenue=('revenue', 'sum'),
            avg_unit_price=('unit_price', 'mean'),
            avg_inventory_level=('inventory_level', 'mean'),
        )
        .reset_index()
    )

    # Rename ``date`` to ``period_start`` for clarity
    grouped = grouped.rename(columns={'date': 'period_start'})
    return grouped


def main():
    # Define paths
    project_root = Path(__file__).resolve().parents[1]
    raw_path = project_root / 'data' / 'raw' / 'sales_data.csv'
    processed_dir = project_root / 'data' / 'processed'
    processed_dir.mkdir(parents=True, exist_ok=True)

    # Load raw data
    print(f'Loading raw data from {raw_path}')
    sales_df = pd.read_csv(raw_path, parse_dates=['date'])

    # Aggregate weekly (week starts on Monday)
    print('Aggregating weekly data...')
    weekly = aggregate_sales(sales_df.copy(), freq='W-MON')
    weekly_path = processed_dir / 'weekly_sales.csv'
    weekly.to_csv(weekly_path, index=False)
    print(f'Saved weekly data to {weekly_path}')

    # Aggregate monthly
    print('Aggregating monthly data...')
    monthly = aggregate_sales(sales_df.copy(), freq='M')
    monthly_path = processed_dir / 'monthly_sales.csv'
    monthly.to_csv(monthly_path, index=False)
    print(f'Saved monthly data to {monthly_path}')

    # Additional transformations could be added here as needed


if __name__ == '__main__':
    main()
