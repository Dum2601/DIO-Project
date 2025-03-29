# -----------------------------------------------------------------
# Utilitaries

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

sales_path = '' # Ponha o caminho do arquivo na String / Put the file path in the String

df = pd.read_csv(sales_path)

# ------------------------------------------------------------------
# Improving treatments

df.dropna(inplace=True) # Removing null values
df.drop_duplicates(inplace=True) # Removing duplicated data


# -------------------------------------------------------------------
# Visual graphs

print(df.head)

df.plot(figsize=(10, 6)) # values recommended by chatGPT (used only to help with the minors visibilities tricks)
plt.show()
