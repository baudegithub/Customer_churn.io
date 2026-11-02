import pandas as pd
from sklearn.model_selection import train_test_split

from src.data_loader import load_client_data
from src.feature_engineering import engineer_customer_features
from src.modeling import build_model_pipeline


def train_model() -> tuple:
    df = load_client_data()
    model_df = engineer_customer_features(df)

    X = model_df.drop(columns=["churn", "id"]) if "id" in model_df.columns else model_df.drop(columns=["churn"])
    y = model_df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = build_model_pipeline(X_train, y_train)
    return model, X_test, y_test


if __name__ == "__main__":
    model, X_test, y_test = train_model()
    print("Model trained successfully.")
    print(model)
