
import pandas as pd


import streamlit as st
import folium
from streamlit_folium import st_folium
from folium import Figure
from PIL import Image
import streamlit.components.v1 as components



st.header("""Community engagment""")

image = Image.open('images/civic.jpg')
st.image(image)

st.write("##")

st.markdown('''Community plays a vital role in bringing a city to life by fostering connection and mutual support. In this analysis, 
I have collected data on schools, community centers, and hospitals. Schools are essential for children's education and serve as hubs for 
families and community activities. Community centers offer interactive opportunities and provide classes that benefit the local population. 
Additionally, hospitals play a crucial role in providing healthcare services and ensuring the well-being of residents. This analysis 
highlights the significance of these institutions in nurturing a thriving and supportive community within the city.
        ''')

st.write("##")

# select box for barri
options_barri = ['la Vila de Gràcia', 'el Putxet i el Farró', 'les Tres Torres', 'la Vila Olímpica del Poblenou', 'Sant Genís dels Agudells', 'el Poble-sec', 
                 'la Marina de Port', 'el Besòs i el Maresme', 'Porta', 'el Baix Guinardó', 'Can Baró', 'el Parc i la Llacuna del Poblenou', 'Montbau',
                   'el Congrés i els Indians', 'Canyelles', 'la Font de la Guatlla', 'el Guinardó', 'les Roquetes', 'la Maternitat i Sant Ramon', 'la Guineueta', 
                   'Sant Gervasi - la Bonanova', "l'Antiga Esquerra de l'Eixample", 'Vallcarca i els Penitents', 'la Bordeta', 'Vilapicina i la Torre Llobeta', 
                   'la Sagrera', "la Font d'en Fargues", "la Dreta de l'Eixample", 'el Clot', "la Vall d'Hebron", 'el Bon Pastor', "la Nova Esquerra de l'Eixample", 
                   'el Carmel', 'el Fort Pienc', 'la Verneda i la Pau', 'Sant Martí de Provençals', 'Sant Antoni', 'Provençals del Poblenou', 'Vallvidrera, el Tibidabo i les Planes', 
                   'la Marina del Prat Vermell', 'el Turó de la Peira', 'la Barceloneta', 'el Raval', 'Pedralbes', 'Ciutat Meridiana', "el Camp d'en Grassot i Gràcia Nova", 'la Salut', 
                   'la Trinitat Nova', 'Navas', 'Sant Andreu', 'Verdun', 'Torre Baró', 'el Coll', 'la Trinitat Vella', 'Sarrià', 'Hostafrancs', 'la Sagrada Família', 'Sant Gervasi - Galvany', 
                   'Sants - Badal', 'la Teixonera', 'Sant Pere, Santa Caterina i la Ribera', 'les Corts', 'la Vila de Gràcia', 'el Poblenou', 'Sants', 'Horta', 'Diagonal Mar i el Front Marítim del Poblenou', 
                   "el Camp de l'Arpa del Clot", 'el Barri Gòtic', 'la Prosperitat']
default_options = ['la Vila de Gràcia']
selected_option_barri =st.selectbox("Select your barri", options_barri)

# select box for equipment.
options = ["schools", "centro_civico", "hospitals"]
default_options = ["option 1"]
selected_option =st.selectbox("What you want to look for?", options)

# function to print equipment map
def map_equipamiento (options_barri, options):
    
    equip = pd.read_csv("csv/equipamiento_1.csv")
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

# show map filtered.
equip = pd.read_csv("csv/equipamiento_1.csv")
map = map_equipamiento (selected_option_barri, selected_option)
st_folium(map, height=500, width=1000)


# get the filtered df.
st.caption("List of asked equipment")

# function to print a db filtering what I choose in streamlit.
def df_streamlit (barri, equipamiento):
    equip = pd.read_csv("csv/equipamiento_1.csv")
    
    df = equip[["name", "category", "sub_category", "barri"]]
    df = df[(df["barri"] == barri) & (df["sub_category"] == equipamiento)]  
    return df

x = df_streamlit (selected_option_barri, selected_option)
st.dataframe(x)

st.write("##")


# visualizations

st.subheader ("Visualization")
st.caption("Community infraestructure")
# graficos soroll 
def main():
    html_temp = "<div class='tableauPlaceholder' id='viz1678985676424' style='position: relative'><noscript><a href='#'><img alt='community engagment ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;co&#47;commun&#47;comm&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='commun&#47;comm' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;co&#47;commun&#47;comm&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678985676424');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    components.html(html_temp, width=730, height=500)
if __name__ == "__main__":    
    main()
st.markdown('''The chart presents the comparison of community infrastructure in different neighborhoods based on quantity and density. 
It reveals that El Raval is the most equipped neighborhood in terms of community infrastructure, considering both the quantity and density 
of facilities. This indicates a higher concentration of schools, community centers, and hospitals in El Raval compared to other 
neighborhoods in the city.
        ''')






    
# "blue", "darkblue", "purple", "darkpurple", "lightblue", "cadetblue", "cadetgray", "gray"
# "darkgreen", "lightgreen", green, ""

    