# Bibliotecas para manuseio dos dados
import pandas as pd
import numpy as np

# train
from sklearn.model_selection import train_test_split

# model
from sklearn import linear_model

# graph
import matplotlib.pyplot as plt

# Load linear Regression
reg = linear_model.LinearRegression()

# datasheet
dataset = pd.read_csv('params_graph.csv', encoding='utf8',
                      delimiter=',', engine='python')

dataset['data'] = pd.to_datetime(dataset['data'])

for (columnName, columnData) in dataset.iteritems():
    if (columnName == 'index' or columnName == 'data'):
        continue

    dataset = dataset[dataset[columnName].notna()]    

    dataset[columnName] = dataset[columnName].values.astype(float)

    newDataset = dataset.groupby('data')[columnName].mean()  # don't reset the index!

    newDataset.to_csv(columnName + '-mean.csv', encoding='utf-8')


    dataToRegression = pd.read_csv(columnName + '-mean.csv', encoding='utf8',
                                   delimiter=',', engine='python', names=['data', columnName])
    
    dataToRegression['data'] = pd.to_datetime(dataToRegression['data'])
    

    reg.fit(dataToRegression['data'].values.reshape(-1, 1), dataToRegression[columnName].values.reshape(-1, 1))

    # Predicao com dados de teste
    y_pred = reg.predict(dataToRegression['data'].values.astype(float).reshape(-1, 1))

    dataToRegression['pred'] = y_pred


    ax = dataToRegression.plot(x='data', y=columnName, color='black', style='.')

    dataToRegression.plot(x='data', y='pred', color='orange', linewidth=3, ax=ax, alpha=0.5)

    ax.set_title('Predicao')

    ax.set_xlabel('Data')

    ax.set_ylabel(columnName)

    plt.savefig('linear-regression-params{}.png' .format(columnName))
