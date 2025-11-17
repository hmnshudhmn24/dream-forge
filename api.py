from fastapi import FastAPI
from pydantic import BaseModel
from world_generator import generate_world
from utils import load_config

app = FastAPI(title='DREAMFORGE API')

class Request(BaseModel):
    prompt: str

@app.post('/generate')
def generate(req: Request):
    cfg = load_config()
    text = generate_world(req.prompt)
    return {'world': text}
