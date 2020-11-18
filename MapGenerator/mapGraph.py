import matplotlib.pyplot as plt
import pandas as pd
import os
from six.moves import urllib

# datasheet
dataset = pd.read_csv("poluition_map.csv", encoding='utf8',
                      delimiter=',', engine='python')

dataset.head()

pd.to_datetime(dataset['data'])

dataset.plot(kind="scatter", x="longitude", y="latitude", figsize=(10, 7)
             s=dataset["IQA"], label="IQA",
             c="IQA", cmap=plt.get_cmap("jet"),
             colorbar=False, alpha=0.4,
             )


plt.legend()

plt.show()
