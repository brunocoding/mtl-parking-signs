import datetime
import locale

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit.components.v1 import html

st.title('Panneaux de stationnement MTL / MTL parking signs')

# Todo auto update deployment_date
locale.setlocale(locale.LC_TIME, 'en_CA')
deployment_date = datetime.datetime.strptime('19/03/24 20:43', '%d/%m/%y %H:%M')
stringfied_date_day = datetime.datetime.strftime(deployment_date, "%d-%b-%Y")
stringfied_date_hr = datetime.datetime.strftime(deployment_date, "%H:%M")

locale.setlocale(locale.LC_TIME, 'fr_CA') # this sets the date time formats to es_ES, there are many other options for currency, numbers etc. 
stringfied_date_day_fr = datetime.datetime.strftime(deployment_date, "%d-%B-%Y")
stringfied_date_hr_fr = datetime.datetime.strftime(deployment_date, "%H:%M")

st.text(f'Mise à jour le {stringfied_date_day_fr} à {stringfied_date_hr_fr} / Updated on {stringfied_date_day} at {stringfied_date_hr}')
button = """
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" BG_COLOR="#000000" data-name="bmc-button" data-slug="bcarvalho" data-color="#FFDD00" data-emoji="" data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
"""
html(button, height=70, width=220)
st.markdown(
    """
    <style>
        iframe[width="220"] {
            position: fixed;
            bottom: 60px;
            right: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
mtl_parking_signs = pd.read_csv("data/signalisation_stationnement.csv")
fig = px.scatter_mapbox(mtl_parking_signs, lat="Latitude", lon="Longitude", hover_name="Quartier", hover_data={'Latitude':False, 'Longitude':False, 'Description':True, 'Depuis/Since': True},
                        color_discrete_sequence=["red"], zoom=8, height=700)
fig.update_layout(
    mapbox_style="open-street-map"
)
fig.update_mapboxes(center={"lat":45.5517,"lon":-73.7073})
fig.update_mapboxes(zoom=8)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# Plot!
st.plotly_chart(fig, use_container_width=True)
st.text('Développé par / Developed by Bruno Carvalho')