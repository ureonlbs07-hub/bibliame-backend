import json
import os

BIBLE_PATH = os.path.join("data", "almeida.json")

bible_data = None


def load_bible():
    global bible_data

    if bible_data is None:
        with open(BIBLE_PATH, encoding="utf-8") as f:
            bible_data = json.load(f)

    return bible_data


def get_verse(book, chapter, verse):

    bible = load_bible()

    for b in bible:
        if b["name"].lower() == book.lower():
            try:
                return b["chapters"][chapter - 1][verse - 1]
            except:
                return "Versículo não encontrado."

    return "Livro não encontrado."
