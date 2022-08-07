from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/api")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/api/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.post("/api/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict