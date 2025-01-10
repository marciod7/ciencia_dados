import yfinance as yf
import pandas as pd
import numpy as np
ticker = 'TSLA'
tkr = yf.Ticker(ticker)
df = tkr.history(period='5d')

#print(pd.concat([df['Close'], df['Close'].shift(2)], axis=1, keys=['Close', '2DaysShift']))

df['2daysRise'] = np.log(df['Close'] / df['Close'].shift(2))
df['2daysAvg'] = df['Close'].shift(1).rolling(2).mean()
df['2daysAvgRise'] = np.log(df['Close'] / df['2daysAvg'])
print(df[['Close', '2daysRise', '2daysAvgRise']])
print(df[['Close', '2DaysRise']])
print(df[['Close', '2daysAvg']])
