from streamlit_folium import st_folium
from folium import Choropleth, Circle, Marker, Icon, Map, DivIcon, LinearColormap
from folium.plugins import HeatMap, MarkerCluster

import folium
from folium import Figure
import pandas as pd

import streamlit as st
#import folium
#from streamlit_folium import st_folium

#import plotly.express as px



from PIL import Image
import streamlit.components.v1 as components


st.title("""Green barri""")

# image for portada
image = Image.open(r'D:\ironhack\proyectos\streamlit_Barcelona_UrbanAnalysis\images\rambla.jpg')
st.image(image)

st.write("##")

st.markdown('''The presence of green infrastructure is vital for the overall health and quality of life in every city. It contributes 
to a healthy environment and enhances the well-being of its residents. In my comprehensive analysis of the city of Barcelona, I 
meticulously gathered data on the tree distribution throughout different districts, as well as the quantification of air pollutants and 
the levels of ambient noise. These factors, in my assessment, hold utmost importance as they significantly impact the living conditions 
in each district. By prioritizing these aspects, my analysis aims to provide valuable insights into the city's green infrastructure and 
its impact on the well-being of its inhabitants.
        ''')

st.header('Urban trees')

# select box for barri
options_barri = ['la vila de gràcia', 'les tres torres', 'el camp de larpa del clot', 'el camp den grassot i gràcia nova', 
                 'horta', 'verdun', 'el besòs i el maresme', 'el congrés i els indians', 'la marina del port', 
                 'la trinitat nova', 'la marina del prat vermell', 'sant pere, santa caterina i la ribera', 
                 'les roquetes', 'el clot', 'hostafrancs', 'navas', 'el parc i la llacuna del poblenou', 
                 'la maternitat i sant ramon', 'sant gervasi - galvany', 'el turó de la peira', 
                 'diagonal mar i el front marítim del poblenou', 'la clota', 'canyelles', 'la prosperitat', 
                 'sant gervasi - la bonanova', 'montbau', 'torre baró', 'la font den fargues', 'sant andreu', 'el poblenou', 
                 'ciutat meridiana', 'les corts', 'vallbona', 'pedralbes', 'sant genís dels agudells', 'la nova esquerra de leixample', 
                 'lantiga esquerra de leixample', 'sarrià', 'la sagrera', 'sant martí de provençals', 'la salut', 'la vall dhebron', 
                 'el bon pastor', 'sants - badal', 'el coll', 'el baix guinardó', 'sant antoni', 
                 'vallvidrera, el tibidabo i les planes', 'la sagrada familia', 'provençals del poblenou', 'baró de viver', 'porta', 
                 'la guineueta', 'la trinitat vella', 'el poble sec', 'el guinardó', 'la vila olímpica del poblenou', 'el barri gòtic', 
                 'la dreta de leixample', 'la barceloneta', 'el raval', 'can peguera', 'vallcarca i els penitents', 'el fort pienc', 
                 'la bordeta', 'el carmel', 'la verneda i la pau', 'la font de la guatlla', 'el putxet i el farró', 'can baró', 
                 'sants', 'la teixonera', 'vilapicina i la torre llobeta']
default_options = ['la Vila de Gràcia']
selected_option_barri =st.selectbox("Select your barri", options_barri)


# show map filtered.

# to plot a heat map.
def heat_map(selected_option_barri):
    # csv and filter
    arbrat = pd.read_csv("D:\ironhack\proyectos\streamlit_Barcelona_UrbanAnalysis\data\\arbolado_mix_barri_barris.csv")
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

mov = pd.read_csv("D:\ironhack\proyectos\streamlit_Barcelona_UrbanAnalysis\data\\arbolado_mix_barri_barris.csv")
map = heat_map(selected_option_barri)
st_folium(map, height=500, width=1000)

# get the filtered df.
st.caption("List of your barri`s trees")

def df_arbrat (selected_option_barri):
    arbrat = pd.read_csv("D:\ironhack\proyectos\streamlit_Barcelona_UrbanAnalysis\data\\arbols.csv")
    df = arbrat[(arbrat["barri"] == selected_option_barri)]  

    return df[["taxon_name", "common_name", "address", "district", "category"]]

x = df_arbrat (selected_option_barri)
st.dataframe(x)

st.write("##")


# TREES GRAPHS.
st.subheader("Visualization")

