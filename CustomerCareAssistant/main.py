import numpy as np

from flask import Flask, render_template, request, jsonify
from scipy.spatial.distance import cdist

from chatbot import generate_response, get_embedding, return_embeddings, return_sections
from ticket import create_ticket, get_open_tickets

app = Flask(__name__)

def respond_to_query(query):
    query_embedding = get_embedding(query)
    distances = cdist([query_embedding], return_embeddings(), metric='cosine')
    closest_index = np.argmin(distances)

    print(distances[0][closest_index])

    if distances[0][closest_index] < 0.2:
        section_text = return_sections()[closest_index][1]
        return generate_response(query, section_text)
    else:
        create_ticket(query)
        return "Your query couldn't be directly adressed. A support ticket has been created, in order to put in contact with a professional."

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query_route():
    data = request.json
    query = data.get("query")
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    response = respond_to_query(query)
    return jsonify({"response": response})

@app.route('/tickets', methods=['GET'])
def tickets_route():
    open_tickets = get_open_tickets()
    return jsonify(open_tickets)

if __name__ == '__main__':
    app.run(debug=True)