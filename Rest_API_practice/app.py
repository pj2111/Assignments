from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample data - in a real application, this would be a database
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"}
]

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# GET endpoint - Retrieve all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET endpoint - Retrieve a specific book by ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

# POST endpoint - Create a new book
@app.route('/api/books', methods=['POST'])
def create_book():
    if not request.json or 'title' not in request.json or 'author' not in request.json:
        return jsonify({"error": "Bad request"}), 400
    print("testing",request.json)
    new_book = {
        'id': max(book['id'] for book in books) + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# PUT endpoint - Update a book
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    if not request.json:
        return jsonify({"error": "Bad request"}), 400
    
    book['title'] = request.json.get('title', book['title'])
    book['author'] = request.json.get('author', book['author'])
    return jsonify(book)

# DELETE endpoint - Delete a book
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    books.remove(book)
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True) 