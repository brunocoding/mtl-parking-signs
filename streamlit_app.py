import streamlit as st
import pandas as pd
import plotly.express as px

mtl_parking_signs = pd.read_csv("data/signalisation_stationnement.csv")

fig = px.scatter_mapbox(mtl_parking_signs, lat="Latitude", lon="Longitude", hover_name="CODE_RPA", hover_data=["DESCRIPTION_RPA", "NOM_ARROND"],
                        color_discrete_sequence=["red"], zoom=3, height=800)
fig.update_layout(
    mapbox_style="open-street-map"
)
fig.update_mapboxes(center={"lat":45.5517,"lon":-73.7073})
fig.update_mapboxes(zoom=8)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Plot!
st.plotly_chart(fig, use_container_width=True)