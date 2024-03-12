# Importing the libraries
import os
import streamlit as st
import numpy as np
import pandas as pd

# import from within the code
from components.landing import *
import subprocess

subprocess.run(['pip', 'install', '.'])
        
# few image choices 
logo = 'images/Logo_Lift_Me_Up.jpg' 
zen = 'images/zen_garden.jpg'
cloud = 'images/cloud_sky.jpg'


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
    