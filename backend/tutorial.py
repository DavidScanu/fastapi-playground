from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Python FastAPI Tutorial: Build a REST API in 15 Minutes
# https://youtu.be/iWS9ogMPOI0?si=67SMAo5DT7XxDQTy

app = FastAPI()

class Item(BaseModel):
    text: str
    is_doner: bool = False


items = []


@app.get("/")
def read_root():
    return {"Hello": "David"}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")
