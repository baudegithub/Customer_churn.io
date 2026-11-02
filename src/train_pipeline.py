from __future__ import annotations

import pandas as pd
from sklearn.model_selection import train_test_split

from src.data_loader import load_client_data
from src.eda import plot_churn_distribution, plot_churn_by_gas, plot_churn_by_tenure
from src.feature_engineering import engineer_customer_features
from src.modeling import build_model_pipeline
from src.evaluation import evaluate_model


def run_pipeline() -> None:
    """Run the customer churn workflow end-to-end."""
    client_df = load_client_data()

    # Exploratory analysis
    plot_churn_distribution(client_df)
    plot_churn_by_gas(client_df)
    plot_churn_by_tenure(client_df)

    # Feature preparation
    model_df = engineer_customer_features(client_df)
    X = model_df.drop(columns=["churn", "id"]) if "id" in model_df.columns else model_df.drop(columns=["churn"])
    y = model_df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = build_model_pipeline(X_train, y_train)
    metrics = evaluate_model(model, X_test, y_test)

    print("Model performance:")
    for key, value in metrics.items():
        if isinstance(value, float):
            print(f"- {key}: {value:.4f}")
        else:
            print(f"- {key}: {value}")


if __name__ == "__main__":
    run_pipeline()
