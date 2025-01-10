#Passo a Passo de Cálculo de Janela Rolante
import pandas as pd

# Criação de uma série temporal de exemplo
data = {'Tempo': [1, 2, 3, 4, 5], 'Valor': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Cálculo da média móvel com janela rolante de tamanho 3
df['Media_Movel'] = df['Valor'].rolling(window=3).mean()
print(df)

#Exemplo Adicional: Desvio Padrão Rolante
import pandas as pd

data = {'Tempo': [1, 2, 3, 4, 5], 'Valor': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Cálculo do desvio padrão rolante com janela de tamanho 3
df['Desvio_Padrao_Rolante'] = df['Valor'].rolling(window=3).std()
print(df)

#Desvio Padrão Rolante
import pandas as pd

# Dados de exemplo
data = {'Dia': [1, 2, 3, 4, 5], 'Preco': [100, 102, 105, 107, 110]}
df = pd.DataFrame(data)

# Cálculo do desvio padrão rolante com janela de tamanho 3
df['Desvio_Padrao_Rolante'] = df['Preco'].rolling(window=3).std()
print(df)

import pandas as pd

# Dados fictícios de exemplo
data = {'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
        'Close': [100, 102, 105, 103, 104, 106, 107, 109, 110, 108, 107, 106, 105, 107, 108, 109, 110, 112, 114, 115, 113, 112, 111, 110, 109, 111, 112, 113, 114, 115]}
df = pd.DataFrame(data)

# Cálculo da média móvel com janela de 5 dias
df['5dayAvg'] = df['Close'].rolling(window=5).mean()
print(df[['Date', 'Close', '5dayAvg']])

#Por Que Usar uma Janela Rolante?
import pandas as pd

# Dados de exemplo
data = {'Dia': range(1, 11), 'Preco': [100, 102, 105, 107, 110, 108, 107, 106, 109, 111]}
df = pd.DataFrame(data)

# Cálculo da média móvel com janela de tamanho 3
df['Media_Movel_3dias'] = df['Preco'].rolling(window=3).mean()
print(df)
