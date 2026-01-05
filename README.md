# Monthly Sales Charts

This small script reads `monthl_sales.json` (12 months of sales) and produces two charts:

- `line_chart.png` — line chart of sales across months
- `bar_chart.png` — bar chart of sales across months

Quick run (Windows PowerShell):

```powershell
# install dependencies in your Python environment
pip install -r requirements.txt

# run the script
python generate_charts.py
```

Outputs will be saved in the workspace root.
