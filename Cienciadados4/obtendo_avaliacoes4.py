import yfinance as yf
import pandas_datareader.data as pdr
from datetime import date, timedelta

# Obter dados da ação
tkr = yf.Ticker('AAPL')
hist = tkr.history(period='1y')

# Ajustar o índice de datas para tz-naive (sem horário) em ambos os DataFrames
hist.index = hist.index.normalize()  # Remove o horário no índice de datas de 'hist'

# Obter dados do índice
end = date.today()
start = end - timedelta(days=365)
index_data = pdr.get_data_stooq('^SPX', start, end)

# Ajustar o índice de datas de 'index_data' para tz-naive (sem horário)
index_data.index = index_data.index.normalize()

# Fazer o join dos dados com as datas em comum (remover os NaN)
df = hist.join(index_data, rsuffix='_idx', how='inner')

# Selecionar as colunas de interesse
df = df[['Close', 'Volume', 'Close_idx', 'Volume_idx']]

# Exibir o DataFrame final
print(df)
