from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_client_data(path: str | None = None) -> pd.DataFrame:
    """Load the customer-level dataset."""
    file_path = Path(path) if path else DATA_DIR / "client_data.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"Client data file not found: {file_path}")
    return pd.read_csv(file_path)


def load_price_data(path: str | None = None) -> pd.DataFrame:
    """Load the pricing dataset."""
    file_path = Path(path) if path else DATA_DIR / "price_data.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"Price data file not found: {file_path}")
    return pd.read_csv(file_path)


def merge_client_and_price_data(client_df: pd.DataFrame, price_df: pd.DataFrame) -> pd.DataFrame:
    """Merge customer and price datasets on customer id."""
    return client_df.merge(price_df, on="id", how="left")
