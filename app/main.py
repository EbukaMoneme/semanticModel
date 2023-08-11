from fastapi import FastAPI
from app.model.model import generate_like_terms

app = FastAPI()


@app.get('/')
def home():
    return {"health_check": "OK"}


@app.get('/tokenize/{query}')
def tokenize(query: str) -> list[str]:
    tokens = generate_like_terms(query)
    return tokens
