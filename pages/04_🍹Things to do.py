


import pandas as pd
import geopandas as gpd
import json

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



st.header("""Things to do around your Barri""")

image = Image.open('images/restaurant.jpg')
st.image(image)

st.write("##")

st.markdown('''
In this comprehensive analysis, I have gathered data on the restaurants, bars, music venues, museums, and other entertainment options 
available throughout the city of Barcelona. These diverse and vibrant activities are crucial for fostering a thriving social scene and 
providing opportunities for people to engage, connect, and enjoy themselves outside of their homes and workplaces. By exploring the wide 
range of options, this analysis highlights the richness and vibrancy of Barcelona's cultural and social life.

        ''')

st.write("##")

# select box for barri
options_barri =['Sant Antoni', 'les Corts', 'Diagonal Mar i el Front Marítim del Poblenou', 'la Vila de Gràcia', "l'Antiga Esquerra de l'Eixample", 
                'la Sagrera', 'Montbau', "la Nova Esquerra de l'Eixample", "la Font d'en Fargues", 'la Trinitat Vella', 
                "el Camp d'en Grassot i Gràcia Nova", 'Canyelles', 'la Font de la Guatlla', 'Sant Martí de Provençals', 'el Clot', 
                'la Salut', 'Torre Baró', 'la Teixonera', 'la Marina de Port', 'la Marina del Prat Vermell', 
                'la Maternitat i Sant Ramon', 'Can Baró', 'la Sagrada Família', 'el Poblenou', 'el Parc i la Llacuna del Poblenou', 
                'la Vila Olímpica del Poblenou', 'el Putxet i el Farró', 'Vallvidrera, el Tibidabo i les Planes', 
                'Provençals del Poblenou', 'el Bon Pastor', "la Vall d'Hebron", 'Horta', 'Sant Gervasi - la Bonanova', 
                'el Besòs i el Maresme', 'el Guinardó', 'el Barri Gòtic', 'Pedralbes', 'el Coll', "el Camp de l'Arpa del Clot", 
                'Verdun', 'Sant Pere, Santa Caterina i la Ribera', 'Porta', 'Navas', 'la Barceloneta', "la Dreta de l'Eixample", 
                'el Poble-sec', 'les Roquetes', 'la Bordeta', 'la Trinitat Nova', 'Vilapicina i la Torre Llobeta', 'el Turó de la Peira',
                'Sant Andreu', 'el Carmel', 'el Congrés i els Indians', 'el Raval', 'les Tres Torres', 'Vallcarca i els Penitents', 
                'Sant Gervasi - Galvany', 'Sants', 'Ciutat Meridiana', 'el Baix Guinardó', 'Sant Genís dels Agudells', 'Hostafrancs', 
                'Sarrià', 'la Verneda i la Pau', 'la Guineueta', 'Sants - Badal', 'el Fort Pienc', 'la Prosperitat']
default_options = ['la Vila de Gràcia']
selected_option_barri =st.selectbox("Select your barri", options_barri)

# select box for equipment.
options = ['museos', 'drinks', 'cines', 'restaurants']
default_options = ["option 1"]
selected_option =st.selectbox("What you want to look for?", options)

# show map filtered.
oc = pd.read_csv("data/ocio_1.csv")
map = lit.mapa_ocio (selected_option_barri, selected_option)
st_folium(map, height=500, width=1000)

# get the filtered df.
st.caption("List of what you asked")

x = lit.df_ocio (selected_option_barri, selected_option)
st.dataframe(x)

st.write("##")


# graficos places and culture 
st.subheader("Visualization")
st.caption("Attractions and culture per Barri")

def main():
    html_temp = "<div class='tableauPlaceholder' id='viz1678991404497' style='position: relative'><noscript><a href='#'><img alt='ocio ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;oc&#47;ocio&#47;ocio&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ocio&#47;ocio' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;oc&#47;ocio&#47;ocio&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678991404497');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    components.html(html_temp, width=700, height=550)
if __name__ == "__main__":    
    main()
st.markdown('''The chart illustrates the density of amenities per square kilometer in each neighborhood (barri). It reveals that 
El Raval is the most densely equipped neighborhood, offering a higher concentration of amenities and activities. This includes 
attractions that appeal to both tourists and residents, which could contribute to its popularity as a tourist destination and a 
densely populated area. The abundance of amenities in El Raval provides a wide range of activities and experiences for people to enjoy.
        ''')