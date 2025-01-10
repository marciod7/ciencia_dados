import pandas as pd
import yfinance as yf

# Inicializar um DataFrame vazio
stocks = pd.DataFrame()

# Lista de tickers
tickers = ['MSFT', 'TSLA', 'GM', 'AAPL', 'ORCL', 'AMZN']

# Loop através dos tickers para obter dados históricos
for ticker in tickers:
    tkr = yf.Ticker(ticker)
    hist = tkr.history(period='5d')
    hist = hist[['Close']].rename(columns={'Close': ticker})
    if stocks.empty:
        stocks = hist
    else:
        stocks = stocks.join(hist)

# Exibir o DataFrame resultante
print(stocks)

stocks_to_keep = []
for i in stocks.columns:
    if stocks[stocks[i] / stocks[i].shift(1)< 0.97].empty:
        stocks_to_keep.append(i)
print(stocks_to_keep)
