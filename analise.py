# -----------------------------------------------------------------
# Utilitaries

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

sales_path = '/home/doug_b_souza/Documentos/Estudo/Programação/Projetos/Projetos DIO/Análise de dados com Python e Pandas/Sales Data Analysis.csv' # Substituir pelo caminho desejado

df = pd.read_csv(sales_path)

# ------------------------------------------------------------------
# Improving treatments

df.dropna(inplace=True) # Removing null values
df.drop_duplicates(inplace=True) # Removing duplicated data


# -------------------------------------------------------------------
# Visual graphs

print(df.head)

df.plot(figsize=(10, 6))
plt.show()