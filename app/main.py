from fastapi import Body, FastAPI
from pydantic import BaseModel
from app.model.model import generate_like_terms

app = FastAPI()


@app.get('/')
def home():
    return {"health_check": "OK"}


@app.post('/tokenize')
def tokenize(payload: dict) -> list[str]:
    tokens = generate_like_terms(payload['query'])
    return tokens
