import dados
from dados import Pokemon
from telas import limpar_term, voltar
from save import save

def menu_add():
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
            novo_pokemon = Pokemon(id=dados.proxid, nome=nomeadd, nivel=niveladd, tipo=tipoadd)
            dados.pokedex.append(novo_pokemon)
            dados.proxid += 1
            save()
            print("\n" + novo_pokemon.nome + " cadastrado com sucesso!")
    except ValueError:
        print("Insira um nivel válido.")

    voltar()
