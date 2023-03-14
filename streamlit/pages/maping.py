import folium
from folium import Choropleth, Circle, Marker, Icon, Map, DivIcon, LinearColormap
from folium.plugins import HeatMap, MarkerCluster
from shapely.geometry import Polygon

from folium import Figure
import pandas as pd
import geopandas as gpd
import json
import geojson
import pyproj

import streamlit as st
import folium
from streamlit_folium import st_folium, folium_static

import plotly.express as px

import importlib
import sys 
sys.path.append("..\src")
import streamlit as lit
importlib.reload(lit)




st.write("""
### Equipamiento

""")

options_barri = ["gotic"]
default_option_barri = ["option 1"]

x =st.selectbox("Select your Barrio", options_barri)

options = ["schools", "civic centre", "hospitals"]
default_options = ["option 1"]


selected_option =st.selectbox("Select your option", options)


figure4 = Figure(width=850,height=550)
barna = folium.Map(location=[41.3887900, 2.1589900],zoom_start=13)
folium.TileLayer('cartodbpositron').add_to(barna)
figure4.add_child(barna)
st.folium_static(barna)


map = lit.map_equipamiento (options)
st.folium_static(map)

equip = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mapping\equipamiento.csv")
map = lit.map_equipamiento (equip)
st.folium_static(map)

st.write("""
### Inserted map with HTML
""")

f=codecs.open("data/choropleth-spain.html", 'r')
mapa = f.read()

components.html(barna,height=550, scrolling=True)
    
# "blue", "darkblue", "purple", "darkpurple", "lightblue", "cadetblue", "cadetgray", "gray"
# "darkgreen", "lightgreen", green, ""
barna
    