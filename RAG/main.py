import streamlit as st
from rag import DocumentIndexer, RAGChatbot
from pdf_processing import PDFProcessor

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("RAG Chatbot")
st.markdown("Ask questions based on the content of the uploaded documents.")

uploaded_files = st.file_uploader("Upload up to 5 PDF documents", type="pdf", accept_multiple_files=True)

if uploaded_files:
    document_chunks = {}
    
    for i, uploaded_file in enumerate(uploaded_files[:5]):
        file_name = f"uploaded_document_{i + 1}.pdf"
        with open(file_name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        processor = PDFProcessor(file_name)
        document_text = processor.extract_text()
        document_chunks[f"Document {i + 1}"] = document_text

    st.sidebar.title("Settings")
    model_choice = st.sidebar.selectbox("Choose the chatbot model:", ["gpt-3.5-turbo", "gpt-4"])
    indexer = DocumentIndexer(document_chunks)
    chatbot = RAGChatbot(indexer, model_choice)
    
    st.success("Documents uploaded and processed successfully!")

    query = st.text_input("Enter your question:")

    if query:
        with st.spinner("Generating answer..."):
            answer, references = chatbot.answer_query(query)
        st.markdown("### Answer")
        st.write(answer)

        st.markdown("### References")
        for ref in references:
            st.write(ref)
else:
    st.info("Please upload up to 5 PDF documents to start.")

st.sidebar.title("Information")
st.sidebar.markdown("📄 Upload up to 5 PDF documents and ask questions on them.")