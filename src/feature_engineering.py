import pandas as pd


def engineer_customer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create a cleaned customer-level dataframe for modeling."""
    df = df.copy()

    # Convert binary flags to numeric values
    if "has_gas" in df.columns:
        df["has_gas"] = df["has_gas"].map({"t": 1, "f": 0}).astype("Int64")

    if "churn" in df.columns:
        df["churn"] = df["churn"].astype(int)

    # Keep key business features and fill missing values for model readiness
    for col in ["cons_12m", "cons_last_month", "net_margin", "pow_max", "num_years_antig"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].fillna(df[col].median())

    return df


def create_price_derived_features(price_df: pd.DataFrame) -> pd.DataFrame:
    """Create basic price trend features from the price dataset."""
    price_df = price_df.copy()
    price_df["price_date"] = pd.to_datetime(price_df["price_date"])

    price_df["avg_price"] = price_df[
        ["price_off_peak_var", "price_peak_var", "price_mid_peak_var",
         "price_off_peak_fix", "price_peak_fix", "price_mid_peak_fix"]
    ].mean(axis=1)

    return price_df
