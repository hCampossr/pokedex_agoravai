#Bibliotecas utilizadas para a criação e manipulação de dicionários, classes e arquivos json
import os
import json
from dataclasses import dataclass, asdict


@dataclass
class Pokemon:      # Criação da classe pokemon, que é composta por diversos tipos de dados
    id: int
    nome: str
    tipo: str
    nivel: int


pokedex = []        # Criação da pokedex, lista que vai guardar todos os pokemon
proxid = 1          # Variável de alteração de ID para cada pokémon criado
