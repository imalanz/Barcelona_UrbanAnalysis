


import pandas as pd

import streamlit as st
import folium
from streamlit_folium import st_folium
from folium import Figure

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


# mapping ocio.
def mapa_ocio(selected_option_barri, selected_option):
    # mapa general.
    figure4 = Figure(width=850,height=1800)
    barna = folium.Map(location=[41.3887900, 2.1589900],zoom_start=12)
    folium.TileLayer('cartodbpositron').add_to(barna)
    figure4.add_child(barna)

    oc = pd.read_csv("csv/ocio_1.csv")
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

# show map filtered.
oc = pd.read_csv("csv/ocio_1.csv")
map = mapa_ocio (selected_option_barri, selected_option)
st_folium(map, height=500, width=1000)


# get the filtered df.
st.caption("List of what you asked")

# function to print a db filtering what I choose in streamlit.
def df_ocio (selected_option_barri, selected_option):
    oc = pd.read_csv("csv/ocio_1.csv")
    df = oc[(oc["barri"] == selected_option_barri) & (oc["sub_category"] == selected_option)]  
    df = oc[["category", "sub_category", "barri"]]
    return df

x = df_ocio (selected_option_barri, selected_option)
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