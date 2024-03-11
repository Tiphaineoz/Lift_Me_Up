#from Aitor work 

# Importing the libraries
from liftmeup_app.params import *
import os

import streamlit as st
import json
import numpy as np
import pandas as pd
from PIL import Image
import requests
import time
import base64

# Front end of the app

#This code is for the background
def get_base64(file_path):
    """Convierte un archivo a su representación en base64."""
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')
        
# few image choices 
logo = 'liftmeup_app/images/Logo_Lift_Me_Up.jpg' 
zen = 'liftmeup_app/images/zen_garden.jpg'
cloud = 'liftmeup_app/images/cloud_sky.jpg'

# to get the background of the webpage
png_file = cloud # Cambia esto por la ruta real de tu imagen
bin_str = get_base64(png_file)
page_bg_img = f'''
    <style>
    .stApp {{
    background-image: url("data:image/jpg;base64,{bin_str}");
    background-position: bottom;
    }}
    </style>
    '''
st.markdown(page_bg_img, unsafe_allow_html=True)

# splitting the top of the page into two columns for the logo on one side and title on the other 
col1, col2 = st.columns([1, 4]) 
with col1:
    #the logo side
    st.markdown(
        """
        <style>
        .rounded-image img{
            border-radius: 50%;
            overflow: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.image(logo, width=50, use_column_width=True, output_format="PNG")

with col2:
    #the title and subtitle side 
    st.markdown("""# Lift Me Up
    """)
    st.subheader('Bringing positivity to your fingertips')

#The form the user should fill in to get the motivational video
col3 = st.columns(1)
with st.form("my_form"):
   st.subheader("How are you feeling today?❤️")
   # Text input box for the user
   user_name= st.text_input("What's your name?")
   user_feeling = st.text_input("Tell me about how you feel:")
   # st.write('your prompt: ' + user_text) 
   coach_name = st.selectbox("Pick your personal motivational coach:", [" ", "Peter", "John", "Jenna", "Gon"])
   submit = st.form_submit_button('Submit')
   
def get_params():
    st.query_params.update(
        user_name=user_name,
        user_feeling=user_feeling,
        coach_name=coach_name,
        page="p2_video_url.py"
    )
    return user_name, user_feeling, coach_name, submit
    
#This is to call the video, once submitted 
if submit:
    # Set query parameters and redirect to page 2
    #get_params()
    st.query_params.update(
        user_name=user_name,
        user_feeling=user_feeling,
        coach_name=coach_name,
        page="p2_video_url.py"
    )
    switch_page("p2_video_url.py")
    