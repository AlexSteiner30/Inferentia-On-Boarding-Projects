from pymongo import MongoClient
from datetime import datetime

import os
from dotenv import load_dotenv 

load_dotenv()
client = MongoClient(os.getenv('MONGODB_URI'))

db = client.customer_support
tickets = db.tickets

def create_ticket(query):
    ticket = {
        "query": query,
        "timestamp": datetime.now(),
        "status": "open"
    }
    tickets.insert_one(ticket)
    print(f"Ticket created: {query}")

def get_open_tickets():
    open_tickets = list(tickets.find({"status": "open"}))
    return [{"id": str(ticket["_id"]), "query": ticket["query"], "timestamp": ticket["timestamp"].isoformat()} for ticket in open_tickets]