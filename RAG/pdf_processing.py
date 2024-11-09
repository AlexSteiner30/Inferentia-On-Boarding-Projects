import fitz

class PDFProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self):
        text = ""
        with fitz.open(self.file_path) as pdf:
            for page in pdf:
                text += page.get_text("text") + "\n"
        return text

    def create_chunks(self, text, max_length=500):
        words = text.split()
        chunks = []
        current_chunk = []
        current_length = 0
        for word in words:
            current_chunk.append(word)
            current_length += len(word) + 1
            if current_length >= max_length:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
                current_length = 0
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        return chunks