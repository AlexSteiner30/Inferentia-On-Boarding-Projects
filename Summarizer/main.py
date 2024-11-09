import streamlit as st
from openai import OpenAI
import fitz  
import numpy as np
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

sections = []
embeddings = []

def get_embedding(text):
    response = client.embeddings.create(input=text, model="text-embedding-3-small")
    return np.array(response.data[0].embedding)

def parse_pdf_and_embed(file):
    global sections, embeddings
    sections.clear()
    embeddings.clear()
    
    doc = fitz.open(stream=file.read(), filetype="pdf")
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text = page.get_text("text")
        sections.append((page_num, text))
        embeddings.append(get_embedding(text))

def generate_response(data, model_name):
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": f"You are a helpful assistant. Given the document content, create a complete summary in JSON format with a title and summary. {data[:16000]}."},
            {"role": "user", "content": data}
        ],
        max_tokens=200
    )
    return json.loads(response.choices[0].message.content.strip())

st.title("Document Summarization")
st.set_page_config(page_title="Document Summarization", page_icon="📄")
st.write("Upload a document to receive title suggestion and content summarization.")

model_name = st.selectbox(
    "Select the model used for summarization:",
    ["gpt-3.5-turbo", "gpt-4"]
)

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    parse_pdf_and_embed(uploaded_file)
    
    document_content = " ".join([text for _, text in sections])

    result = generate_response(document_content, model_name) 
    
    st.subheader("Generated Title")
    st.write(result["title"])

    st.subheader("Summarization")
    st.write(result["summary"])

    st.subheader("Structured JSON Output")
    st.json(result)