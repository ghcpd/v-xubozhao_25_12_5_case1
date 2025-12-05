import json
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for file output
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = Path(__file__).parent / 'monthl_sales.json'


def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def make_line_chart(months, sales, out_path):
    plt.figure(figsize=(10, 5))
    plt.plot(months, sales, marker='o', linestyle='-', color='tab:blue')
    plt.title('Monthly Sales (Line)')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def make_bar_chart(months, sales, out_path):
    plt.figure(figsize=(10, 5))
    plt.bar(months, sales, color='tab:orange')
    plt.title('Monthly Sales (Bar)')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


if __name__ == '__main__':
    data = load_data(DATA_FILE)
    months = [row['Month'] for row in data]
    sales = [row['Sales'] for row in data]

    out_line = Path(__file__).parent / 'monthly_sales_line.png'
    out_bar = Path(__file__).parent / 'monthly_sales_bar.png'

    make_line_chart(months, sales, out_line)
    make_bar_chart(months, sales, out_bar)

    print(f"Saved line chart to: {out_line}")
    print(f"Saved bar chart to: {out_bar}")
