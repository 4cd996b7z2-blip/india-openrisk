import pandas as pd
import requests
from io import StringIO
from pathlib import Path

DATA_DIR = Path("data/reference")
DATA_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}


def fetch_sp500_constituents() -> pd.DataFrame:
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()

    table = pd.read_html(StringIO(response.text), attrs={"id": "constituents"})[0]
    table = table[["Symbol", "Security", "GICS Sector", "GICS Sub-Industry"]]
    table.columns = ["ticker", "company_name", "sector", "sub_industry"]
    return table


def fetch_nifty500_constituents() -> pd.DataFrame:
    url = "https://archives.nseindia.com/content/indices/ind_nifty500list.csv"
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()

    table = pd.read_csv(StringIO(response.text))
    table.columns = [c.strip().lower().replace(" ", "_") for c in table.columns]
    return table


def main():
    sp500 = fetch_sp500_constituents()
    sp500.to_csv(DATA_DIR / "sp500_constituents.csv", index=False)
    print(f"S&P 500: {len(sp500)} tickers saved")

    nifty500 = fetch_nifty500_constituents()
    nifty500.to_csv(DATA_DIR / "nifty500_constituents.csv", index=False)
    print(f"Nifty 500: {len(nifty500)} tickers saved")


if __name__ == "__main__":
    main()