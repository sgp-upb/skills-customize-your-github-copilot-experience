# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework. Students will define API routes, use Pydantic models for request and response validation, and handle JSON data.

## 📝 Tasks

### 🛠️ API Setup and Routes

#### Description
Create a FastAPI application with routes to list items and retrieve a single item by ID.

#### Requirements
Completed program should:

- Initialize a `FastAPI` app instance.
- Add a `GET /items` endpoint that returns a list of items.
- Add a `GET /items/{item_id}` endpoint that returns a single item by its ID.
- Return an appropriate error if the item is not found.

### 🛠️ Pydantic Models and POST Requests

#### Description
Use a Pydantic model to define item data, and add a route to create new items.

#### Requirements
Completed program should:

- Define an `Item` model with fields for `id`, `name`, `price`, and optional `description`.
- Add a `POST /items` endpoint that accepts an `Item` payload.
- Return the newly created item in the response.

### 🛠️ Query Parameters and Filtering

#### Description
Add query parameter support to filter the item list and document how parameters work in FastAPI.

#### Requirements
Completed program should:

- Allow an optional query parameter named `q` on the `GET /items` endpoint.
- Return only items whose names contain the query text when `q` is provided.
- Keep the full item list when no query parameter is given.
