from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import YoutubeLoader
from lang.langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from lang.langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chat_message_histories import ChatMessageHistory
import os

api_key = os.environ.get("HUGO_OPENAI")
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

# 1. Load and Split PDF Pages
def load_pdf_pages(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()
    return pages

# 2. Load Texts from YouTube Videos and Split Into Chunks
def transcribe_ytvideos(youtube_url_list):
    texts = []
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=500)
    for url in youtube_url_list:
        loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
        result=loader.load()
        texts.extend(text_splitter.split_documents(result))
    return texts

# 3. Combine Texts, Split into Chunks, and Generate Embeddings
def combine_texts_pages(texts, pages):
    data = texts + pages
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=500)
    text_chunks = text_splitter.split_documents(data)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(text_chunks, embedding=embeddings)
    return vector_store

# 4. Create Retriever and Invoke
def create_and_invoke_retriever(vector_store, query):
    retriever = vector_store.as_retriever(k=4)
    docs = retriever.invoke(query)
    return docs

# 5. Setup Document Chain and Handle Query
def handle_query_with_document_chain(chat, question_answering_prompt,user_message, docs):
    document_chain = create_stuff_documents_chain(chat, question_answering_prompt)
    demo_ephemeral_chat_history = ChatMessageHistory()
    demo_ephemeral_chat_history.add_user_message(user_message)
    response = document_chain.invoke({"messages": demo_ephemeral_chat_history.messages,"context": docs})
    return response

def main(user_query):
    pdf_path = "PDF/simon-sinek-start-with-why.pdf"
    youtube_urls = ["https://www.youtube.com/watch?v=tPF5UnO1pEE", "https://www.youtube.com/watch?v=rFTwuYN9Wa8", "https://www.youtube.com/watch?v=qDhByYzAkbM", "https://www.youtube.com/watch?v=P12l9kmuTSY", "https://www.youtube.com/watch?v=XZ5NaZ2Ucdo", "https://www.youtube.com/watch?v=Tuw8hxrFBH8", "https://www.youtube.com/watch?v=fxXP2a3Mq6Y", "https://www.youtube.com/watch?v=tG98GhLmXI4", "https://www.youtube.com/watch?v=7sxpKhIbr0E", "https://www.youtube.com/watch?v=UFKCLjhO2bo", "https://www.youtube.com/watch?v=hfNOXhDpXOk", "https://www.youtube.com/watch?v=0b2MtFQk_aU", "https://www.youtube.com/watch?v=4oN5JShOs2I", "https://www.youtube.com/watch?v=0vcgxhRPdz8", "https://www.youtube.com/watch?v=_fLl9aMkdqA"]
    user_query = user_query
    #user_query = "I am feeling down, I've been having issues with my eating disorder."

    # Load and split PDF
    pages = load_pdf_pages(pdf_path)
    # Load texts from Youtube
    texts = transcribe_ytvideos(youtube_urls)
    # Prepare data and generate embeddings
    vector_store = combine_texts_pages(texts, pages)
    # Retrieve docs based on query
    docs = create_and_invoke_retriever(vector_store, user_query)

    # Setup chat model and prompt template
    chat = ChatOpenAI(api_key = api_key, model="gpt-3.5-turbo-1106", temperature=.8)
    question_answering_prompt= ChatPromptTemplate.from_messages([
        ("system", f"Answer the user's questions as if you were Tony Robbins known for inspiring people. Speak directly to the user and make sure to sound upbeat. The answer should be around 250 words."),
        MessagesPlaceholder(variable_name="messages"),
    ])
    
    # question_answering_prompt= ChatPromptTemplate.from_messages([
    #     ("system", f"Answer the user's questions based on the follwing context:{docs}. You are Toby Robbins known for inspiring people. Speak directly to them and make sure to sound upbeat. The answer should be 2 paragraphs max."),
    #     MessagesPlaceholder(variable_name="messages"),
    # ])

    # Handle query with document chain
    response = handle_query_with_document_chain(chat, question_answering_prompt, user_query, docs)
    print(response)

if __name__ == "__main__":
    main()
