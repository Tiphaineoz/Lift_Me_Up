# in case nothing works use openAI

import os
from params import *
from openai import OpenAI 

api_key = os.environ.get('api_key')

def planB(prompt, user_name):
    client = OpenAI(api_key = api_key)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0613",  # Use the engine of your choice
    messages = [{"role": "system", "content": f"You are the perfect mix between a psychologist and a motivanal speaker (like Simon SInek, Oprah or Tony Robbins) and you are giving a positive pep talk to {user_name}"},
                {"role": "user", "content": prompt}],
    max_tokens = 200
    )
    message = response.choices[0].message.content
    return message 

