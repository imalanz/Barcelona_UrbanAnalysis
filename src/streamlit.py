# streamlit

from bs4 import BeautifulSoup 
import pandas as pd
import requests
import re
import importlib

import sys 
sys.path.append("..\src")
import social as soc
importlib.reload(soc)

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


# map equipamiento 

equip = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mapping\equipamiento.csv")


def map_equipamiento (selected_option):

    figure4 = Figure(width=850,height=550)
    barna = folium.Map(location=[41.3887900, 2.1589900],zoom_start=13)

    folium.TileLayer('cartodbpositron').add_to(barna)
    figure4.add_child(barna)

    for i, rows in equip.iterrows():
        for option in selected_option:

            marker = {"location": [rows["latitud"], rows["longitud"]], "tooltip": rows["name"]}

            if selected_option == "hospitals":
                icon = folium.Icon(color="cadetblue", icon="fa-thin fa-graduation-cap", prefix = 'fa')
                hosp = folium.Marker(**marker, icon = icon)
                hosp.add_to(barna)

            if selected_option == "schools":
                icon = folium.Icon(color="darkblue", icon = "fa-thin fa-building-columns", prefix = 'fa', )

                sc = folium.Marker(**marker, icon = icon)
                sc.add_to(barna)

            if selected_option == "centre_civic":
                icon = folium.Icon(color="lightblue", icon="fa-light fa-suitcase-medical", prefix = 'fa')
            
                d = folium.Marker(**marker, icon = icon)
                d.add_to(barna)
    
    return st_folium(figure4, width = 850)