# api_gateway.py
from flask import Flask, jsonify, request
import requests
import os

API_SERVICE_HOST = os.getenv('API_SERVICE_HOST')
API_SERVICE_PORT = os.getenv('API_SERVICE_PORT')
BOOK_SERVICE_URL = f'http://{os.getenv("BOOK_SERVICE_HOST")}:{os.getenv("BOOK_SERVICE_PORT")}/books'
AUTHOR_SERVICE_URL = f'http://{os.getenv("AUTHOR_SERVICE_HOST")}:{os.getenv("AUTHOR_SERVICE_PORT")}/authors'


app = Flask(__name__)

# BOOK_SERVICE_URL = 'http://172.18.0.2:5000/books'
# AUTHOR_SERVICE_URL = 'http://172.18.0.3:5001/authors'

# Routes for the API Gateway
@app.route('/books', methods=['GET'])
def get_books():
    response = requests.get(BOOK_SERVICE_URL)
    return jsonify(response.json())

@app.route('/authors', methods=['GET'])
def get_authors():
    response = requests.get(AUTHOR_SERVICE_URL)
    return jsonify(response.json())

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5002)
    app.run(host=API_SERVICE_HOST, port=API_SERVICE_PORT)