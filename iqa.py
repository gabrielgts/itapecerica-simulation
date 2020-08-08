# Bibliotecas para manuseio dos dados
import pandas as pd
import numpy as np

# datasheet
dataset = pd.read_csv("parametros_ssinal_trasformed.csv", encoding='utf8',
                      delimiter=';', engine='python')

print(dataset.head())

dataset.info()

dataset['Turbidez'].astype('float32')

print(dataset.columns.tolist())

dataset = dataset.fillna(0)

print(dataset['Turbidez'])


dataset['IQA'] = (dataset['Oxigênio dissolvido'] * 0.17) + \
    (dataset['Coliformes termotolerantes'] * 0.15) + \
    (dataset['pH laboratório'] * 0.12) + \
    (dataset['Demanda Bioquímica de Oxigênio'] * 0.1) + \
    ((dataset['Nitrogênio amoniacal total'] + dataset['Nitrogênio orgânico']) * 0.1) + \
    (dataset['Fósforo total'] * 0.1) + \
    (dataset['Temperatura da água'] * 0.1) + \
    (dataset['Turbidez'] * 0.08) + \
    (dataset['Sólidos totais'] * 0.08)

print(dataset['IQA'])


dataset['IQA'].to_csv('normalized_data_iqa.csv', encoding='utf-8')
