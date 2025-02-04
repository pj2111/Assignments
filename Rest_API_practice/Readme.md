1. Summary - Defination - API, REST API, Endpoint, Flask, Flask REST API Example

2. UI based interation -
Code for app.py - how to use flask to create and interact with api

3. SDK based interation -
Code for client.py - how to use requests in python to interact with api

4. Look at langchain and how it interacts with sagemaker api endpoint and useage of content handler
[text](https://github.com/kyopark2014/LLM-LangChain/blob/main/langchain-sagemaker-endpoint-Q%26A.ipynb)
[text](https://python.langchain.com/docs/integrations/text_embedding/sagemaker-endpoint/)

Examples to try - User registration and login using ui and client both 
 - can you share 5 ideas to generate endpoint examples in flask

Review Software programming patterns

Docker and Kubernetes

# Flask REST API Example

## Introduction

### What is an API?
An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other. It defines the methods and data formats that applications can use to request and exchange information.

### What is a REST API?
REST (Representational State Transfer) API is an architectural style for designing networked applications. It uses HTTP requests to access and manipulate data. REST is stateless, meaning each request from client to server must contain all information needed to understand and process the request.

Key characteristics of REST APIs:
- Uses HTTP methods (GET, POST, PUT, DELETE)
- Stateless operations
- Resource-based URLs
- Data exchange typically in JSON format

### What is Flask?
Flask is a lightweight web application framework for Python. It's simple and easy to use, making it perfect for building web applications and APIs. Flask provides tools, libraries, and patterns to help build robust web applications.

### What is an Endpoint?
An endpoint is a specific URL in an API that represents a specific resource or functionality. It's the point of entry in a communication channel when two systems are interacting. For example, `/api/books` is an endpoint that handles book-related operations.

## API Implementation

This example implements a simple book management API with the following endpoints:

1. **GET /api/books**
   - Retrieves all books
   - Returns a JSON array of books

2. **GET /api/books/<book_id>**
   - Retrieves a specific book by ID
   - Returns a single book object or 404 if not found

3. **POST /api/books**
   - Creates a new book
   - Requires JSON body with 'title' and 'author'
   - Returns the created book with status 201

4. **PUT /api/books/<book_id>**
   - Updates an existing book
   - Requires JSON body with 'title' and/or 'author'
   - Returns the updated book or 404 if not found

5. **DELETE /api/books/<book_id>**
   - Deletes a book by ID
   - Returns success message or 404 if not found

## Setup and Installation

1. Install Flask:



