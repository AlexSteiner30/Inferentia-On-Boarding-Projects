# RAG

This repository contains a simple rag powered by the OpenAI API (model `gpt-3.5-turbo` and `gpt-4`), designed to retrieve and respond to user queries accurately from up to 5 documents uploaded by the user himself.

## Key Features

- **Fast Query Responses**: Uses OpenAI's `gpt-3.5-turbo` for efficient and cost effective responses.
- **PDF Document Processing**: Embeds PDF content using the `text-embedding-3-small` model for efficient document retrieval, keeping API costs lowest possible via [OpenAI Pricing](https://openai.com/api/pricing/).
- **Streamlite Interface**: Simple user interface allowing the user to upload his own PDF.

## How It Works

1. **Embedding and Retrieval**: The assistant embeds both the PDF documents content and user query using `text-embedding-3-small`.
2. **Response**: The response is then shown in realtime on the streamlite app
3. **Reference**: The similarity between the query and the documents is the reported to the user in order to have a feedback on the liability of the data used my the model

## Project Structure

The project is divided into the following modules:

- **`rag.py`**: Handles embedding and processes for the RAG.
- **`main.py`**: The main server file, running the backend.
- **`pdf_processing.py`**: Manages PDF processing.

## Setup Instructions

### Prerequisites

- Python 3.x
- Libraries: `streamlit`, `scipy`, `fitz` (PyMuPDF), and other dependencies specified in `requirements.txt`

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AlexSteiner30/inferentia-onboard-projects.git
   cd RAG
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   In your `.env` file, set up the following:
   - `OPENAI_API_KEY`: Your OpenAI API key

   Example `.env` file:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   MONGODB_URI=your_mongodb_uri
   ```

### Running the Project

1. **Start the Backend Server**:
   ```bash
   streamlit run rag
   ```

2. **Access the Frontend**:
   Open your web browser and go to `http://localhost:8501`.

## Usage

- Use the "Upload" button to upload up to 5 PDF documents you want the assistant to search within.
- After uploading the documents, enter your query in the input box.
- The assistant will respond with the most relevant content extracted from the documents, along with a similarity score.
- You can continue querying the uploaded documents, or clear them and upload new ones as needed.