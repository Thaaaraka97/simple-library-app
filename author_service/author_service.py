# author_service.py
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
authors = [
    {'id': 1, 'name': 'Author 1'},
    {'id': 2, 'name': 'Author 2'},
    {'id': 3, 'name': 'Author 3'}
]

# Routes for the Author Service
@app.route('/authors', methods=['GET'])
def get_authors():
    return jsonify({'authors': authors})

@app.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = next((author for author in authors if author['id'] == author_id), None)
    if author:
        return jsonify(author)
    else:
        return jsonify({'error': 'Author not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)