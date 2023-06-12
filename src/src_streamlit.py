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
import streamlit.components.v1 as components



# COMMUNITY ENGAGMENT PAGE
# EQUIPAMIENTO 

# function to print equipment map.
def map_equipamiento (options_barri, options):
    
    equip = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mapping\equipamiento_1.csv")
    equip = equip[equip["barri"] == options_barri]
    # general map.
    figure4 = Figure(width=850,height=1800)
    barna = folium.Map(location=[41.3887900, 2.1589900],zoom_start=12)
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
                icon = folium.Icon(color="darkblue", icon = 'landmark', prefix = 'fa')
                sc = folium.Marker(**marker, icon = icon)
                sc.add_to(barna)
        
        if options == "hospitals":
            if rows['sub_category'] == "hospitals":
                icon = folium.Icon(color="lightblue", icon="fas fa-clinic-medical", prefix = 'fa')       
                d = folium.Marker(**marker, icon = icon)
                d.add_to(barna)
    
    return barna

# function to print a db filtering what I choose in streamlit.
def df_streamlit (barri, equipamiento):
    equip = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mapping\equipamiento_1.csv")
    
    df = equip[["name", "category", "sub_category", "barri"]]
    df = df[(df["barri"] == barri) & (df["sub_category"] == equipamiento)]  
    return df





# ACCESIBILITY PAGE
# mobility

# csv file
def mapa_mobilidad(options_barri, options):
    # mapa general.
    figure4 = Figure(width=850, height=800)
    barna = folium.Map(location=[41.3887900, 2.1589900], zoom_start=12)
    folium.TileLayer('cartodbpositron').add_to(barna)
    figure4.add_child(barna)

    bicing = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mobilidad\\bicing.csv")
    for i, rows in bicing.iterrows():
        marker1 = {"location": [rows["latitud"], rows["longitud"]], "tooltip": rows["category"]}

        if options == "bicing":  
            if rows['sub_category'] == "bicing":  
                icon = folium.Icon(color="lightblue", icon="fa-thin fa-bicycle", prefix = 'fa')   
                d = folium.Marker(**marker1, icon = icon)
                d.add_to(barna)

    # data of mobility without bicing
    mov = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mapping\mobilidad_1.csv")
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

# function to print a db filtering what I choose in streamlit.
def df_streamlit_mob (barri, equipamiento):
    mov = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mapping\mobilidad_1.csv")
    df = mov[["category", "sub_category", "barri"]]
    df = df[(df["barri"] == barri) & (df["sub_category"] == equipamiento)]  
    return df





# GREEN BARRIS PAGE.
# trees.

# to plot a heat map.
def heat_map(selected_option_barri):
    # csv and filter
    arbrat = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\\arbolado\\arbolado_mix_barri_barris.csv")
    arbrat = arbrat[arbrat["barri"] == selected_option_barri]
    # Mapa general.   
    figure4 = Figure(width=850,height=1800)
    barna = folium.Map(location=[41.3887900, 2.1589900],zoom_start=12)
    folium.TileLayer('cartodbpositron').add_to(barna)
    figure4.add_child(barna)

    
    for i, rows in arbrat.iterrows():
        if selected_option_barri == rows['barri']:
            marker = [[rows["latitud"], rows["longitud"]]]
            
            gradient = {0.05: "lime", 1:"green"}

            HeatMap(marker, gradient=gradient, radius=5, blur=7, min_alpha_opacity=.5).add_to(barna)

    return barna

# function to print a db filtering what I choose in streamlit.
def df_arbrat (selected_option_barri):
    arbrat = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\stramlit\\arbols.csv")
    df = arbrat[(arbrat["barri"] == selected_option_barri)]  

    return df[["taxon_name", "common_name", "address", "district", "category"]]


# download the geo json for polygon barris 
# filter all the barris and clean it 
# Open the file for reading
'''with open("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\polygon_barris_barcelona.geojson", "r") as fp:
    # Load the dictionary from the file
    barris = json.load(fp)'''

'''# map for barris
figure4 = Figure(width=850,height=550)
barna = folium.Map(location=[41.3887900, 2.1589900],zoom_start=13)

folium.TileLayer('cartodbpositron').add_to(barna)
figure4.add_child(barna)

for key, values, in barris.items():
    
    polygon_feature = {"type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": values
        }
    }
    Polygon = folium.Polygon(locations=values, popup=geo_data.keys, color='gray', fill_color='gray').add_to(barna)
    Polygon.add_to(barna)
barna
'''






# THINGS TO DO PAGE.
# ocio.

# mapping.
def mapa_ocio(selected_option_barri, selected_option):
    # mapa general.
    figure4 = Figure(width=850,height=1800)
    barna = folium.Map(location=[41.3887900, 2.1589900],zoom_start=12)
    folium.TileLayer('cartodbpositron').add_to(barna)
    figure4.add_child(barna)

    oc = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mapping\ocio_1.csv")
    oc = oc[oc["barri"] == selected_option_barri]

    for i, rows in oc.iterrows():
        marker = {"location": [rows["latitud"], rows["longitud"]], "tooltip": rows["name"]}

        if selected_option == "restaurants":
            if rows['sub_category'] == "restaurants":
                icon = folium.Icon(color="cadetblue", icon="fa-thin fa-utensils", prefix = 'fa')
                hosp = folium.Marker(**marker, icon = icon)
                hosp.add_to(barna)

        if selected_option == "drinks":
            if rows['sub_category'] == "drinks":
                icon = folium.Icon(color="darkblue", icon = "fa-thin fa-martini-glass-citrus", prefix = 'fa', )
                sc = folium.Marker(**marker, icon = icon)
                sc.add_to(barna)

        if selected_option == "museos":
            if rows['sub_category'] == "museos":
                icon = folium.Icon(color="lightblue", icon="fa-thin fa-building-columns", prefix = 'fa')
                d = folium.Marker(**marker, icon = icon)
                d.add_to(barna)    

        if selected_option == "cines":
            if rows['sub_category'] == "cines":
                icon = folium.Icon(color="purple", icon="fa-thin fa-video", prefix = 'fa')         
                d = folium.Marker(**marker, icon = icon)
                d.add_to(barna)  

    return barna

# function to print a db filtering what I choose in streamlit.
def df_ocio (selected_option_barri, selected_option):
    oc = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\mapping\ocio_1.csv")
    df = oc[(oc["barri"] == selected_option_barri) & (oc["sub_category"] == selected_option)]  
    df = oc[["category", "sub_category", "barri"]]
    return df



# SECURITY

# function to print a db filtering what I choose in streamlit.
def mossos (selected_option_barri):
    equip = pd.read_csv("D:\ironhack\proyectos\Barcelona_UrbanAnalysis\csv_from_python\stramlit\seguridad.csv")
    df = equip[(equip["personal"] == selected_option_barri)]
    
    return df

