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
from langchain.label_predict import predict_label
from langchain.query_doc_chain import *

key = os.environ.get('key')
api_key = os.environ.get('TIPH_OPENAI')

cloud = 'images/cloud_sky.jpg'
water = 'images/water_zen.jpg'
clear = 'images/beige.jpg'

landing_page(clear)

# Use the values from the input page
st.write(f"Hi {st.session_state.user_name}")
st.write("Nice to see you today ☀️ Let's get started.")
st.write(f" If I understand correctly your preocupation today is about: ...")
time.sleep(5)
st.write(f"{predict_label(st.session_state.user_feeling)}")
time.sleep(5)
# st.write(f" You said: {st.session_state.user_feeling}")
st.write(f"You chose {st.session_state.coach_name} as your motivational coach.")

# input = "I'm feeling quite anxious about this project I'm not sure how I'll finish it on time" 
# input = "I hear you're feeling a bit anxious about this project, wondering if you'll be able to finish it on time. \
#         First off, I want you to take a deep breath. Inhale confidence, exhale doubt. You've got this. \
#         See, feeling a little anxious is totally normal when you're pushing yourself to excel. It's a sign that you care \
#         deeply about your work, and that's something to be proud of. But here's the thing: anxiety only has as much power as \
#         you give it. You're in the driver's seat of your mind, my friend."

time.sleep(5)
    
if plan == 'PlanA':
    st.write(f" If I understand correctly your preocupation today is about: ...")
    time.sleep(5)
    st.write(f"{predict_label(st.session_state.user_feeling)}")
    time.sleep(5)
    st.write(f"Let me get you {st.session_state.coach_name} whom I'll train to help with this matter")
    time.sleep(5)
    #add all the code from Hugo
    input = main(st.session_state.user_feeling)
    st.write(f"Here is the input for the video: {input}")
    #so it gives us an input to use for the audio & video
    #input = "god knows what"
    #input = input
   
    
if plan == 'PlanB':
    input = planB(st.session_state.user_feeling, st.session_state.user_name)
    #input = input
    
# connecting the API to our output
# the workflow that works for sure!
# -----------------------------
# response, video_id = createTalk(st.session_state.coach_name, input)
# st.write(f"{st.session_state.coach_name} will be with you shortly... ") # just to check it runs ok : (" response: {response} video_id : {video_id}")
# time.sleep(40)
# video_test = getTalk(video_id)
# st.write(f"got the talk ? {video_test}") # just to check it runs ok
# st.write(f" type : {type(video_test)}") # just to check it runs ok
# time.sleep(20)
# data = json.loads(video_test.text)
# st.write(f"got the json ? {data}") # just to check it runs ok


# video = data.get("result_url")
# if video: 
#     st.write("⏲️")
#     time.sleep(5)
#     st.video(video)
# else : 
    # audio = data.get("audio_url")
    # if audio: 
    #     st.write("getting the audio ⏲️")
    #     time.sleep(5)
    #     st.audio(audio)
# st.write(f"-- For the hard of hearing audience --")
# st.write(f"Here is the transcript:")
# st.write(f"{input}")
# -----------------------------


# st.write("test built in function")
# data = download_video(st.session_state.coach_name, input)
# st.write(f" result download video function {data}")
# st.write(data)
# video = data.get("result_url")
# if video: 
#     st.write("downloading video ⏲️")
#     time.sleep(5)
#     st.video(video)
# audio = data.get("audio_url")
# if audio: 
#     st.write("downloading audio ⏲️")
#     time.sleep(5)
#     st.audio(audio)
# st.write(f"-- For the hard of hearing audience --")
# st.write(f"Here is the transcript:")
# st.write(f"{input}")


# ------ plan C faking the results ------
if plan == "PlanC":
    st.write(f"Your coach will be with you shortly... ")
    time.sleep(40)
    audio_url = "https://d-id-talks-prod.s3.us-west-2.amazonaws.com/auth0%7C65f0a6a03606a9a45e89a9fe/tlk_MW192Q_ICbdtUhu0ztZdh/microsoft.wav?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1710409897&Signature=hsesGmSkgSEbdtZq0%2F9%2FOBSfylM%3D"
    st.audio(audio_url, format='audio/wav', start_time=0)

    st.write(f"-- For the hard of hearing audience --")
    st.write(f"Here is the transcript:")
    st.write("Hey Tiph! I've heard that you're feeling anxious about this project, but let me tell you something - you've got this!)
    st.write("First of all, take a deep breath and remind yourself of all the amazing things you've accomplished in the past. You're capable of so much, and this project is no different. ")
    st.write("I know it's tough, but remember that anxiety only has as much power as you give it. You're in control, and you're going to do great. ")