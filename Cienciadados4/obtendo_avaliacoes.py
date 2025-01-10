from langdetect import detect
import pandas as pd

# Função para detectar idioma localmente
def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        print(f"Erro ao detectar idioma para o texto: '{text}'. Erro: {e}")
        return None

# Dados de exemplo
data = {
    'title': [
        "This is amazing!", 
        "Produto excelente", 
        "Très mauvais service", 
        "Muy buen produto", 
        "Horrible experience"
    ],
    'rating': [5, 5, 1, 4, 1]
}
df = pd.DataFrame(data)

# Detectar idioma
df['lang'] = df['title'].apply(detect_language)

# Exibir os resultados
print("\nResultados:")
df = df[df['lang'] == 'en']
print(df)