# get the filtered df.
st.caption("Quantity of trees per barri")
# graficos arboles 
def main():
    html_temp = """<div class='tableauPlaceholder' id='viz1678977498967' style='position: relative'><noscript><a href='#'><img alt='Tree per barri ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;tr&#47;trees_16789771519730&#47;trees&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='trees_16789771519730&#47;trees' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;tr&#47;trees_16789771519730&#47;trees&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678977498967');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""    
    components.html(html_temp, width=700, height=550)
if __name__ == "__main__":    
    main()
st.markdown('''The analysis reveals that Poble Sec is the neighborhood in Barcelona with the highest number of trees. However, 
upon closer examination, it is evident that this is mainly due to the inclusion of Montjuic Park within the neighborhood's 
boundaries. Although it may seem biased, it is important to note that the presence of a park within the city has a significant 
impact on the local climate, as well as the overall quality of the surrounding areas and buildings.
        ''')
st.write("##")


# get the filtered df.
st.caption("Quantity of trees per Km2")
def main():
    html_temp = "<div class='tableauPlaceholder' id='viz1678977581751' style='position: relative'><noscript><a href='#'><img alt='Trees per area ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;tr&#47;trees_areas&#47;Sheet8&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='trees_areas&#47;Sheet8' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;tr&#47;trees_areas&#47;Sheet8&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678977581751');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    components.html(html_temp, width=700, height=550)
if __name__ == "__main__":    
    main()
st.markdown('''The graph depicts the relationship between the amount of greenery and the area size of each neighborhood. While 
Poble Sec is a large neighborhood, there are other smaller neighborhoods that have a higher density of trees per square kilometer. 
This highlights that the quantity of trees relative to the area differs among neighborhoods, indicating variations in green space 
distribution throughout the city.
        ''')
st.write("##")


# get the filtered df.
st.caption("Air contaminants per Km2")
# graficos aire
def main():
    html_temp = "<div class='tableauPlaceholder' id='viz1678978627563' style='position: relative'><noscript><a href='#'><img alt='Air contaminants ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ai&#47;air_16789770057090&#47;air&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='air_16789770057090&#47;air' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ai&#47;air_16789770057090&#47;air&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678978627563');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"    
    components.html(html_temp, width=700, height=550)
if __name__ == "__main__":    
    main()
st.markdown('''It shows how many contaminants has each barrio, for this I gather data of the contaminants, for contaminants it apears:
    NO, NO2, NOx, O3, CO that are the more common contaminants in each city.
    ''')
st.markdown('''* **Particulate Matter (PM):** Tiny particles that can be inhaled into the lungs and can cause respiratory 
    problems, cardiovascular disease, and even premature death. PM is often produced by vehicles, power plants, and industrial processes.
    ''')
st.markdown('''* **Ozone (O3):** A highly reactive gas that can cause chest pain, coughing, and shortness of breath. Ozone is produced 
    when emissions from vehicles and industrial processes react with sunlight.
    ''')
st.markdown('''* **Nitrogen Oxides (NOx):** Gases that can cause respiratory problems and contribute to the formation of ozone and PM. 
    NOx is produced by vehicle exhaust and industrial processes.
    ''')
st.markdown('''* **Carbon Monoxide (CO):** A colorless, odorless gas that can cause headaches, dizziness, and nausea, and can be deadly 
    in high concentrations. CO is produced by the incomplete burning of fossil fuels, such as in vehicle exhaust.
    ''')
st.write("##")


st.caption("Max sound per Barri")
st.markdown('''The total decibel sound and its intensity/ Energy for each dB.''')
# graficos soroll 
def main():
    html_temp = "<div class='tableauPlaceholder' id='viz1678976597862' style='position: relative'><noscript><a href='#'><img alt='Sound ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;so&#47;sonido&#47;sonido&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='sonido&#47;sonido' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;so&#47;sonido&#47;sonido&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678976597862');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>    components.html(html_temp, width=1000, height=500)"
    components.html(html_temp, width=700, height=550)
if __name__ == "__main__":    
    main()
st.markdown('''The chart presents the average sound decibel levels recorded throughout the day for each neighborhood (barri). 
It focuses on the maximum sound levels, where 20dB represents complete silence. The chart compares the total decibel sound and 
its intensity/energy for each dB, providing insights into the varying levels of sound intensity across the neighborhoods.
        ''')