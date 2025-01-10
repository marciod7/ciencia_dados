import pandas as pd
from googletrans import Translator
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn import metrics

# Leitura do arquivo CSV
try:
    df = pd.read_csv('reviews.csv')
except FileNotFoundError:
    print("Erro: Arquivo 'reviews.csv' não encontrado.")
    exit()

print('Número de avaliações: ', len(df))

# Garantindo que as colunas necessárias existem
if 'title' not in df.columns or 'rating' not in df.columns:
    print("Erro: O arquivo CSV deve conter as colunas 'title' e 'rating'.")
    exit()

# Verificando valores nulos
df = df.dropna(subset=['title', 'rating'])

# Criando uma instância do tradutor
detector = Translator()

# Função para detectar idioma
def detect_lang(text):
    try:
        return detector.detect(text).lang
    except Exception as e:
        print(f"Erro ao detectar idioma do texto '{text}': {e}")
        return 'unknown'

# Detectando o idioma dos títulos
df['lang'] = df['title'].apply(detect_lang)

# Filtrando apenas avaliações em inglês
df = df[df['lang'] == 'en']
print('Número de avaliações em inglês:', len(df))

# Remover texto desnecessário na coluna 'rating'
df['rating'] = df['rating'].str.replace(' out of 5 stars', '', regex=False)

# Garantir que os valores sejam numéricos
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Remover valores ausentes após a conversão
df = df.dropna(subset=['rating'])

# Verificar os valores únicos após a limpeza
print("Valores únicos na coluna 'rating' após limpeza:", df['rating'].unique())

# Adicionando o comando para agrupar e contar os ratings
print(df.groupby('rating').size())

# Convertendo ratings para classes categóricas (binárias)
ratings = np.where(df['rating'] >= 4, 1, 0)

# Preparando os dados para treino e teste
reviews = df['title'].values

# Dividindo os dados em treino e teste
reviews_train, reviews_test, y_train, y_test = train_test_split(reviews, ratings, test_size=0.2, random_state=1000)

# Transformando os textos em vetores de contagem
vectorizer = CountVectorizer()
vectorizer.fit(reviews_train)
x_train = vectorizer.transform(reviews_train)
x_test = vectorizer.transform(reviews_test)

# Treinando o modelo
classifier = LogisticRegression(max_iter=1000)
classifier.fit(x_train, y_train)

# Avaliando o modelo
predicted = classifier.predict(x_test)
accuracy = np.mean(predicted == y_test)
print("Accuracy:", round(accuracy, 2))
print(metrics.confusion_matrix(y_test, predicted, labels=[0, 1]))

# Adicionando o relatório de classificação com zero_division
print(metrics.classification_report(y_test, predicted, labels=[0, 1], zero_division=1))
