## Power\u00a0BI Dashboard Outline

This document provides guidance on building a comprehensive Power\u00a0BI report
using the processed data from this project. The goal is to present
business\u2011relevant insights clearly and effectively, with interactive
slicers and drill\u2011down capabilities.

### 1. Overview page

Create a high\u2011level summary page that answers the question: *How are we
performing overall?*

- **KPIs:** Display cards for total revenue, total units sold, average unit
  price, and average inventory level for the selected period. Allow users to
  filter by date range, store, and product.
- **Trend chart:** Use a line chart to show revenue over time (weekly or
  monthly). Add a secondary axis for units sold if needed.
- **Top performers:** Include a bar or column chart showing the top
  five stores or products by revenue.

### 2. Store and product analysis

Use a matrix or heatmap visual to compare stores and products.

- **Sales heatmap:** Build a matrix with stores on the rows and
  products on the columns, showing total units sold or revenue. Apply a
  colour scale to highlight strong and weak performers.
- **Detailed table:** Add a table that lists store–product combinations
  with aggregated metrics (total revenue, units sold, average price,
  average inventory), sortable by any column.

### 3. Inventory health

Help decision makers spot potential stock issues before they occur.

- **Inventory vs. sales:** Create a bar chart or scatter plot comparing
  total units sold against average inventory level for each product.
  Products with low inventory but high sales should stand out; these are
  candidates for replenishment.
- **Stock‑out indicator:** Calculate a metric such as `(units_sold / inventory_level)`
  to estimate how quickly stock is being depleted. Visualise this metric
  across products or stores to prioritise restocking.

### 4. Slicers and filters

Add slicers for date ranges, store IDs, and product IDs to allow users to
focus on specific segments. Use sync options so slicers apply across all
pages where appropriate.

### General tips

- Keep the layout clean and uncluttered. Use grids to align visuals and
  leave white space between sections.
- Use consistent number formatting (e.g. thousand separators, currency
  symbols) and descriptive axis titles.
- Test your report with different date ranges and filters to ensure that
  visuals update correctly.
- Incorporate tooltips with concise explanations of each visual or metric.
