

import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium


from PIL import Image
import streamlit.components.v1 as components



st.title("""Conclution""")

# image for portada

image = Image.open('images/barcellona-guida-verde.jpg')
st.image(image)

st.write("##")

st.markdown('''Throughout this research, the main emphasis and personal focus were directed towards evaluating the quality of the 
    ecological environment in each neighborhood (barri). The quantity of trees, air quality, and noise pollution emerged as the most 
    impactful and valuable factors in assessing the ecological well-being of the neighborhoods. These aspects hold significant importance 
    in promoting a healthy and sustainable living environment for residents. By prioritizing these elements, the research aimed to shed light 
    on the ecological conditions and potential areas for improvement in each barri.
        ''')

st.write("##")

st.caption("Process")
st.markdown('''To determine the best barri, I conducted an extensive analysis by merging different data frames and considering various 
    investigations. The count and mean values were calculated for each investigation, and the density of each point was derived by dividing 
    it by the total area of the barrio. Applying urban criteria, I assigned values and multiplied them accordingly. Positive activities were 
    summed, while negative activities, such as security incidents or accidents, were subtracted. This comprehensive approach allowed me to 
    obtain a total result and identify the best barrio based on the count.''')

st.markdown('''To gather this wealth of information, I made use of Barcelona Open Data, leveraging various data formats such as CSV, JSON, and web scraping. 
    After cleaning and organizing the data, I was able to gain a clearer understanding and refine my analysis to achieve the desired objectives.
    ''')

st.markdown('''The porcentage by activity was for: ''')
st.markdown('''* **Trees ...................... 18%.**''')
st.markdown('''* **Accesibility ............... 18%.**''')
st.markdown('''* **Clean air .................. 16%.**''')
st.markdown('''* **Security ................... 16%.**''')
st.markdown('''* **Sound ...................... 14%.**''')
st.markdown('''* **community engagemant ....... 11%.**''')
st.markdown('''* **Things to do around ........ 7%.**''')

st.write("##")

# data frame total healthiness
st.caption("Data Frame")
x = pd.read_csv("csv/healthy_barrio.csv")
x = x[["barri_id", "distrito", "Área (km²)", "seguridad","max_sound","mobilidad","ocio","air_contam","trees","equipamiento","healthy"]]
st.dataframe(x)

st.write("##")


# healthy GRAPHS.
st.subheader("Visualization")
# total healthy 
st.caption("Best Barri")
def main():
    html_temp = "<div class='tableauPlaceholder' id='viz1678995673034' style='position: relative'><noscript><a href='#'><img alt='Healthy barri ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;he&#47;healthy_16789663938900&#47;healthy&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='healthy_16789663938900&#47;healthy' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;he&#47;healthy_16789663938900&#47;healthy&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678995673034');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    components.html(html_temp, width=700, height=500)
if __name__ == "__main__":    
    main()

st.markdown('''According to the final result, Pedralbes emerges as the healthiest barrio in Barcelona. It is closely followed by Poble 
    Sec and Sant Pere, Catalina. These three barrios stand out for their high scores in terms of health and well-being. Additionally, their 
    proximity to the outskirts of Barcelona allows for a greater presence of green areas, contributing to a healthier environment. In the 
    case of Poble Sec, the presence of Montjuic Park further enhances its environmental quality. The chart indicates a gradual decline in 
    health scores as we move away from these barrios.
        ''')

st.write("##")


# plot box compare district 
st.caption("Comparation for district.")
def main():
    html_temp = "<div class='tableauPlaceholder' id='viz1678996002615' style='position: relative'><noscript><a href='#'><img alt='Healthy district&#47;Barri ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pl&#47;plotbox_16789958010600&#47;healbox&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='plotbox_16789958010600&#47;healbox' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pl&#47;plotbox_16789958010600&#47;healbox&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1678996002615');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"    
    components.html(html_temp, width=700, height=500)
if __name__ == "__main__":    
    main()

st.markdown('''You make a valid observation. While the healthiest barrios may stand out in terms of their superior quality of living and 
    clean air, it's important to note that their positive attributes may not have a direct correlation with the overall health of neighboring 
    barrios within the same district. The differences in environmental quality and well-being can be influenced by various factors, including 
    geographical proximity, urban planning, and local infrastructure. Although the healthiest barrios may set a positive example, addressing 
    environmental concerns and improving quality of life in adjacent areas remains an important consideration for fostering a healthier and 
    more sustainable city as a whole.
        ''')

# image for portada
image = Image.open('images/1280px-Barcelona_Barris_map colors.png')
st.image(image)
st.markdown('''The map clearly shows a correlation between the best barrios and their proximity to the city's parks. This correlation 
    suggests that access to parks contributes significantly to the overall health and well-being of a barrio. While other factors could have 
    been considered and assigned different values, it is evident that Pedralbes emerges as the standout barrio in terms of its positive 
    characteristics and access to green spaces.''')

