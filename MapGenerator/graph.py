import pandas as pd
import plotly.express as px

df = pd.read_csv('dataset.csv', sep=';')

# fig = px.line(df, x='Data', y='Oxigenio dissolvido',
#               title='Apple Share Prices over time (2014)')

# fig = px.line(df, x='Data', y='pH',
#               title='Ph')

# fig = px.line(df, x='Data', y='Escherichia coli', title='Escherichia coli')

#fig = px.line(df, x='Data', y='Fosforo Total', title='Fosforo Total')

# fig = px.line(df, x='Data', y='Temperatura da Agua', title='Temperatura da Agua')

fig = px.line(df, x='Data', y='Turbidez',
              title='Turbidez')
fig.show()
