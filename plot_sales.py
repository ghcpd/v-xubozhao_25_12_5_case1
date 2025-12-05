import json
from pathlib import Path
import matplotlib.pyplot as plt


def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    months = [item['Month'] for item in data]
    sales = [item['Sales'] for item in data]
    return months, sales


def plot_line(months, sales, out_path):
    plt.figure(figsize=(10, 5))
    plt.plot(months, sales, marker='o', linestyle='-', color='#1f77b4')
    plt.title('Monthly Sales - Line Chart')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def plot_bar(months, sales, out_path):
    plt.figure(figsize=(10, 5))
    bars = plt.bar(months, sales, color='#ff7f0e')
    plt.title('Monthly Sales - Bar Chart')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(axis='y', alpha=0.25)
    # Add value labels
    for bar in bars:
        h = bar.get_height()
        plt.annotate(f'{h}', xy=(bar.get_x() + bar.get_width() / 2, h),
                     xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=8)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def main():
    base = Path(__file__).parent
    data_file = base / 'monthl_sales.json'
    line_out = base / 'sales_line.png'
    bar_out = base / 'sales_bar.png'

    months, sales = load_data(data_file)
    plot_line(months, sales, line_out)
    plot_bar(months, sales, bar_out)
    print(f'Wrote {line_out}\nWrote {bar_out}')


if __name__ == '__main__':
    main()
