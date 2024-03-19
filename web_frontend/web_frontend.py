# web_frontend.py
from flask import Flask, render_template, request
import requests

# enabling logging
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

API_GATEWAY_URL = 'http://locahost:5002'

@app.route('/')
def index():
    books_response = requests.get(f"{API_GATEWAY_URL}/books")
    authors_response = requests.get(f"{API_GATEWAY_URL}/authors")

    books = books_response.json()['books']
    authors = authors_response.json()['authors']

    return render_template('index.html', books=books, authors=authors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)