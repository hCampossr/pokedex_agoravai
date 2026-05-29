import json
import dados
from dataclasses import asdict

def save():
    conteudo = {
        "proxid": dados.proxid,
        "pokemon": [asdict(p) for p in dados.pokedex]
    }
    with open("pokedex.json", "w", encoding="utf-8") as f:
        json.dump(conteudo, f, ensure_ascii=False, indent=4)
