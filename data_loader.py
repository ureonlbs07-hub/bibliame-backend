import os
import requests

DATA_DIR = "data"

FILES = {
    "bible_vectors.npy": "https://SEU_LINK_PUBLICO/bible_vectors.npy",
    "bible_refs.json": "https://SEU_LINK_PUBLICO/bible_refs.json",
    "almeida.json": "https://SEU_LINK_PUBLICO/almeida.json"
}

def ensure_data():

    os.makedirs(DATA_DIR, exist_ok=True)

    for name, url in FILES.items():

        path = os.path.join(DATA_DIR, name)

        if not os.path.exists(path):

            print(f"Downloading {name}...")

            r = requests.get(url, stream=True)
            r.raise_for_status()

            with open(path, "wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)

            print(f"{name} downloaded.")

        else:
            print(f"{name} already exists.")
