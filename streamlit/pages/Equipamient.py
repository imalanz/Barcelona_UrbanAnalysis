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
from streamlit_folium import st_folium

import plotly.express as px

import importlib
import sys 
sys.path.append("..\src")
import src_streamlit as lit
importlib.reload(lit)




st.header("""Barcelona city equipment""")


# select box for barri
options_barri = ['Vallvidrera, el Tibidabo i les Planes', 'el Parc i la Llacuna del Poblenou', 'la Clota', 'el Baix Guinardó', 
                 'el Fort Pienc', 'Ciutat Meridiana', 'la Trinitat Nova', 'el Poble Sec', 'el Barri Gòtic', 'Baró de Viver', 
                 "el Camp de l'Arpa del Clot", 'la Sagrera', 'la Marina del Prat Vermell', 'la Verneda i la Pau', 'la Marina de Port', 
                 'Verdun', 'les Roquetes', 'Vallbona', 'la Guineueta', 'Provençals del Poblenou', 'Montbau', 'la Vila de Gràcia', 'Sant Andreu', 
                 'el Poble-sec', "l'Antiga Esquerra de l'Eixample", 'la Font de la Guatlla', 'Sants', 'Torre Baró', 'la Sagrada Família', 'Navas', 
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
options = ["schools", "centro_civico", "hospitals"]
default_options = ["option 1"]
selected_option =st.selectbox("What you want to look for?", options)

# show map filtered.
equip = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mapping\equipamiento.csv")
map = lit.map_equipamiento (selected_option_barri, selected_option)
st_folium(map, height=900, width=1800)

# get the filtered df.
st.subheader("List of asked equipment")

x = lit.df_streamlit (selected_option_barri, selected_option)
st.dataframe(x)





    
# "blue", "darkblue", "purple", "darkpurple", "lightblue", "cadetblue", "cadetgray", "gray"
# "darkgreen", "lightgreen", green, ""

    