from openai import OpenAI
import fitz  
import numpy as np
import os
from dotenv import load_dotenv 

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

sections = []
embeddings = []

def get_embedding(text):
    response = client.embeddings.create(input=text, model="text-embedding-3-small")
    return np.array(response.data[0].embedding)

def parse_pdf_and_embed(file_path):
    global sections, embeddings
    doc = fitz.open(file_path)

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text = page.get_text("text")

        sections.append((page_num, text))
        embeddings.append(get_embedding(text))

def return_embeddings():
    return embeddings

def return_sections():
    return sections

def generate_response(query, data):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant. Respond to the following query given the following data {data}"},
            {"role": "user", "content": query}
        ],
        max_tokens=200
    )
    return response.choices[0].message.content.strip()

parse_pdf_and_embed('company-profile.pdf')