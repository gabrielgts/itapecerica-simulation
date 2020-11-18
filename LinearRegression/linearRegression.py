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
dataset = pd.read_csv('iqa_1.csv', encoding='utf8',
                      delimiter=',', engine='python')

dataset['data'] = pd.to_datetime(dataset['data'])

dataset['IQA'] = dataset['IQA'].values.astype(float)

reg.fit(dataset['data'].values.reshape(-1, 1), dataset['IQA'].values.reshape(-1, 1))

# Predicao com dados de teste
y_pred = reg.predict(dataset['data'].values.astype(float).reshape(-1, 1))

dataset['pred'] = y_pred

print(dataset.var(axis=1))

ax = dataset.plot(x='data', y='IQA', color='black', style='.')

dataset.plot(x='data', y='pred', color='orange', linewidth=3, ax=ax, alpha=0.5)

ax.set_title('Predicao')

ax.set_xlabel('Data')

ax.set_ylabel('IQA')

plt.show()


# df_x = dataset

# df_y = dataset['IQA']

# x_train, x_test, y_train, y_test = train_test_split(
#     df_x, df_y, test_size=0.3, random_state=4)

# reg.fit(x_train, y_train)

# print(reg.coef_)

# # predict test
# reg.predict(x_test)

# # erros
# print(np.mean((reg.predict(x_test) - y_test)**2))
