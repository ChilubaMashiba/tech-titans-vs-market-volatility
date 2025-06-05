# Tech Titans vs Market Volatility
This project analyzes whether major tech companies Apple (AAPL), Microsoft (MSFT), Tesla (TSLA), and Nvidia (NVDA) behave more like resilient or risky assets during periods of financial crises, by comparing them to market indices like the S&P 500 (^GSPC) and Nasdaq (^IXIC). 
Periods of financial stress often trigger a “flight to quality,” where investors move from riskier assets to safer ones. This study explores whether tech stocks exhibit defensive characteristics or increased sensitivity during such periods, offering insights into asset allocation, financial contagion, and sector-specific behavior under systemic stress.

# Data Collection and Preparation
We downloaded daily adjusted closing prices from Yahoo Finance for each stock and index from 2010 to 2024 using Python’s yfinance library. This dataset provides a consistent historical basis for examining the behavior of tech stocks and market indices.

# Our research question is: 
Do major technology stocks behave more like resilient (defensive) assets or risky assets during periods of financial market stress?

# Analysis
We apply a series of time-series analyses. Specifically, we compute:
# Daily Returns
We calculated the daily returns for each stock to understand their day-to-day fluctuations. Daily returns show how much the value of a stock changes in a day, which is crucial for assessing both short-term volatility and investor exposure to rapid market movements.
# Time-Varying Risk Dynamics (Rolling Measures)
Rolling window analysis was employed to capture the evolving behavior of assets during financial crises.
# Rolling Volatility (30-day)
Measures the short-term fluctuation in stock prices. Spikes in volatility often signal stress periods or uncertainty in the market.
# Rolling Beta (60-day)
Rolling beta tracks how sensitive each stock is to market movements over time. A higher beta indicates stronger co-movement with the market, while a lower beta suggests more independence.
# Rolling Correlation (60-day)
This measure shows how closely the stocks move with the S&P 500 and Nasdaq over time. Sudden drops or surges may reflect shifts in investor sentiment or systemic contagion.

Together, these analyses provide a comprehensive perspective on each stock’s volatility, market sensitivity, and co-movement patterns, enhancing our understanding of their behavior during periods of financial stress relative to broader indices.

# Visualizations
We include time-series plots for daily returns and rolling measures, highlighting structural shifts during key market stress periods such as the Eurozone crisis, COVID-19 crash, and the inflation-driven drawdown.

# Key Findings
-
-
-

# Local Setup 
Ensure that your environment has the following:
- Python 3.8+
- Jupyter Notebook or JupyterLab
- Libraries: pandas, matplotlib, seaborn, yfinance, numpy
- Version Control: Git, GitHub

# Authors
Chiluba Mashiba, Alina Ruzhentseva









