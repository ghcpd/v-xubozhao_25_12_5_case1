import json
from pathlib import Path
import matplotlib.pyplot as plt


def load_data(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def make_line_chart(months, values, out_path: Path):
    plt.figure(figsize=(10, 5))
    plt.plot(months, values, marker='o', linestyle='-', color='#1f77b4')
    plt.title('Monthly Sales (Line)')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def make_bar_chart(months, values, out_path: Path):
    plt.figure(figsize=(10, 5))
    bars = plt.bar(months, values, color='#ff7f0e')
    plt.title('Monthly Sales (Bar)')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.xticks(rotation=0)

    # label bars with values
    for bar in bars:
        h = bar.get_height()
        plt.annotate(f"{int(h)}",
                     xy=(bar.get_x() + bar.get_width() / 2, h),
                     xytext=(0, 4),
                     textcoords='offset points',
                     ha='center', va='bottom', fontsize=8)

    plt.grid(axis='y', alpha=0.25)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def main():
    repo_root = Path(__file__).parent
    json_path = repo_root / 'monthl_sales.json'
    if not json_path.exists():
        print('ERROR: monthl_sales.json not found in workspace root.')
        return

    data = load_data(json_path)

    months = [row['Month'] for row in data]
    sales = [row['Sales'] for row in data]

    out_line = repo_root / 'line_chart.png'
    out_bar = repo_root / 'bar_chart.png'

    make_line_chart(months, sales, out_line)
    make_bar_chart(months, sales, out_bar)

    print(f'Charts saved: {out_line.name}, {out_bar.name}')


if __name__ == '__main__':
    main()
