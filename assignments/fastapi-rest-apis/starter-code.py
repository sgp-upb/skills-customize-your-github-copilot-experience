from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

items = [
    {"id": 1, "name": "FastAPI Guide", "price": 0.0, "description": "A starter item."},
    {"id": 2, "name": "Demo Product", "price": 9.99, "description": "Example API item."},
]

# TODO: Add a GET /items endpoint that returns all items.

# TODO: Add optional query parameter support for `q` to filter items by name.

# TODO: Add a GET /items/{item_id} endpoint that returns an item by its ID.

# TODO: Add a POST /items endpoint that accepts an Item and returns the created item.

# Run the app with `uvicorn starter-code:app --reload` when you're ready to test.
