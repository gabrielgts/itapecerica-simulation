# Bibliotecas para manuseio dos dados
import pandas as pd
import numpy as np
import re

# datasheet
dataset = pd.read_csv("estacao-240.csv", encoding='utf8',
                      delimiter=',', engine='python')

print(dataset.head())
test = dataset.groupby("data").mean()
print(test)
