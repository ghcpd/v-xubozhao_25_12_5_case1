import os
import sys
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = os.path.dirname(__file__)
json_path = os.path.join(ROOT, 'monthl_sales.json')

try:
    df = pd.read_json(json_path)
except Exception as e:
    print(f'ERROR: Could not read JSON file: {e}')
    sys.exit(2)

# Ensure data columns exist
if 'Month' not in df.columns or 'Sales' not in df.columns:
    print('ERROR: Expected columns "Month" and "Sales" not found')
    sys.exit(3)

# Plot: Line chart
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', linewidth=2)
plt.title('Monthly Sales - Line Chart')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True, linestyle='--', alpha=0.6)
line_out = os.path.join(ROOT, 'line_chart.png')
plt.savefig(line_out, bbox_inches='tight')
plt.close()

# Plot: Bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(df['Month'], df['Sales'], color='C1')
plt.title('Monthly Sales - Bar Chart')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(axis='y', linestyle='--', alpha=0.6)
# Annotate bars
for bar in bars:
    h = bar.get_height()
    plt.annotate(f'{int(h)}', xy=(bar.get_x() + bar.get_width() / 2, h),
                 xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=9)
bar_out = os.path.join(ROOT, 'bar_chart.png')
plt.savefig(bar_out, bbox_inches='tight')
plt.close()

print('SUCCESS: Charts saved as line_chart.png and bar_chart.png')
