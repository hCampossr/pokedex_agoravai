import json
import os
import dados
from dados import Pokemon

def load():
    if os.path.exists("pokedex.json"):
        try:
            with open("pokedex.json", "r", encoding="utf-8") as f:
                conteudo = json.load(f)
                dados.proxid = conteudo.get("proxid", 1)
                dados.pokedex = [Pokemon(**p) for p in conteudo.get("pokemon", [])]
        except (json.JSONDecodeError, KeyError):
            dados.pokedex = []
            dados.proxid = 1
