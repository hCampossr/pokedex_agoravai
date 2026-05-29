from dataclasses import dataclass

@dataclass
class Pokemon:
    id: int
    nome: str
    tipo: str
    nivel: int

pokedex = []
proxid = 1