
print(os.getcwd())

from PIL import Image
import streamlit as st
import pandas as pd
import requests
import os
import sqlite3

import base64
from PIL import Image
import streamlit as st
import io


st.title("Healthy Barri")
st.subheader('a Barcelona Urban Analysis')

# image for portada

'''def file_selector(folder_path='D:/ironhack/proyectos/Barcelona_UrbanAnalysis/images/poster.png'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select an image file', filenames)
    return os.path.join(folder_path)

# Assuming your images are located in the "images" folder
image_folder = 'images'
filename = file_selector(folder_path=image_folder)
st.write('You selected `%s`' % filename)

if filename:
    image = Image.open(filename)
    st.image(image)'''


# Example with an image URL
'''image_url = "D:/ironhack/proyectos/Barcelona_UrbanAnalysis/images/poster.png"
response = requests.get(image_url)
image_bytes = io.BytesIO(response.content)
st.image(image_bytes)'''

# Example with a local image file
with open("D:/ironhack/proyectos/Barcelona_UrbanAnalysis/images/poster.png", "rb") as file:
    image_bytes = file.read()
st.image(image_bytes)



'''image = Image.open('D://ironhack//proyectos/streamlit_prueba//images//poster.png')
st.image(image)'''




st.write("##")


st.markdown('''This analysis aims to identify the best neighborhood to live in Barcelona based on several urban characteristics. 
        A good place to live should provide a tranquil environment, good conditions for health, security, and mobility, and encourage 
        outdoor activities. ''')
st.markdown('''To conduct this analysis, I obtained data from Barcelona Open Data through CSV and web scraping. I cleaned and merged 
        the data to derive meaningful insights. I focused on the ecological environment as it contributes to a healthier and happier 
        way of life. ''')


st.caption('Process')
st.markdown('''For this project, I collected data from the Barcelona Open Data platform and performed web scraping to gather additional 
information. The primary focus was on implementing an Extract, Transform, Load (ETL) process in Python. The ETL process involved 
consolidating diverse data frames into a standardized format. Subsequently, these transformed data frames were stored in a MySQL database, 
facilitating efficient querying and retrieval of desired information. The extracted data was then utilized to generate visualizations, 
enhancing comprehension and analysis.''')


st.caption('Key Findings')

st.markdown('''* **Green spaces.** Barcelona is striving to become a greener city, which is crucial for the well-being of its residents. 
            To achieve this, the city is creating more public spaces, including parks in the streets, and reducing car usage.''')



st.markdown('''* **Clean air.** Trees help filter the air, and reducing car usage can significantly reduce pollution. This is particularly 
        important in a densely populated city like Barcelona.''')



st.markdown('''* **Accesibility.** The city is encouraging walkability and connectivity through public transportation, making it more 
        enjoyable for residents to move around.''')



st.markdown('''* **Community engagement.** A strong sense of community can create a safer environment, particularly if everyone 
        knows each other. Therefore, neighborhoods with community activities and support systems are ideal.''')



st.markdown('''* **Safety.** A safe neighborhood is one where residents can interact freely without fear of violence or crime.''')



st.markdown('''* **Things to do around.** Having a range of activities, such as museums and entertainment venues, makes a neighborhood more 
        attractive and enjoyable.''')











