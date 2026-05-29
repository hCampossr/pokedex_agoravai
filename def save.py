def save():     # Função de salvar os arquivos
    dados = {
        "proxid": proxid,       # guarda o valor da variável de alteração do id
        "pokemon": [asdict(p) for p in pokedex]     #Transforma pokemon em dicionários, pois json não reconhece classes
    }
    with open("pokedex.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)       # Garante que os dados sejam salvos formatados
