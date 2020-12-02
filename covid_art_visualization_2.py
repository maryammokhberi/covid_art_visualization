# visualization using bokeh and Holoviews
#http://examples.holoviews.org/Earthquake_Visualization.html
import pandas as pd
# us_cities = pd.read_csv("https://public.opendatasoft.com/explore/dataset/covid-19-pandemic-worldwide-data/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B")
us_cities = pd.read_csv('/Users/maryam/Documents/covid and art visualization/covid-19-pandemic-worldwide-data.csv', sep=';')
import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()