import os
import pandas as pd
import numpy as np
from tqdm import tqdm

df_list = []
for file in os.listdir('data/archive (1)/'):
  df_aux = pd.read_csv(f'data/archive (1)/{file}', low_memory=False)
  df_list.append(df_aux)
df = pd.concat(df_list, ignore_index=True)

print(df.columns)

df.drop(columns=['Dst IP', 'Dst Port', 'Src Port', 'Src IP', 'Protocol', 'Flow ID'], inplace=True)

# Loop sobre todas as colunas do DataFrame
for column in tqdm(df.columns):
    # Verificar se a coluna precisa ser convertida para tipo numérico
    if df[column].dtype == 'object' and column != 'Label':
        # Converter a coluna para tipo numérico, coercing valores não numéricos para NaN
        df[column] = pd.to_numeric(df[column], errors='coerce')
        # Calcular a mediana dos valores existentes na coluna
        median_value = df[column].median()
        # Preencher os valores NaN na coluna com a mediana calculada
        df[column].fillna(median_value, inplace=True)

# Verificar se ainda há valores NaN no DataFrame
print(df.isna().sum())

# Salvar o DataFrame em formato Parquet
df.to_parquet('data/cse_cic_ids_2018.parquet')