# web_frontend.py
from flask import Flask, render_template, request
import requests
import os

FE_SERVICE_HOST = os.getenv('FE_SERVICE_HOST')
FE_SERVICE_PORT = os.getenv('FE_SERVICE_PORT')
API_GATEWAY_URL = f'http://{os.getenv("API_GATEWAY_HOST")}:{os.getenv("API_GATEWAY_PORT")}'

# # enabling logging
# import logging
# logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# API_GATEWAY_URL = 'http://locahost:5002'

@app.route('/')
def index():
    books_response = requests.get(f"{API_GATEWAY_URL}/books")
    authors_response = requests.get(f"{API_GATEWAY_URL}/authors")

    books = books_response.json()['books']
    authors = authors_response.json()['authors']

    return render_template('index.html', books=books, authors=authors)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5003)
    app.run(host=FE_SERVICE_HOST, port=FE_SERVICE_PORT)