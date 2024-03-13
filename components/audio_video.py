import streamlit as st
import os
import requests
import json
import time

key = os.environ.get('key')

# list of coach options
coach_dict = { "Peter" : { 'url' : "https://clips-presenters.d-id.com/darren/RYscOXmp8t/CtDjn3POSq/image.png",
                          'voice_id' : "en-US-AndrewNeural",
                            'style' : "Cheerful"},
              "Sean" : {'url' : "https://clips-presenters.d-id.com/william/FPvBkeR0kv/bAIOAUOG33/image.png",
                          'voice_id' : "en-US-JasonNeural",
                            'style' : "Hopeful"},
              "Jenna": {'url' : "https://clips-presenters.d-id.com/amy/sEIU0O2gBy/VrHMAOUSgO/image.png",
                          'voice_id' : "en-US-JennyNeural",
                            'style' : "Hopeful"},
              "Christine": {'url' : "https://clips-presenters.d-id.com/alyssa/Kpjhh2J_rm/Oa9TBDfWdE/image.png",
                          'voice_id' : "en-US-NancyNeural",
                            'style' : "Hopeful"}
}

# This is the function to create the talk
def createTalk(coach_name, input):
    url = "https://api.d-id.com/talks"
    
    source_url = coach_dict[coach_name]['url']
    voice_id = coach_dict[coach_name]['voice_id']
    style = coach_dict[coach_name]['style']
    
    payload = {
        "source_url": source_url,
        "script": {
            "type": "text",
            "input": input,
            "provider":{
                "type": "microsoft",
                "voice_id": voice_id,
                "voice_config":{
                    "style": style,
                }
            }
        },
        "config": {
            "fluent": "false",
            "pad_audio": "0.0",
            "stitch": True,
            "driver_expressions": {
                    "expressions": [
                        {
                        "start_frame": 0,
                        "expression": "happy",
                        "intensity": 1
                        }]
            },
        }
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": key
    }
    
    
    response = requests.post(url, json=payload, headers=headers)
    data = json.loads(response.text)
    id_video = data.get("id")
    return response, id_video

# This is the function to get the video
def getTalk(id_video):
    url = "https://api.d-id.com/talks/"+str(id_video)    

    headers = {
        "accept": "application/json",
        "authorization": key
    }
    
    response = requests.get(url, headers=headers)
    return response

# this is the combine function to run both of the above and get the result (audio + video)
def download_video(coach_name, input):
    response, id_video = createTalk(coach_name, input)
    time.sleep(20)
    video_test = getTalk(id_video)
    st.write(f"got the talk ? {video_test}")
    st.write(type(video_test))
    time.sleep(20)
    data = json.loads(video_test.text)
    return data


# ----------------------- MANUAL TESTING -----------------------
# st.write(f"input ☑️ {input}")
# st.write("downloading video ☑️")
# video_url = download_video(st.session_state.coach_name, input)
# st.video(video_url)

# st.write(f"input ?:  {input}")
# key, response, id_video, source_url, voice_id, style = createTalk(st.session_state.coach_name, input)
# st.write(f"creating talk ? {key, response, id_video, source_url, voice_id, style}")
# time.sleep(5)
# st.write("sleep ☑️")
# video_test = getTalk(id_video)
# st.write(f"got the talk ? {video_test}")
# data = json.loads(video_test.text)
# st.write(f"got the json ? {data}")
# url_video = data.get("result_url")
# st.write(f"got the url video ? {url_video}")
#st.video(str(url_video))

# video_url = "https://d-id-talks-prod.s3.us-west-2.amazonaws.com/google-oauth2%7C109918195984028087127/tlk_FEh7nIgLTQD3PSnKXQ_to/1710238395727.mp4?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1710324799&Signature=kPI7RTV9vNF4PhQdfUDoNcYxB4w%3D"
# st.video(video_url)
# json_example = {"user": {"features": ["stitch", "clips", None], "stripe_plan_group": "deid-trial", "authorizer": "basic", "owner_id": "google-oauth2|109918195984028087127", "id": "google-oauth2|109918195984028087127", "plan": "deid-trial", "email": "tiphaine.ollivier1@gmail.com"}, "script": {"length": 239, "subtitles": False, "type": "text", "provider": {"type": "microsoft", "voice_id": "en-US-NancyNeural", "voice_config": {"style": "Hopeful"}}}, "audio_url": "https://d-id-talks-prod.s3.us-west-2.amazonaws.com/google-oauth2%7C109918195984028087127/tlk_42yqgHtRslgFAelaX83_U/microsoft.wav?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1710327987&Signature=Cym5ZPytbJBNPkC5l%2F0rxJFuTtg%3D", "created_at": "2024-03-12T11:06:27.652Z", "config": {"stitch": True, "align_driver": True, "sharpen": True, "normalization_factor": 1, "result_format": ".mp4", "fluent": False, "driver_expressions": {"expressions": [{"intensity": 1, "start_frame": 0, "expression": "happy"}], "transition_frames": 50}, "pad_audio": 0, "reduce_noise": False, "auto_match": True, "show_watermark": True, "motion_factor": 1, "align_expand_factor": 0.3}, "source_url": "https://d-id-talks-prod.s3.us-west-2.amazonaws.com/google-oauth2%7C109918195984028087127/tlk_42yqgHtRslgFAelaX83_U/source/image.png?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1710327987&Signature=0AC10YgKAIUjAYom8y6sszh8B%2B8%3D", "created_by": "google-oauth2|109918195984028087127", "status": "started", "driver_url": "bank://natural/", "modified_at": "2024-03-12T11:06:27.827Z", "user_id": "google-oauth2|109918195984028087127", "subtitles": False, "id": "tlk_42yqgHtRslgFAelaX83_U", "duration": 18, "started_at": "2024-03-12T11:06:27.720", "pending_url": "s3://d-id-talks-prod/google-oauth2|109918195984028087127/tlk_42yqgHtRslgFAelaX83_U/1710241587652.mp4"}

# audio_url2 = json_example['audio_url']
#audio_url = "https://d-id-talks-prod.s3.us-west-2.amazonaws.com/google-oauth2%7C109918195984028087127/tlk_42yqgHtRslgFAelaX83_U/microsoft.wav?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1710327987&Signature=Cym5ZPytbJBNPkC5l%2F0rxJFuTtg%3D"

#st.audio(audio_url)
# st.audio(audio_url2)