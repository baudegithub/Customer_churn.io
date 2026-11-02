import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_loader import load_client_data


def plot_churn_distribution(df: pd.DataFrame) -> None:
    churn_share = df["churn"].value_counts(normalize=True).reindex([0, 1], fill_value=0) * 100
    labels = ["Retention", "Churn"]
    values = [churn_share.get(0, 0), churn_share.get(1, 0)]

    plt.figure(figsize=(7, 5))
    ax = sns.barplot(x=labels, y=values, palette=["#2E8B57", "#D9534F"])
    ax.set_title("Churn Status of Customers", fontsize=14, weight="bold")
    ax.set_ylabel("Percentage (%)")
    ax.set_xlabel("")

    for container in ax.containers:
        ax.bar_label(container, labels=[f"{v:.1f}%" for v in values], padding=3, fontsize=11)

    plt.tight_layout()
    plt.show()


def plot_churn_by_gas(df: pd.DataFrame) -> None:
    gas_df = df[["has_gas", "churn"]].copy()
    gas_df["has_gas"] = gas_df["has_gas"].map({"t": "Has Gas", "f": "No Gas"})
    summary = gas_df.groupby("has_gas")["churn"].mean().mul(100).reset_index()
    summary.columns = ["Gas Service", "Churn Rate (%)"]

    plt.figure(figsize=(7, 5))
    ax = sns.barplot(data=summary, x="Gas Service", y="Churn Rate (%)", palette=["#4C78A8", "#F58518"])
    ax.set_title("Churn Rate by Gas Service", fontsize=14, weight="bold")
    ax.set_ylabel("Churn Rate (%)")
    ax.set_xlabel("")

    for p in ax.patches:
        ax.annotate(f"{p.get_height():.1f}%", (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha="center", va="bottom", fontsize=11)

    plt.tight_layout()
    plt.show()


def plot_churn_by_tenure(df: pd.DataFrame) -> None:
    summary = df.groupby("num_years_antig")["churn"].mean().mul(100).reset_index()
    summary.columns = ["Tenure (years)", "Churn Rate (%)"]

    plt.figure(figsize=(8, 5))
    ax = sns.lineplot(data=summary, x="Tenure (years)", y="Churn Rate (%)", marker="o", linewidth=2.5)
    ax.set_title("Churn Rate by Customer Tenure", fontsize=14, weight="bold")
    ax.set_xlabel("Customer tenure (years)")
    ax.set_ylabel("Churn Rate (%)")

    for x, y in zip(summary["Tenure (years)"], summary["Churn Rate (%)"]):
        ax.annotate(f"{y:.1f}%", (x, y), textcoords="offset points", xytext=(0, 6), ha="center", fontsize=9)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df = load_client_data()
    plot_churn_distribution(df)
    plot_churn_by_gas(df)
    plot_churn_by_tenure(df)
