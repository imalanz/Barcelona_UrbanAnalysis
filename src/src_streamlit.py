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


# EQUIPAMIENTO 

# function to print equipment map.
def map_equipamiento (options_barri, options):
    
    equip = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mapping\equipamiento_1.csv")
    equip = equip[equip["barri"] == options_barri]
    # general map.
    figure4 = Figure(width=850,height=550)
    barna = folium.Map(location=[41.3887900, 2.1589900],zoom_start=13)
    folium.TileLayer('cartodbpositron').add_to(barna)    
    figure4.add_child(barna)
    # iterate to get each equipment in the map with different icons.
    for i, rows in equip.iterrows():
        marker = {"location": [rows["latitud"], rows["longitud"]], "tooltip": rows["name"]}

        if options == "schools":
            if rows['sub_category'] == "schools":
                icon = folium.Icon(color="cadetblue", icon="fa-thin fa-graduation-cap", prefix = 'fa')
                hosp = folium.Marker(**marker, icon = icon)
                hosp.add_to(barna)
                
                
        if options == "centro_civico":
            if rows['sub_category'] == "centro_civico":
                icon = folium.Icon(color="darkblue", icon = "fa-thin fa-building-columns", prefix = 'fa')
                sc = folium.Marker(**marker, icon = icon)
                sc.add_to(barna)
        
        if options == "hospitals":
            if rows['sub_category'] == "hospitals":
                icon = folium.Icon(color="lightblue", icon="fa-solid fa-file-medical", prefix = 'fa')       
                d = folium.Marker(**marker, icon = icon)
                d.add_to(barna)
    
    return barna

# function to print a db filtering what I choose in streamlit.
def df_streamlit (barri, equipamiento):
    equip = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mapping\equipamiento_1.csv")
    df = equip[["name", "category", "sub_category", "barri"]]
    df = df[(df["barri"] == barri) & (df["sub_category"] == equipamiento)]  
    return df



# mobility

# csv file
def mapa_mobilidad(options_barri, options):
    # mapa general.
    figure4 = Figure(width=850, height=550)
    barna = folium.Map(location=[41.3887900, 2.1589900], zoom_start=13)
    folium.TileLayer('cartodbpositron').add_to(barna)
    figure4.add_child(barna)

    # data of mobility without bicing
    mov = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mapping\mobilidad_1.csv")
    mov = mov[mov["barri"] == options_barri]

    for i, rows in mov.iterrows():
        marker = {"location": [rows["latitud"], rows["longitud"]], "tooltip": rows["category"]}

        if options == "bus":
            icon = folium.Icon(color="cadetblue", icon="fa-thin fa-bus-simple", prefix='fa')
            hosp = folium.Marker(**marker, icon=icon)
            hosp.add_to(barna)

        elif options == "metro":
            icon = folium.Icon(color="darkblue", icon="fa-thin fa-train-subway", prefix='fa')
            sc = folium.Marker(**marker, icon=icon)
            sc.add_to(barna)

        elif options == "bici_puerto":
            icon = folium.Icon(color="purple", icon="fa-thin fa-circle-parking", prefix='fa')
            d = folium.Marker(**marker, icon=icon)
            d.add_to(barna)

    return barna


bicing = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mobilidad\\bicing.csv")
    


# ocio
'''for i, rows in bicing.iterrows():
        marker1 = {"location": [rows["latitud"], rows["longitud"]], "tooltip": rows["category"]}

        if options == "bicing":    
            icon = folium.Icon(color="lightblue", icon="fa-thin fa-bicycle", prefix = 'fa')   
            d = folium.Marker(**marker1, icon = icon)
            d.add_to(barna)'''