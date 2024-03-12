import streamlit as st
from liftmeup_app.langchain.plan_b import planB

with st.form("my_form"):
   st.subheader("How are you feeling today?❤️")
   # Text input box for the user
   user_name= st.text_input("What's your name?")
   user_feeling = st.text_input("Tell me about how you feel:")
   # st.write('your prompt: ' + user_text) 
   coach_name = st.selectbox("Pick your personal motivational coach:", [" ", "Peter", "John", "Jenna", "Gon"])
   submit = st.form_submit_button('Submit')
   
# if user_feeling:
#     st.write(planB(user_feeling))
    
st.session_state.user_name = user_name