


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


st.title("""Safety""")

image = Image.open('images/smartcity-seguridad.jpg')
st.image(image)

st.write("##")

st.markdown('''Based on the analysis of incident data from Mossos de Esquadra and Guardia Urbana, 
this information focuses on incidents in Barcelona by district. The data includes incidents that directly affected people and 
neighborhoods, as well as street incidents related to pedestrian safety. Mossos de Esquadra recorded severe incidents such as fraud, 
homicides, and squatters, while Guardia Urbana dealt with smaller incidents like neighbor disputes and vandalism in public areas. 
This analysis provides insights into the types of incidents reported and the respective roles of the two law enforcement agencies in 
addressing them. ''')


st.write("##")

# select box for barri
options_barri = ["mossos", "guardia urbana"]
default_options = ["option 1"]
selected_option_barri =st.selectbox("Select your barri", options_barri)
# get the filtered df.
st.caption("List of incidents")

x = lit.mossos (selected_option_barri)
st.dataframe(x)

st.write("##")


st.subheader("Visualization")
# get the filtered df.
st.caption("Security in the city")
def main():       
        html_temp = "<div class='tableauPlaceholder' id='viz1678991763705' style='position: relative'><noscript><a href='#'><img alt='Quantity of incidents ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;se&#47;security_16789917447820&#47;seguridad&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='security_16789917447820&#47;seguridad' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;se&#47;security_16789917447820&#47;seguridad&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678991763705');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
        components.html(html_temp, width=700, height=550)
if __name__ == "__main__":    
    main()
st.markdown('''The graph illustrates the number of incidents reported by Mossos de Esquadra, Guardia Urbana, and traffic accidents 
in each district. The data has been filtered based on the density of the area to focus on incidents that specifically impact the 
community and residents of Barcelona. This analysis provides a clearer understanding of the incident rates and distribution across 
different districts, highlighting areas with higher incident density and potential safety concerns for the local population.
        ''')