# Bibliotecas para manuseio dos dados
import pandas as pd
import numpy as np

# datasheet
dataset = pd.read_csv("parametros_ssinal_trasformed.csv", encoding='utf8',
                      delimiter=';', engine='python')

dataset['Data de Amostragem'] = pd.to_datetime(dataset['Data de Amostragem'])

print(dataset.columns.tolist())

dataset = dataset.fillna(0)

dataset['IQA'] = (dataset['Oxigenio dissolvido'].astype('float32') ** 0.17) * \
    (dataset['Coliformes totais'].astype('float32') ** 0.15) * \
    (dataset['pH in loco'].astype('float32') ** 0.12) * \
    (dataset['Demanda Bioquimica de Oxigenio'].astype('float32') ** 0.1) * \
    ((dataset['Nitrogenio amoniacal total'].astype('float32') + dataset['Nitrogenio organico'].astype('float32')) ** 0.1) * \
    (dataset['Fosforo total'].astype('float32') ** 0.1) * \
    (dataset['Temperatura da agua'].astype('float32') ** 0.1) * \
    (dataset['Turbidez'].astype('float32') ** 0.08) * \
    (dataset['Solidos totais'].astype('float32') ** 0.08)


newDataset = pd.DataFrame({
    'IQA': dataset['IQA'],
    'oxigenio_dissolvido': dataset['Oxigenio dissolvido'].astype('float32'),
    'coliformes_totais': dataset['Coliformes totais'].astype('float32'),
    'pH_loco': dataset['pH in loco'].astype('float32'),
    'demanda_bioquimica_oxigenio': dataset['Demanda Bioquimica de Oxigenio'].astype('float32'),
    'nitrogenio_total': dataset['Nitrogenio amoniacal total'].astype('float32') + dataset['Nitrogenio organico'].astype('float32'),
    'fosforo_total': dataset['Fosforo total'].astype('float32'),
    'temperatura_da_agua': dataset['Temperatura da agua'].astype('float32'),
    'turbidez': dataset['Turbidez'].astype('float32'),
    'solidos_totais': dataset['Solidos totais'].astype('float32'),
    'data': dataset['Data de Amostragem']
})

newDataset = newDataset.sort_values(by='data')

newDataset.to_csv('iqa_.csv', encoding='utf-8')
