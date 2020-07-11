# Bibliotecas para manuseio dos dados
import pandas as pd
import numpy as np

# normalizacao dos dados
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

# Modelo sequemcial (inpute de uma camada e output da outra)
from keras.models import Sequential

# Perceptron Multicamada
from keras.layers import Dense

# datasheet
dataset = np.loadtxt("dataset-without-data.csv", delimiter=';')

colluns = ['Oxigenio dissolvido',
           'Escherichia coli',
           'pH',
           'Demanda bioquimica de oxigenioDBO(5. 20)',
           'Fosforo Total',
           'Temperatura da Agua',
           'Turbidez',
           'Residuos totais',
           'Nitrogenio Amoniacal']

X = dataset[:, 0:8]
y = dataset[:, 8]

print(y)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# # normalizacao dos dados
# scaler  = StandardScaler().fit(X_train)
# X_train = scaler.transform(X_train)
# X_test  = scaler.transform(X_test)

# # Modelo inicializado 
# model = Sequential()

# # Camada de entrada de dados 
# model.add(Dense(12, activation='relu', input_shape=(11,)))

# # Camada oculta
# model.add(Dense(8, activation='relu'))

# # Camada de saida
# model.add(Dense(1, activation='sigmoid'))

# # compilacao : Optmizacao do processamento,  
# model.compile(loss='binary_crossentropy',
#               optimizer='adam',
#               metrics=['accuracy'])

# model.fit(X_train, y_train,epochs=20, batch_size=1, verbose=1)
# y_pred = model.predict(X_test)

# print(y_pred)

# print(y_test[:5])
