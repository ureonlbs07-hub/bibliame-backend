from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.reflection_service import generate_reflection


app = FastAPI()

# habilitar CORS para permitir chamadas do Flutter Web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ReflectionRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"status": "Bibliame API online"}


@app.post("/reflection")
def reflection(req: ReflectionRequest):
    result = generate_reflection(req.text)
    return result