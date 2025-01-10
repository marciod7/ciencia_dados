from langdetect import detect
import pandas as pd

# Função para detectar idioma localmente
def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        print(f"Erro ao detectar idioma para o texto: '{text}'. Erro: {e}")
        return None

# Caminho do arquivo
file_path = 'C:/Users/User/Desktop/ciênciadados/ciênciadados4/reviews.csv'

# Carregar dados do arquivo CSV
df = pd.read_csv(file_path)

# Exibir as primeiras linhas do DataFrame para verificar os dados
print("Dados originais:")
print(df.head())

# Detectar idioma da coluna 'title'
df['lang'] = df['title'].apply(detect_language)

# Exibir os resultados com todos os idiomas detectados
print("\nResultados com detecção de idiomas:")
print(df)

# Salvar o DataFrame com os idiomas detectados em um novo arquivo CSV (opcional)
output_path = 'C:/Users/User/Desktop/ciênciadados/ciênciadados4/reviews_with_lang.csv'
df.to_csv(output_path, index=False)
print(f"\nArquivo salvo com idiomas detectados: {output_path}")
