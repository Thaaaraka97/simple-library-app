# api_gateway.py
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BOOK_SERVICE_URL = 'http://172.18.0.2:5000/books'
AUTHOR_SERVICE_URL = 'http://172.18.0.3:5001/authors'

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
    app.run(host='0.0.0.0', port=5002)