import streamlit as st
import os
#from app import get_base64, get_params


st.write("This is page 2 where we'll put the video url.")

# Access query parameters
user_name = st.query_params.get("user_name")
user_feeling = st.query_params.get("user_feeling")
coach_name = st.query_params.get("coach_name")

# Use the values in the second page
st.write(f"Hi {user_name}")
st.write(f" You said: {user_feeling}")
st.write(f"You chose {coach_name} as your motivational coach.")

coach_dict = { "Peter" : { 'url' : "https://clips-presenters.d-id.com/william/qE4P1OFtWM/Lc2cQ93AYR/image.png",
                          'voice_id' : "en-US-AndrewNeural",
                            'style' : "Cheerful"},
              "John" : {}
              , 
              "Jenna", 
              "Gon"
}

input = #hugostuff

#This is the function to create the talk
def createTalk():
    url = "https://api.d-id.com/talks"
    payload = {
        "source_url": coach_dict[coach_name]['url'],
        "script": {
            "type": "text",
            "input": #hugostuff - "So I had the chance to meet with some of the kids in the program today, where are you.",
            "provider":{
                "type": "microsoft",
                "voice_id": coach_dict[coach_name]['voice_id'],
                "voice_config":{
                    "style": coach_dict[coach_name]['style'],
                }
            }
        },
        "config": {
            "fluent": "false",
            "pad_audio": "0.0",
            "stitch": True
        }
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": os.environ.get("AITOR_AUDIO")
    }
    
    response = requests.post(url, json=payload, headers=headers)
    data = json.loads(response.text)
    id_video = data.get("id")
    return id_video

#This is the function to create the get

def getTalk(id_video):
    url = "https://api.d-id.com/talks/"+id_video

    headers = {
        "accept": "application/json",
        "authorization": os.environ.get("AITOR_VIDEO")
    }
    
    response = requests.get(url, headers=headers)
    return response

#st.image("https://clips-presenters.d-id.com/william/qE4P1OFtWM/Lc2cQ93AYR/image.png", width=300)
id_test = createTalk()
#id_test = "tlk_U-ml4wN-zMsvvm1T1ff62"
st.subheader(id_test)

time.sleep(5)

video_test = getTalk(id_test)

data = json.loads(video_test.text)
# url_video = data.get("result_url") #THIS LINE IS THE ONE THAT WORKS
url_video = "https://player.vimeo.com/video/197634410?title=0&portrait=0&byline=0&autoplay=1&loop=1&transparent=1&muted=1" #THIS WORKS TOO
video_file = open(url_video, 'rb')
video_bytes = video_file.read()

st.video(url_video, format='video/mp4', start_time=0)
