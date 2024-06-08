from enum import Enum
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/')
async def index():
    return {'message': 'Welcome to news app!'}

