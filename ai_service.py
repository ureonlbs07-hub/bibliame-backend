import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def consultar_ia(relato: str):

    prompt = f"""
Um usuário descreveu uma situação da vida.

Analise a situação e retorne:

1) Uma reflexão acolhedora baseada em princípios bíblicos
2) 3 versículos que podem ajudar

Responda em JSON no formato:

{{
  "analysis": "texto",
  "verses": [
    {{ "book": "Provérbios", "chapter": 3, "verse": 5 }},
    {{ "book": "Salmos", "chapter": 37, "verse": 5 }},
    {{ "book": "Tiago", "chapter": 1, "verse": 5 }}
  ]
}}

Situação do usuário:
{relato}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
