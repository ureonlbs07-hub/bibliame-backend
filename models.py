from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    relato: str
