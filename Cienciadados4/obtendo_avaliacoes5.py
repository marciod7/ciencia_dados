import yfinance as yf
import pandas_datareader.data as pdr
import numpy as np
from datetime import date, timedelta
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Obtenção dos dados históricos da AAPL
tkr = yf.Ticker('AAPL')
hist = tkr.history(period="1y")

# Obtenção dos dados do índice S&P 500
end = date.today()
start = end - timedelta(days=365)
index_data = pdr.get_data_stooq('^SPX', start=start, end=end)

# Convertendo os índices para 'tz-naive' (sem fuso horário)
hist.index = hist.index.tz_localize(None)
index_data.index = index_data.index.tz_localize(None)

# Unindo os dados da AAPL e do índice S&P 500
df = hist.join(index_data, rsuffix='_idx')

# Verificando as colunas após o join
print("Colunas de df após o join:")
print(df.columns)

# Seleção das colunas de interesse
df = df[['Close', 'Volume', 'Close_idx', 'Volume_idx']]

# Preenchendo os NaNs com o valor anterior (forward fill)
df.ffill(inplace=True)

# Calculando as variações logarítmicas
df['priceRise'] = np.log(df['Close'] / df['Close'].shift(1))
df['volumeRise'] = np.log(df['Volume'] / df['Volume'].shift(1))
df['priceRise_idx'] = np.log(df['Close_idx'] / df['Close_idx'].shift(1))
df['volumeRise_idx'] = np.log(df['Volume_idx'] / df['Volume_idx'].shift(1))

# Removendo NaNs após o cálculo das variações
df.dropna(inplace=True)

# Selecionando apenas as colunas de variação
df = df[['priceRise', 'volumeRise', 'priceRise_idx', 'volumeRise_idx']]
print(df)
# Criando a coluna 'Pred' para a previsão
conditions = [
    (df['priceRise'].shift(-1) >  0.01),  # Previsão de alta (>1%)
    (df['priceRise'].shift(-1) < -0.01)   # Previsão de queda (<-1%)
]
choices = [1, -1]
df['Pred'] = np.select(conditions, choices, default=0)  # Pred = 0 para movimentos menores
print(df)
# Transformando as features e o target em numpy arrays
features = df[['priceRise', 'volumeRise', 'priceRise_idx', 'volumeRise_idx']].to_numpy()
features = np.around(features, decimals=2)
target = df['Pred'].to_numpy()

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Treinando o modelo de Regressão Logística
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Avaliando o modelo
accuracy = clf.score(X_test, y_test)
print(f"\nAcurácia do modelo de Regressão Logística: {accuracy * 100:.2f}%")
