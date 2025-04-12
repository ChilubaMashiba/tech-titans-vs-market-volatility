import yfinance as yf

def fetch_data(tickers, start='2020-01-01', end='2024-12-31'):
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    return data

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'TSLA', 'NVDA', '^GSPC', '^IXIC']
    df = fetch_data(tickers)
    print(df.head())
