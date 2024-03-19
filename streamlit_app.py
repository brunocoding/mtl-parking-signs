from urllib import request

import geojson
import folium
import streamlit as st
from streamlit_folium import folium_static


m = folium.Map(location=[45.5517, -73.7073], zoom_start=8)

with request.urlopen('https://donnees.montreal.ca/dataset/8ac6dd33-b0d3-4eab-a334-5a6283eb7940/resource/52cecff0-2644-4258-a2d1-0c4b3b116117/download/signalisation_stationnement.geojson') as f:
    gj = geojson.loads(f.read())

popup = folium.GeoJsonPopup(
    fields=list(gj["features"][0]["properties"]),
    # aliases=["State", "% Change"],
    localize=True,
    labels=True,
    style="background-color: yellow;",
)

tooltip = folium.GeoJsonTooltip(
    fields=list(gj["features"][0]["properties"]),
    # aliases=["State:", "2015 Median Income(USD):", "Median % Change:"],
    localize=True,
    sticky=False,
    labels=True,
    style="""
        background-color: #F0EFEF;
        border: 2px solid black;
        border-radius: 3px;
        box-shadow: 3px;
    """,
    max_width=800,
)

g = folium.GeoJson(
    gj,
    style_function=lambda x: {
        "fillColor": "#A0EFEF",
        "color": "black",
        "fillOpacity": 0.5,
    },
    marker=folium.Circle(radius=4, fill_color="orange", fill_opacity=0.6, color="orange", weight=1),
    tooltip=tooltip,
    popup=popup,
).add_to(m)

# Plot!
folium_static(m, width=725)