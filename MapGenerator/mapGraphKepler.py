import matplotlib.pyplot as plt
import pandas as pd
import os
from six.moves import urllib

import pandas as pd  # importing the Pandas Library as 'pd'
from keplergl import KeplerGl  # importing KeplerGl
import geopandas as gpd  # importing geopandas as 'gpd'

# datasheet
dataset = pd.read_csv("poluition_map.csv", encoding='utf8',
                      delimiter=',', engine='python')

dataset.head()


#Create a basemap
map = KeplerGl(height=600, width=800)


# Create a geodataframe
gdf = gpd.GeoDataFrame(
    dataset, geometry=gpd.points_from_xy(dataset.latitude, dataset.longitude))
#make sure that your latitude and longitude are named as they are in your csv


map.add_data(data=gdf, name="IQA")  # add geoenabled dataframe to map

map.save_to_html(file_name='GeoViz.html')

map
