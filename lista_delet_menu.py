def menu_list():            #Lista os pokemon cadastrados
    limpar_term()
    print("--- LISTA DE POKEMON ---\n")
    if not pokedex:
        print("Não há Pokémon cadastrado...")
    else:
        for p in pokedex:
            print(f"ID: {p.id} | Nome: {p.nome} | Tipo: {p.tipo} | Nível: {p.nivel}")
    voltar()