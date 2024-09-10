import streamlit as st
from PIL import Image

with st.expander("Start Cemare"):
    #Start Cemare
    image = st.camera_input("Camera")

if image: 
    #Create a Pillow Image
    img = Image.open(image)
    #Conver Image into Gray Scale
    gray_img= img.convert("L")
    #Print GrayScale Image
    st.image(gray_img)