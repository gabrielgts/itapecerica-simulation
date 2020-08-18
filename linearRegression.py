# Bibliotecas para manuseio dos dados
import pandas as pd
import numpy as np

# train
from sklearn.model_selection import train_test_split

# model
from sklearn import linear_model

# graph
from matplotlib import pyplot as plt

# Load linear Regression
reg = linear_model.LinearRegression()

# datasheet
dataset = pd.read_csv('normalized_data_iqa.csv', encoding='utf8',
                      delimiter=',', engine='python')

df_x = dataset

df_y = dataset['IQA']

x_train, x_test, y_train, y_test = train_test_split(
    df_x, df_y, test_size=0.3, random_state=4)

reg.fit(x_train, y_train)

print(reg.coef_)

# predict test
reg.predict(x_test)

# erros
print(np.mean((reg.predict(x_test) - y_test)**2))
