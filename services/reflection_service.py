import os
from openai import OpenAI
from services.bible_search import search

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_reflection(text):

    verses = search(text, top_k=5)

    refs = ", ".join([v["reference"] for v in verses])

    prompt = f"""
O usuário escreveu o seguinte relato:

{text}

Versículos semanticamente relacionados encontrados:
{refs}

Escreva uma reflexão espiritual profunda baseada nesses versículos.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um guia espiritual cristão."},
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "reflection": response.choices[0].message.content,
        "verses": verses
    }