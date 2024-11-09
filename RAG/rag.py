from dotenv import load_dotenv
import os
import openai
from torch import cosine_similarity
import numpy as np
from pdf_processing import PDFProcessor
import torch

load_dotenv()
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

class RAGChatbot:
    def __init__(self, indexer, model):
        self.indexer = indexer
        self.model = model

    def answer_query(self, query):
        retrieved_docs = self.indexer.retrieve(query)
        context = " ".join([doc[0]["text"] for doc in retrieved_docs])
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": f"You are a helpful assistant. Use the following data to respond accurately: {context}"},
                {"role": "user", "content": query}
            ],
            max_tokens=200
        )
        answer = response.choices[0].message.content.strip()
        references = [f"{doc[0]['doc_id']} (Score: {doc[1]:.2f})" for doc in retrieved_docs]

        return answer, references


class DocumentIndexer:
    def __init__(self, documents):
        self.documents = self.process_documents(documents)

    def process_documents(self, documents):
        nodes = []
        embeddings = []
        for doc_id, text in documents.items():
            chunks = PDFProcessor("").create_chunks(text)
            for chunk in chunks:
                try:
                    embedding_response = client.embeddings.create(input=[chunk], model="text-embedding-3-small")
                    embedding = embedding_response.data[0].embedding
                    nodes.append({"text": chunk, "embedding": embedding, "doc_id": doc_id})
                    embeddings.append(embedding)
                except Exception as e:
                    print(f"Error creating embedding for chunk: {e}")
        self.nodes = nodes
        self.embeddings = np.array(embeddings)
        return nodes

    def retrieve(self, query):
        try:
            query_embedding_response = client.embeddings.create(input=[query], model="text-embedding-3-small")
            query_embedding = torch.tensor(query_embedding_response.data[0].embedding)
            
            if not isinstance(self.embeddings, torch.Tensor):
                self.embeddings = torch.tensor(self.embeddings)
   
            similarities = cosine_similarity(query_embedding.unsqueeze(0), self.embeddings).flatten()
            top_indices = similarities.argsort(descending=True)[:min(3, len(similarities))]
            
            return [(self.nodes[idx], similarities[idx].item()) for idx in top_indices]
        except Exception as e:
            print(f"Error retrieving documents: {e}")
            return []

