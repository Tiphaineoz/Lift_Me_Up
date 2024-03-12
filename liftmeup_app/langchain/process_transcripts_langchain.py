# code from Hugo 
from liftmeup_app.params import *

#import libraries
from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI
import os

os.environ.get("HUGO_OPENAI")
# Load the OpenAI model
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

# TIPH DRAFT: 
# from ml_logic.models import topic
# topic = 'eating_disorder'

# youtube_dict = {'eating_disorder' : [video1,video2, video3], 
#                 'depression' : [video1,video2, video3], 
#                 'anxiety' : [video1,video2, video3], 
#                 'stress' : [video1,video2, video3], 
#                 'motivation' : [video1,video2, video3]}

# motivational_agent = {'tony robbins': 'https://www.youtube.com/watch?v=O9F19ban7A4',}
# youtube_dict[topic]

#  Transcribe multiple Youtube videos
def transcribe_ytvideos(youtube_url_list):
    texts = []
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
    for url in youtube_url_list:
        loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
        result=loader.load()

        texts.extend(text_splitter.split_documents(result))
    return texts

# Summarize
def summarize_ytvideos(texts):
    chain = load_summarize_chain(llm, chain_type="map_reduce", verbose=True)
    return chain.run(texts[:])

def main():
    youtube_url_from_langchailist = ["https://www.youtube.com/watch?v=tPF5UnO1pEE", "https://www.youtube.com/watch?v=rFTwuYN9Wa8", "https://www.youtube.com/watch?v=qDhByYzAkbM", "https://www.youtube.com/watch?v=P12l9kmuTSY"]
    result = transcribe_ytvideos(youtube_url_from_langchailist)
    summary = summarize_ytvideos(result)
    print(summary)

if __name__ == "__main__":
    main()
