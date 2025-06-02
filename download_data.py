import yfinance as yf
import pandas as pd
import os

def fetch_data(tickers, start='2010-01-01', end='2024-12-31'):
    all_data = pd.DataFrame()

    for ticker in tickers:
        try:
            print(f"Downloading {ticker}...")
            data = yf.download(ticker, start=start, end=end, auto_adjust=False)

            if 'Adj Close' in data.columns:
                all_data[ticker] = data['Adj Close']
            else:
                print(f"⚠️ Skipping {ticker}: 'Adj Close' not found in data.columns → {list(data.columns)}")

        except Exception as e:
            print(f"❌ Failed to download {ticker}: {e}")

    return all_data

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'TSLA', 'NVDA', '^GSPC', '^IXIC']

    df = fetch_data(tickers)

    if not df.empty:
        # Ensure data/ folder exists
        os.makedirs("data", exist_ok=True)

        df.to_csv("data/tech_vs_index_prices.csv")
        print("✅ Data successfully saved to data/tech_vs_index_prices.csv")
        print(df.head())
    else:
        print("⚠️ No data fetched.")
