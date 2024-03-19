import geojson

import streamlit as st
import pandas as pd
import plotly.express as px

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

from urllib import request

with request.urlopen('https://donnees.montreal.ca/dataset/8ac6dd33-b0d3-4eab-a334-5a6283eb7940/resource/52cecff0-2644-4258-a2d1-0c4b3b116117/download/signalisation_stationnement.geojson') as f:
    # file = print(f.read().decode())
    gj = geojson.loads(f.read())

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=800)
fig.update_layout(
    mapbox_style="open-street-map",
    mapbox_layers=[
        {
            "name": "Example",
            "below": 'traces',
            "opacity": 0.6,
            "sourcetype": "geojson",
            "type": "circle",
            "color": "royalblue",
            "source": gj
        }
      ])
fig.update_mapboxes(center={"lat":45.5517,"lon":-73.7073})
fig.update_mapboxes(zoom=8)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Plot!
st.plotly_chart(fig, use_container_width=True)