# Document Summarization with Model Selection

This project is a Streamlit based application for PDF document summarization, using the OpenAI API the app generates both title suggestions and summaries for uploaded PDF files. The users can choose between `gpt-3.5-turbo` and `gpt-4` models for the summarization technique. 

## Key Features

- **Model Selection**: Choose between `gpt-3.5-turbo` and `gpt-4` models for text summarization.
- **PDF Document Embedding**: Processes and embeds PDF text content using OpenAI's `text-embedding-3-small`.
- **Structured Summarization**: Generates a JSON object containing the document's title and summary.
- **Interactive Interface**: Built with Streamlit, allowing users to upload PDF files and view results with JSON formatting.

## How It Works

1. **PDF Parsing and Embedding**: The PDF document is parsed for each page using PyMuPDF (`fitz`) embedded using OpenAI's embedding model.
2. **Summary Generation**: The content is then processed with a user selected model (`gpt-3.5-turbo` or `gpt-4`) to generate a title and summary.
3. **Output in JSON Format**: The title and summary are displayed in JSON format for structured data representation.

## Project Structure

- **`main.py`**: The main file containing the Streamlit application code.

## Setup Instructions

### Prerequisites

- Python 3.x
- Libraries: `streamlit`, `fitz` (PyMuPDF), `numpy`, `openai`, `dotenv`
- An OpenAI API Key

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AlexSteiner30/inferentia-onboard-projects.git
   cd Summarizer
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file to securely store your API key:
   ```plaintext
   OPENAI_API_KEY="your_openai_api_key"
   ```

### Running the Project

1. **Launch the Application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the Frontend**:
   Open your browser and go to `http://localhost:8501` to use the application.

## Usage

1. **Upload a PDF**: Use the file uploader to select a PDF document to summarize.
2. **Model Selection**: Choose between `gpt-3.5-turbo` and `gpt-4` from the dropdown menu.
3. **Generate Summary**: The app will parse the PDF, embed the content, and generate a title and summary.
4. **View Results**: The title, summary, and structured JSON output are displayed within the app.

## Example Output

Here’s an example of the output JSON structure generated:

```json
{
    "title": "Example Document Title",
    "summary": "This is a summarized overview of the document's content."
}
```