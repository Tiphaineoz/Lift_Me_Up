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
#from liftmeup_app.interface.main import main
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

def landing_page(img):
    # to get the background of the webpage
    png_file = img # Cambia esto por la ruta real de tu imagen
    bin_str = get_base64(png_file)
    page_bg_img = f'''
        <style>
        .stApp {{
        background-image: url("data:image/jpg;base64,{bin_str}");
        background-position: center;
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
        st.markdown("""<h1 style='color:#02B1B6'>Lift Me Up</h1>
        """, unsafe_allow_html=True)
        st.markdown("""<h3 style='color:#FE704A'>Bringing positivity to your fingertips</h3>""", unsafe_allow_html=True)

landing_page(cloud)
#The form the user should fill in to get the motivational video
col3 = st.columns(1)
with st.form("my_form"):
   st.markdown("""<h3 style='color:#4ADED2'>How are you feeling today?❤️</h3>""", unsafe_allow_html=True)
   # Text input box for the user
   st.session_state.user_name = st.text_input("What's your name?")
   st.session_state.user_feeling = st.text_input("Tell me about how you feel:")
   # st.write('your prompt: ' + user_text) 
   st.session_state.coach_name = st.selectbox("Pick your personal motivational coach:", [" ", "Peter", "Sean", "Jenna", "Christine"])
   submit = st.form_submit_button('Submit')

# change page once submitted
def switch_page(page_name: str):
    """
    Switch page programmatically in a multipage app
    Args:
        page_name (str): Target page name
    """
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages
    pages = get_pages("pages")  # OR whatever your main page is called
    for page_hash, config in pages.items():
        if config["page_name"] == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )
    page_names = [config["page_name"] for config in pages.values()]
    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")


if submit:
    switch_page('video_url')





# def get_params():
#     st.query_params.update(
#         user_name=user_name,
#         user_feeling=user_feeling,
#         coach_name=coach_name,
#         page="p2_video_url.py"
#     )
#     return user_name, user_feeling, coach_name, submit
    
# #This is to call the video, once submitted 
# if submit:
#     # Set query parameters and redirect to page 2
#     #get_params()
#     st.query_params.update(
#         user_name=user_name,
#         user_feeling=user_feeling,
#         coach_name=coach_name,
#         page="p2_video_url.py"
#     )
#     switch_page("p2_video_url.py")
    