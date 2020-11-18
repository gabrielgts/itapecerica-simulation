# -*- coding: utf-8 -*-
# Bibliotecas para manuseio dos dados
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# datasheet
dataset = pd.read_csv("params_graph.csv", encoding='utf8',
                      delimiter=',', engine='python')

dataset['data'] = pd.to_datetime(dataset['data'])

dataset.sort_values(by='data')

# define number of rows and columns for subplots

nrow = 3
ncol = 2

# make a list of all dataframes

df_list = [dataset['Oxigenio dissolvido'],
           dataset['Coliformes totais'],
           dataset['pH in loco'],
           dataset['Demanda Bioquimica de Oxigenio'],
           dataset['Nitrogenio amoniacal total'],
           dataset['Nitrogenio organico']]

fig, axes = plt.subplots(nrow, ncol)
# plot counter
count = 0
for r in range(nrow):
    for c in range(ncol):
        df_list[count].plot(ax=axes[r, c])
        count = +1

plt.show()