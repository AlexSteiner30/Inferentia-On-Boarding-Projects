# Customer Care Assistant

This repository contains a simple customer care chatbot powered by the OpenAI API (model `gpt-3.5-turbo`), designed to retrieve and respond to user queries accurately by utilizing PDF document embedding.

## Key Features

- **Fast Query Responses**: Uses OpenAI's `gpt-3.5-turbo` for effiency and cost effective responses.
- **PDF Document Processing**: Embeds PDF content using the `text-embedding-3-small` model for efficient document retrieval, keeping API costs the lowest as via [OpenAI Pricing](https://openai.com/api/pricing/).
- **Ticket System**: Automatically creates support tickets based on similarity scoring between user queries and PDF content, on the MongoDB databse.

## How It Works

1. **Embedding and Retrieval**: The assistant embeds both the PDF document content and user query using `text-embedding-3-small`.
2. **Similarity Calculation**: Calculates the cosine similarity between the query embedding and PDF embeddings determines how closely related they are.
3. **Cosine Similarity Formula**:
   \[
   \text{cosine similarity} = S_{C}(A,B) := \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|} = \frac{\sum_{i=1}^{n} A_{i} B_{i}}{\sqrt{\sum_{i=1}^{n} A_{i}^{2}} \cdot \sqrt{\sum_{i=1}^{n} B_{i}^{2}}}
   \]
   - **Threshold**: If the similarity score is above 0.2 (arbitrarly threshold), a support ticket is created.
4. **Ticket Management**: The assistant records tickets in a NoSQL database (MongoDB) for flexible data storage and retrieval.

## Project Structure

The project is divided into the following modules:

- **`chatbot.py`**: Handles embedding and query processing for PDF documents.
- **`main.py`**: The main server file, running the backend.
- **`ticket.py`**: Manages ticket creation and storage in MongoDB.
- **Frontend**: Static files (JavaScript, CSS) and HTML templates for the user interface, `static` and `templates` folders.

## Setup Instructions

### Prerequisites

- Python 3.x
- Libraries: `flask`, `scipy`, `fitz` (PyMuPDF), and other dependencies specified in `requirements.txt`
- MongoDB (or MongoDB URI for cloud storage)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/customer-care-assistant.git
   cd customer-care-assistant
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   In your `.env` file, set up the following:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `MONGODB_URI`: URI for your MongoDB database

   Example `.env` file:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   MONGODB_URI=your_mongodb_uri
   ```

### Running the Project

1. **Start the Backend Server**:
   ```bash
   python main.py
   ```

2. **Access**:
   Open your web browser and go to `http://localhost:5000`.

## Usage

- Users can submit queries related to the PDF content.
- The assistant searches through PDF embeddings and provides relevant answers.
- If a query is highly relevant to the content (cosine similarity > 0.2), a support ticket is generated in MongoDB for further assistance.