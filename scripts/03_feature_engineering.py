import pandas as pd


def engineer_customer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "has_gas" in df.columns:
        df["has_gas"] = df["has_gas"].map({"t": 1, "f": 0}).astype("Int64")

    if "churn" in df.columns:
        df["churn"] = df["churn"].astype(int)

    for col in ["cons_12m", "cons_last_month", "net_margin", "pow_max", "num_years_antig"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].fillna(df[col].median())

    return df


if __name__ == "__main__":
    from src.data_loader import load_client_data

    df = load_client_data()
    transformed = engineer_customer_features(df)
    print(transformed.head())
