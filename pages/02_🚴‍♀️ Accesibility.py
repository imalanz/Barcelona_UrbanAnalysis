# Mobility

import pandas as pd

import json
import geojson
import pyproj

import streamlit as st
import folium
from streamlit_folium import st_folium

import plotly.express as px

import importlib
import sys 
sys.path.append("..\src")
import src_streamlit as lit
importlib.reload(lit)
from PIL import Image
import streamlit.components.v1 as components

from bs4 import BeautifulSoup 
import pandas as pd
import requests
import re
import importlib


import plotly

import folium
from folium import Choropleth, Circle, Marker, Icon, Map, DivIcon, LinearColormap
from folium.plugins import HeatMap, MarkerCluster
from shapely.geometry import Polygon

from folium import Figure
import geopandas as gpd
import json
import geojson
import pyproj
import folium
from streamlit_folium import st_folium, folium_static

import plotly.express as px

from shapely.ops import transform
from shapely.geometry import Polygon
import streamlit.components.v1 as components

st.title("""Accesibility""")

image = Image.open('images/Giant_cityhybrid.jpg')
st.image(image)

st.write("##")

st.markdown('''In this analysis, the focus is on accessibility as a key infrastructure element in a city. A well-planned and connected 
urban environment is crucial for facilitating pedestrian movement. The analysis includes data on the locations of bicing ports, bicing 
parking spots, as well as bus and metro stations throughout the city. This information provides insights into the accessibility and 
connectivity of the city, which are essential factors for a well-functioning urban environment.
        ''')

st.write("##")

# select box for barri
options_barri = ['el Poble-sec', 'Vallvidrera, el Tibidabo i les Planes', 'el Parc i la Llacuna del Poblenou', 'la Clota', 'el Baix Guinardó', 
                 'el Fort Pienc', 'Ciutat Meridiana', 'la Trinitat Nova', 'el Poble Sec', 'el Barri Gòtic', 'Baró de Viver', 
                 "el Camp de l'Arpa del Clot", 'la Sagrera', 'la Marina del Prat Vermell', 'la Verneda i la Pau', 'la Marina de Port', 
                 'Verdun', 'les Roquetes', 'Vallbona', 'la Guineueta', 'Provençals del Poblenou', 'Montbau', 'la Vila de Gràcia', 'Sant Andreu', 
                  "l'Antiga Esquerra de l'Eixample", 'la Font de la Guatlla', 'Sants', 'Torre Baró', 'la Sagrada Família', 'Navas', 
                 'la Bordeta', 'Can Baró', 'les Corts', 'la Salut', 'la Trinitat Vella', 'Porta', 'Diagonal Mar i el Front Marítim del Poblenou', 
                 'Sant Genís dels Agudells', 'Sarrià', 'Vallcarca i els Penitents', 'Sant Gervasi - la Bonanova', 'Sant Martí de Provençals', 
                 'el Guinardó', 'el Carmel', "la Vall d'Hebron", "la Font d'en Fargues", 'el Coll', 'Can Peguera', 'el Besòs i el Maresme', 
                 'Pedralbes', 'les Tres Torres', 'el Clot', "la Nova Esquerra de l'Eixample", 'Sant Gervasi - Galvany', 'el Poblenou', 'Sant Antoni', 
                 'la Prosperitat', 'Sants - Badal', 'Horta', 'Vilapicina i la Torre Llobeta', 'el Turó de la Peira', "el Camp d'en Grassot i Gràcia Nova", 
                 'la Teixonera', 'Sant Pere, Santa Caterina i la Ribera', 'la Barceloneta', 'la Vila Olímpica del Poblenou', 'el Putxet i el Farró', 
                 "la Dreta de l'Eixample", 'la Maternitat i Sant Ramon', 'Hostafrancs', 'el Congrés i els Indians', 'el Bon Pastor', 'el Raval', 'Canyelles']
default_options = ["option 1"]
selected_option_barri =st.selectbox("Select your barri", options_barri)

# select box for equipment.
options = ["metro", "bici_puerto", "bus", "bicing"]
default_options = ["option 1"]
selected_option =st.selectbox("What you want to look for?", options)

# show map filtered. 

def mapa_mobilidad(options_barri, options):
    # mapa general.
    figure4 = Figure(width=850, height=800)
    barna = folium.Map(location=[41.3887900, 2.1589900], zoom_start=12)
    folium.TileLayer('cartodbpositron').add_to(barna)
    figure4.add_child(barna)

    bicing = pd.read_csv("data/bicing.csv")
    for i, rows in bicing.iterrows():
        marker1 = {"location": [rows["latitud"], rows["longitud"]], "tooltip": rows["category"]}

        if options == "bicing":  
            if rows['sub_category'] == "bicing":  
                icon = folium.Icon(color="lightblue", icon="fa-thin fa-bicycle", prefix = 'fa')   
                d = folium.Marker(**marker1, icon = icon)
                d.add_to(barna)

    # data of mobility without bicing
    mov = pd.read_csv("data/mobilidad_1.csv")
    mov = mov[mov["barri"] == options_barri]

    for i, rows in mov.iterrows():
        marker = {"location": [rows["latitud"], rows["longitud"]], "tooltip": rows["category"]}

        if options == "bus":
            if rows['sub_category'] == "bus":
                icon = folium.Icon(color="cadetblue", icon="fa-thin fa-bus-simple", prefix='fa')
                hosp = folium.Marker(**marker, icon=icon)
                hosp.add_to(barna)

        elif options == "metro":
            if rows['sub_category'] == "metro":
                icon = folium.Icon(color="darkblue", icon="fa-thin fa-train-subway", prefix='fa')
                sc = folium.Marker(**marker, icon=icon)
                sc.add_to(barna)

        elif options == "bici_puerto":
            if rows['sub_category'] == "bici_puerto":
                icon = folium.Icon(color="purple", icon="fa-thin fa-circle-parking", prefix='fa')
                d = folium.Marker(**marker, icon=icon)
                d.add_to(barna)

    return barna


bicing = pd.read_csv("data/bicing.csv")
mov = pd.read_csv("data/mobilidad_1.csv")
map = mapa_mobilidad (selected_option_barri, selected_option)
st_folium(map, height=500, width=1000)

# get the filtered df.
st.caption("List of asked infraestructure")



x = lit.df_streamlit_mob (selected_option_barri, selected_option)
st.dataframe(x)

st.write("##")


# MOBILITY GRAPHS.

st.subheader("Visualization")
# get the filtered df.
st.caption("Mobility Infraestructure")
def main():       
        html_temp = "<div class='tableauPlaceholder' id='viz1678981887360' style='position: relative'><noscript><a href='#'><img alt='Mobility and Area ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;mo&#47;mobility_16789813515390&#47;Sheet11&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='mobility_16789813515390&#47;Sheet11' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;mo&#47;mobility_16789813515390&#47;Sheet11&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678981887360');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"    
        components.html(html_temp, width=700, height=550)
if __name__ == "__main__":    
    main()
st.markdown('''The graph illustrates the availability of public transportation infrastructure in terms of bicycle infrastructure, 
bicycle parking, metro stations, and bus stops. It enables a comparison of the infrastructure density in each neighborhood relative 
to its area. Based on the data, El Raval stands out as the most densely equipped neighborhood in terms of public transportation 
infrastructure.
        ''')