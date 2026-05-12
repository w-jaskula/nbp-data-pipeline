import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import get_logger

DB_PATH = "../data/nbp.db"
logger = get_logger(__name__)


def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM rates", conn)
    conn.close()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(["currency", "date"])
    logger.info(f"Loaded {len(df)} records from database for analysis")
    return df


def build_financial_table(df):
    # --- Monthly Performance Table ---
    df = df.copy()
    df["month"] = df["date"].dt.strftime('%b')
    monthly = df.groupby(['currency', 'month'], sort=False).last().reset_index()
    monthly['pct_diff'] = monthly.groupby('currency')['rate'].pct_change() * 100

    pivot = monthly.pivot(index='currency', columns='month', values=['rate', 'pct_diff'])
    pivot = pivot.swaplevel(0, 1, axis=1)

    order = ['Mar', 'Feb', 'Jan']
    existing_months = [m for m in order if m in pivot.columns.get_level_values(0)]
    pivot = pivot.reindex(columns=existing_months, level=0)
    pivot = pivot.rename(columns={'rate': 'Exchange Rate', 'pct_diff': '% Change (MoM)'})
    return pivot


def plot_dynamics(df):
    logger.info("Generating currency dynamics charts...")
    sns.set_theme(style="darkgrid")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # --- Chart 1: Indexed Performance (Base 100) ---
    df['indexed'] = df.groupby('currency')['rate'].transform(lambda x: (x / x.iloc[0]) * 100)
    sns.lineplot(data=df, x="date", y="indexed", hue="currency", ax=ax1, linewidth=2.5)
    ax1.axhline(100, color='black', linestyle='--', alpha=0.5)
    ax1.set_title("Currency Performance Index Q1 2026 (Base 100)", fontsize=14, pad=15)
    ax1.set_ylabel("Performance Index (Start = 100)")
    ax1.set_xlabel("")

    # --- Chart 2: Volatility (Daily % Change) ---
    sns.lineplot(data=df, x="date", y="pct_change", hue="currency", ax=ax2, alpha=0.7)
    ax2.set_title("Daily Exchange Rate Volatility (%)", fontsize=12)
    ax2.set_ylabel("Daily % Change")
    ax2.axhline(0, color='red', linewidth=1, alpha=0.3)

    plt.tight_layout()
    plt.show()


def main():
    try:
        df = load_data()
        print("\n" + "=" * 85)
        print("NBP FX Report: Q1 2026 (Monthly Summary)")
        print("=" * 85)

        table = build_financial_table(df)
        print(table.round(3).fillna("-").to_markdown(tablefmt="grid"))
        print("=" * 85 + "\n")

        plot_dynamics(df)
        logger.info("Analysis completed successfully")

    except Exception as e:
        logger.error(f"Analysis Error: {e}")
        print("Please ensure the 'tabulate' library is installed: pip install tabulate")


if __name__ == "__main__":
    main()