from fastapi import FastAPI
from pydantic import BaseModel
from services.reflection_service import generate_reflection

app = FastAPI()


class ReflectionRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"status": "Bibliame API online"}


@app.post("/reflection")
def reflection(req: ReflectionRequest):
    result = generate_reflection(req.text)
    return result

