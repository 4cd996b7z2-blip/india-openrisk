import os
from pathlib import Path

import pandas as pd
import requests
import yfinance as yf
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

START = "2015-01-01"
END = None

YF_TICKERS = {
    "sp500": "^GSPC",
    "nasdaq100": "^NDX",
    "vix": "^VIX",
    "nifty50": "^NSEI",
}


def fetch_yf_series(name: str, ticker: str) -> pd.DataFrame:
    df = yf.download(ticker, start=START, end=END, progress=False)
    df.to_csv(DATA_DIR / f"{name}.csv")
    return df


def fetch_fred_series(series_id: str) -> pd.DataFrame:
    api_key = os.environ["FRED_API_KEY"]
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
        "observation_start": START,
    }
    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    obs = response.json()["observations"]
    df = pd.DataFrame(obs)[["date", "value"]]
    df.to_csv(DATA_DIR / "us_10yr_yield.csv", index=False)
    return df


def main():
    for name, ticker in YF_TICKERS.items():
        df = fetch_yf_series(name, ticker)
        print(f"{name}: {len(df)} rows saved")

    yield_df = fetch_fred_series("DGS10")
    print(f"us_10yr_yield: {len(yield_df)} rows saved")


if __name__ == "__main__":
    main()