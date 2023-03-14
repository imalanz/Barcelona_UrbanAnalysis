import streamlit as st
from PIL import Image


st.title("Barcelona Urban Analysis")

image = Image.open('D:\ironhack\proyectos\Barcelona_UrbanAnalysis\images\poster.png')

st.image(image)

st.markdown('''Analysis of Barcelona Urban distribution, comparing 4 main characteristics: 
         - Social:
         - Equipment
         - Ecologic:
         - Mobility''')

st.subheader('Social')
st.subheader('Equipment')
st.subheader('Ecology')
st.subheader('Mobility')