# import libraries 
import streamlit as st
import os
import requests
import json
import time

# import from within the code 
from components.landing import *
from components.audio_video import *
from params import *
from langchain.plan_b import planB

key = os.environ.get('key')
api_key = os.environ.get('TIPH_OPENAI')

cloud = 'images/cloud_sky.jpg'
water = 'images/water_zen.jpg'
stones = 'images/zen_garden.jpg'

landing_page(cloud)

# Use the values from the input page
st.write(f"Hi {st.session_state.user_name }")
#st.write(f" You said: {st.session_state.user_feeling}")
st.write(f"You chose {st.session_state.coach_name} as your motivational coach.")

#input = "I'm feeling quite anxious about this project I'm not sure how I'll finish it on time" 
# input = "I hear you're feeling a bit anxious about this project, wondering if you'll be able to finish it on time. \
#         First off, I want you to take a deep breath. Inhale confidence, exhale doubt. You've got this. \
#         See, feeling a little anxious is totally normal when you're pushing yourself to excel. It's a sign that you care \
#         deeply about your work, and that's something to be proud of. But here's the thing: anxiety only has as much power as \
#         you give it. You're in the driver's seat of your mind, my friend."

if plan == 'PlanB':
    input = planB(st.session_state.user_feeling, st.session_state.user_name)
    #input = input
    data = download_video(st.session_state.coach_name, input)
    st.write(data)
    video = data.get("result_url")
    if video: 
        st.write("downloading video ⏲️")
        time.sleep(5)
        st.video(video)
    audio = data.get("audio_url")
    if audio: 
        st.write("downloading audio ⏲️")
        time.sleep(5)
        st.audio(audio)
    st.write(f"Transcript for the hard of hearing people: \
             {input}")