import geojson

import streamlit as st
import pandas as pd
import plotly.express as px

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

with open('https://donnees.montreal.ca/dataset/8ac6dd33-b0d3-4eab-a334-5a6283eb7940/resource/52cecff0-2644-4258-a2d1-0c4b3b116117/download/signalisation_stationnement.geojson') as f:
    gj = geojson.load(f)

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=800)
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        },
        {
            "sourcetype": "raster",
            "sourceattribution": "Government of Canada",
            "source": ["https://geo.weather.gc.ca/geomet/?"
                       "SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857"
                       "&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR_1KM_RDBR&TILED=true&FORMAT=image/png"],
        },
        {
            "name": "Example",
            "below": 'traces',
            "opacity": 0.6,
            "sourcetype": "geojson",
            "type": "fill",
            "color": "royalblue",
            "source": gj
        }
      ])
fig.update_mapboxes(center={"lat":45.5517,"lon":-73.7073})
fig.update_mapboxes(zoom=8)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Plot!
st.plotly_chart(fig, use_container_width=True)