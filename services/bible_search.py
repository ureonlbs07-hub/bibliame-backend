import json
import numpy as np
import os
from openai import OpenAI

client = OpenAI()

# carregar embeddings se existirem
if os.path.exists("data/bible_vectors.npy"):
    vectors = np.load("data/bible_vectors.npy")
else:
    vectors = None

# carregar referências se existirem
if os.path.exists("data/bible_refs.json"):
    with open("data/bible_refs.json") as f:
        refs = json.load(f)
else:
    refs = []

# carregar texto da bíblia
if os.path.exists("data/almeida.json"):
    with open("data/almeida.json") as f:
        bible = json.load(f)
else:
    bible = None


def embed_query(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return np.array(response.data[0].embedding)


def search(query, top_k=5):
    q = embed_query(query)

    scores = vectors @ q
    best = np.argsort(scores)[-top_k:][::-1]

    results = []

    for i in best:
        ref = refs[i]["reference"]

        results.append({
            "reference": ref,
            "score": float(scores[i])
        })

    return results
