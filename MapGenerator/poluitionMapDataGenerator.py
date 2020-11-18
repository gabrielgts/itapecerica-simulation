# -*- coding: utf-8 -*-
# Bibliotecas para manuseio dos dados
import pandas as pd
import numpy as np
import re

# datasheet
dataset = pd.read_csv("parametros_map.csv", encoding='utf8',
                      delimiter=';', engine='python')

dataset['Data de Amostragem'] = pd.to_datetime(dataset['Data de Amostragem'])

dataset['Data de Amostragem'] = pd.to_datetime(
    dataset['Data de Amostragem'], unit='s').dt.strftime('%Y-%m-%d %H:%M')

print(dataset.columns.tolist())

dataset['IQA'] = (dataset['Oxigenio dissolvido'].astype('float32') ** 0.17) * \
    (dataset['Coliformes totais'].astype('float32') ** 0.15) * \
    (dataset['pH in loco'].astype('float32') ** 0.12) * \
    (dataset['Demanda Bioquimica de Oxigenio'].astype('float32') ** 0.1) * \
    ((dataset['Nitrogenio amoniacal total'].astype('float32') + dataset['Nitrogenio organico'].astype('float32')) ** 0.1) * \
    (dataset['Fosforo total'].astype('float32') ** 0.1) * \
    (dataset['Temperatura da agua'].astype('float32') ** 0.1) * \
    (dataset['Turbidez'].astype('float32') ** 0.08) * \
    (dataset['Solidos totais'].astype('float32') ** 0.08)

# remove valores not a number
dataset = dataset[dataset['IQA'].notna()]

estacoes = {}

estacoes[5] = ['''19d56'23.8"S''', '''44d0.4'00.4"W''']
estacoes[10] = ['''19d55'46.1"S''', '''44d4'43.9"W''']
estacoes[20] = ['''19d55'48"S''', '''44d3'33.9"W''']
estacoes[30] = ['''19d54'53.1"S''', '''44d3'15.0"W''']
estacoes[37] = ['''19d53'17.9"S''', '''44d02'15.4"W''']
estacoes[40] = ['''19d52'15"S''', '''44d3'6.1"W''']
estacoes[45] = ['''19d52'13.3"S''', '''44d2'4.4"W''']
estacoes[55] = ['''19d52'34.2"S''', '''44d3'5.9"W''']
estacoes[60] = ['''19d52'50.4"S''', '''44d2'39.5"W''']
estacoes[65] = ['''19d52'57.3"S''', '''44d2'23.5"W''']
estacoes[70] = ['''19d52'43.1"S''', '''44d2'7"W''']
estacoes[75] = ['''19d52'30.3"S''', '''44d1'9.6"W''']
estacoes[80] = ['''19d52'25.7"S''', '''44d0'54.1"W''']
estacoes[85] = ['''19d53'26.2"S''', '''44d0'22.8"W''']
estacoes[90] = ['''19d53'25.3"S''', '''44d0'16.4"W''']
estacoes[105] = ['''19d52'10.8"S''', '''43d59'53.7"W''']
estacoes[110] = ['''19d51'39.6"S''', '''43d59'49.8"W''']
estacoes[115] = ['''19d51'39.6"S''', '''43d59'49.8"W''']
estacoes[125] = ['''19d50'33"S''', '''44d02'66"W''']
estacoes[130] = ['''19d50'52.3"S''', '''44d2'21"W''']
estacoes[135] = ['''19d51'2.9"S''', '''44d1'56.1"W''']
estacoes[140] = ['''19d50'16.7"S''', '''44d1'36.4"W''']
estacoes[145] = ['''19d50'44.8"S''', '''44d1'17.2"W''']
estacoes[150] = ['''19d51'39.3"S''', '''44d2'14.2"W''']
estacoes[155] = ['''19d51'21.8"S''', '''44d1'25.2"W''']
estacoes[160] = ['''19d51'14.5"S''', '''44d0'47.8"W''']
estacoes[165] = ['''19d51'24.8"S''', '''44d0'38.9"W''']
estacoes[167] = ['''19d51'15.45"S''', '''44d00'19.86"W''']
estacoes[175] = ['''19d51'02.9"S''', '''44d00'18.3"W''']
estacoes[180] = ['''19d50'26.7"S''', '''44d00'04.3"W''']
estacoes[185] = ['''19d49'44.3"S''', '''44d0'16.4"W''']
estacoes[190] = ['''19d50'15.2"S''', '''43d59'40.2"W''']
estacoes[200] = ['''19d53'25.3"S''', '''43d58'58.5"W''']
estacoes[205] = ['''19d53'04.8"S''', '''43d58'35.8"W''']
estacoes[210] = ['''19d51'47.9"S''', '''43d58'34.1"W''']
estacoes[220] = ['''19d50'39"S''', '''43d57'44"W''']
estacoes[230] = ['''19d50'45.08"S''', '''43d59'29.13"W''']
estacoes[235] = ['''19d51'21.25"S''', '''43d58'43.35"W''']
estacoes[240] = ['''19d50'44.97"S''', '''43d58'07.32"W''']

dataset['latitude'] = ''
dataset['longetude'] = ''

for index, row in dataset.iterrows():
    if row['Estacao'] in estacoes:
        deg, minutes, seconds, direction = re.split(
            '[d\'"]', estacoes[row['Estacao']][0])
        dataset.at[index, 'latitude'] = (
            (float(deg) + float(minutes)/60 + float(seconds)/(60*60)) * (-1 if direction in ['W', 'S'] else 1))
        deg, minutes, seconds, direction = re.split(
            '[d\'"]', estacoes[row['Estacao']][1])
        dataset.at[index, 'longetude'] = (
            (float(deg) + float(minutes)/60 + float(seconds)/(60*60)) * (-1 if direction in ['W', 'S'] else 1))
    else:
        dataset.at[index, 'latitude'] = 0
        dataset.at[index, 'longetude'] = 0


newDataset = pd.DataFrame({
    'estacao': dataset['Estacao'],
    'IQA': dataset['IQA'],
    'data': dataset['Data de Amostragem'],
    'latitude': dataset['latitude'],
    'longetude': dataset['longetude']
})

# dataset = dataset.sort_values(by='Data de Amostragem')

# mean_col = dataset.groupby('Data de Amostragem')['IQA'].mean()  # don't reset the index!

newDataset.to_csv('poluition_map.csv', encoding='utf-8')
