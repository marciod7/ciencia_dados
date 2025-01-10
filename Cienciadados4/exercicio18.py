import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Caminho do arquivo
file_path = r'C:/Users/User/Desktop/ciênciadados/ciênciadados4/Online Retail.xlsx'

# Leitura e preparação dos dados
df_retail = pd.read_excel(file_path, index_col=0, engine='openpyxl')

# Remover registros sem descrição
df_retail = df_retail.dropna(subset=['Description'])

# Assegurar que a coluna "Description" seja do tipo string
df_retail = df_retail.astype({"Description": "str"})

# Agrupar as descrições por número de fatura
trans = df_retail.groupby(['InvoiceNo'])['Description'].apply(list).to_list()

# Codificar as transações
encoder = TransactionEncoder()
encoded_array = encoder.fit(trans).transform(trans)
df_retail_encoded = pd.DataFrame(encoded_array, columns=encoder.columns_)

# Encontrar itemsets frequentes
frequent_itemsets = apriori(df_retail_encoded, min_support=0.025, use_colnames=True)

# Gerar regras de associação
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)
print(rules.iloc[:, 0:7])
