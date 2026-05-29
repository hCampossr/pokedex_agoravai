def menu_add():     # Função de adicionar pokemon, item por item
    global proxid
    limpar_term()
    print("--- ADICIONAR UM POKÉMON ---\n")
    nomeadd = input("Nome do Pokémon: \n")
    tipoadd = input("Tipo do Pokémon: \n")

    try:
        niveladd = int(input("Nivel do Pokémon: \n"))

        if tipoadd == "":
            tipoadd = "Normal"
        if nomeadd == "" or niveladd <= 0 or niveladd > 100:
            print("Cadastro inválido.")
        else:
            novo_pokemon = Pokemon(id=proxid, nome=nomeadd, nivel=niveladd, tipo=tipoadd)
            pokedex.append(novo_pokemon)
            proxid += 1     # Id aumenta em 1 toda vez que um pokemon novo é registrado
            print("\n " + novo_pokemon.nome + " cadastrado com sucesso!")
    except ValueError:
        print("Insira um nivel válido.")