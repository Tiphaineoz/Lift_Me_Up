
import streamlit as st
import json
import numpy as np
import pandas as pd
from PIL import Image
import requests
import time
import base64

# images list : 
logo = 'images/Logo_Lift_Me_Up.jpg' 

#This code is for the background
def get_base64(file_path):
    """Convierte un archivo a su representación en base64."""
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# This for the background of the webpage and the headers (aka logo + title & slogan)
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

# to go from one page to another
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
