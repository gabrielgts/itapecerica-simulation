# -*- coding: utf-8 -*-
# Bibliotecas para manuseio dos dados
import pandas as pd
import numpy as np

# datasheet
dataset = pd.read_csv("2020.csv", encoding='utf8',
                      delimiter=';', engine='python')


items = {}

df = pd.DataFrame({})

for index, row in dataset.iterrows():
    df.at[row['HORA_AMOSTRAGEM'], 'estacao'] = row['estacao']
    df.at[row['HORA_AMOSTRAGEM'], row['NOME_PARAMETRO']] = row['RESULTADO']


print(df)

# dataset['IQA'] = (dataset['Oxigenio dissolvido'].astype('float32') ** 0.17) * \
#     (dataset['Coliformes totais'].astype('float32') ** 0.15) * \
#     (dataset['pH in loco'].astype('float32') ** 0.12) * \
#     (dataset['Demanda Bioquimica de Oxigenio'].astype('float32') ** 0.1) * \
#     ((dataset['Nitrogenio amoniacal total'].astype('float32') + dataset['Nitrogenio organico'].astype('float32')) ** 0.1) * \
#     (dataset['Fosforo total'].astype('float32') ** 0.1) * \
#     (dataset['Temperatura da agua'].astype('float32') ** 0.1) * \
#     (dataset['Turbidez'].astype('float32') ** 0.08) * \
#     (dataset['Solidos totais'].astype('float32') ** 0.08)

# # remove valores not a number
# dataset = dataset[dataset['IQA'].notna()]

# newDataset = newDataset.sort_values(by='data')

# mean_col = newDataset.groupby('data')['IQA'].mean()  # don't reset the index!

df.to_csv('2020_before_iqa_1.csv', sep=';', encoding='utf-8')
