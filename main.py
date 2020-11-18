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
dataset = pd.read_csv("parametros_ssinal_trasformed.csv",
                          delimiter=';', engine='python')

colluns = [
           'Estacao',
           'Data de Amostragem',
           'Alcalinidade de bicarbonato',
           'Alcalinidade total',
           'Aluminio dissolvido',
           'Arsenio total',
           'Cadmio total',
           'Calcio total',
           'Chumbo total',
           'Cianeto Livre',
           'Cloreto total',
           'Clorofila a',
           'Cobre dissolvido',
           'Coliformes termotolerantes',
           'Coliformes totais',
           'Condicao de tempo',
           'Condutividade eletrica in loco',
           'Condutividade eletrica laboratorio',
           'Cor verdadeira',
           'Cromo total',
           'Demanda Bioquimica de Oxigenio',
           'Demanda Quimica de Oxigenio',
           'Densidade de cianobacterias',
           'Dureza de Calcio',
           'Dureza de magnesio',
           'Dureza total',
           'Ensaio ecotoxicologico',
           'Escherichia coli',
           'Estanho total',
           'Fenois totais',
           'Feoftina a',
           'Ferro dissolvido',
           'Fosforo total',
           'Magnesio total',
           'Manganes total',
           'Sinal Mercurio total',
           'Mercurio total',
           'Microcistina',
           'Niquel total',
           'Nitrato',
           'Nitrito',
           'Nitrogenio amoniacal total',
           'Nitrogenio organico',
           'oleos e graxas',
           'Oxigenio dissolvido',
           'pH in loco',
           'pH laboratorio',
           'Saxitoxina',
           'Solidos dissolvidos totais',
           'Solidos em suspensao totais',
           'Solidos sedimentaveis',
           'Solidos totais',
           'Substancias tensoativas',
           'Sulfato total',
           'Sulfeto',
           'Temperatura da agua',
           'Temperatura do ar',
           'Turbidez',
           'Vanadio total',
           'Zinco total',
           ]

dataset.head()

dataset.info()

dataset['Data de Amostragem'] = pd.to_datetime(dataset['Data de Amostragem'])

dataset = dataset.fillna(0)


dataset.to_csv('normalized_data.csv', encoding='utf-8')

dataset.astype('float32')
scaler = StandardScaler().fit(dataset)

print(dataset['Data de Amostragem'])
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# # normalizacao dos dados
# X_train = scaler.transform(X_train)
# X_test  = scaler.transform(X_test)

# Modelo inicializado 
model = Sequential()

# Camada de entrada de dados 
model.add(Dense(12, activation='relu', input_shape=(11,)))

# Camada oculta
model.add(Dense(8, activation='relu'))

# Camada de saida
model.add(Dense(1, activation='sigmoid'))

# compilacao : Optmizacao do processamento,  
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X_train, y_train,epochs=20, batch_size=1, verbose=1)
y_pred = model.predict(X_test)

print(y_pred)

print(y_test[:5])
