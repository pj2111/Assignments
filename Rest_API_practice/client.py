import requests
import json

class BookAPIClient:
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
        self.api_endpoint = f"{base_url}/api/books"

    def get_all_books(self):
        """Retrieve all books from the server"""
        try:
            response = requests.get(self.api_endpoint)
            response.raise_for_status()  # response is an object # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting books: {e}")
            return None

    def get_book(self, book_id):
        """Retrieve a specific book by ID"""
        try:
            response = requests.get(f"{self.api_endpoint}/{book_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting book {book_id}: {e}")
            return None

    def add_book(self, title, author):
        """Add a new book"""
        book_data = {
            "title": title,
            "author": author
        }
        try:
            response = requests.post(
                self.api_endpoint,
                headers={"Content-Type": "application/json"},
                data=json.dumps(book_data)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error adding book: {e}")
            return None

    def update_book(self, book_id, title=None, author=None):
        """Update an existing book"""
        book_data = {}
        if title:
            book_data["title"] = title
        if author:
            book_data["author"] = author

        try:
            response = requests.put(
                f"{self.api_endpoint}/{book_id}",
                headers={"Content-Type": "application/json"},
                data=json.dumps(book_data)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating book {book_id}: {e}")
            return None

    def delete_book(self, book_id):
        """Delete a book"""
        try:
            response = requests.delete(f"{self.api_endpoint}/{book_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error deleting book {book_id}: {e}")
            return None


def main():
    # Create a client instance
    client = BookAPIClient()

    # Example usage
    print("\n1. Getting all books:")
    books = client.get_all_books()
    if books:
        print(json.dumps(books, indent=2))

    print("\n2. Adding a new book:")
    new_book = client.add_book("The Hobbit", "J.R.R. Tolkien")
    if new_book:
        print(json.dumps(new_book, indent=2))

    print("\n3. Getting a specific book:")
    book = client.get_book(1)
    if book:
        print(json.dumps(book, indent=2))

    print("\n4. Updating a book:")
    updated_book = client.update_book(1, title="Updated Title")
    if updated_book:
        print(json.dumps(updated_book, indent=2))

    print("\n5. Deleting a book:")
    result = client.delete_book(2)
    if result:
        print(json.dumps(result, indent=2))

    print("\n6. Final list of books:")
    final_books = client.get_all_books()
    if final_books:
        print(json.dumps(final_books, indent=2))


if __name__ == "__main__":
    main() 