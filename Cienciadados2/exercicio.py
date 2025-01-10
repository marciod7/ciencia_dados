import yfinance as yf
import numpy as np
import pandas as pd

# Obter dados da Tesla
ticker = 'TSLA'
tkr = yf.Ticker(ticker)
df = tkr.history(period='1mo')

# Selecionar e renomear colunas
df = df[['Close', 'Volume']].rename(columns={'Close': 'Price'})

# Calcular variação logarítmica de preço
df['priceRise'] = np.log(df['Price'] / df['Price'].shift(1))

# Calcular variação logarítmica de volume
df['volumeRice'] = np.log(df['Volume'] / df['Volume'].shift(1))

# Calcular soma dos volumes dos dois dias anteriores
df['volumeSum'] = df['Volume'].shift(1).rolling(2).sum().fillna(0).astype(int)

# Calcular volume do próximo dia
df['nextvolume'] = df['Volume'].shift(-1).fillna(0).astype(int)

# Calcular soma dos priceRise dos dois dias anteriores
df['priceRiseSum'] = df['priceRise'].rolling(2).sum().fillna(0)

# Análise dos dados
print("Dias com grandes variações de preço (abs(priceRise) > 0.05):")
print(df[abs(df['priceRise']) > 0.05])

print("\nMédia da variação logarítmica de volume:")
print(df['volumeRice'].mean().round(4))

print("\nMédia da variação de volume nos dias com grandes variações de preço:")
print(df[abs(df['priceRise']) > 0.05]['volumeRice'].mean().round(4))

print("\nAnálise com a nova métrica (priceRiseSum) e volumeSum:")
print(df[abs(df['priceRise']) > 0.05][['priceRiseSum', 'volumeSum', 'volumeRice']])

print("\nDados com grandes variações de preço e sem zeros (limpeza dos dados):")
print(df[abs(df['priceRise']) > 0.05].replace(0, np.nan).dropna())
