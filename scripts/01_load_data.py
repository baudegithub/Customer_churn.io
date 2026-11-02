from pathlib import Path
import pandas as pd


def load_client_data(path: str | None = None) -> pd.DataFrame:
    """Load the customer-level dataset."""
    base_dir = Path(__file__).resolve().parents[1]
    data_dir = base_dir / "data"
    file_path = Path(path) if path else data_dir / "client_data.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"Client data file not found: {file_path}")

    return pd.read_csv(file_path)


def load_price_data(path: str | None = None) -> pd.DataFrame:
    """Load the price dataset."""
    base_dir = Path(__file__).resolve().parents[1]
    data_dir = base_dir / "data"
    file_path = Path(path) if path else data_dir / "price_data.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"Price data file not found: {file_path}")

    return pd.read_csv(file_path)


if __name__ == "__main__":
    client_df = load_client_data()
    price_df = load_price_data()
    print(client_df.head())
    print(price_df.head())
