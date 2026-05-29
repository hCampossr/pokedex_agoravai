import dados
from telas import limpar_term, voltar
from save import save

def menu_list():
    limpar_term()
    print("--- LISTA DE POKEMON ---\n")
    if not dados.pokedex:
        print("Não há Pokémon cadastrado...")
    else:
        for p in dados.pokedex:
            print(f"ID: {p.id} | Nome: {p.nome} | Tipo: {p.tipo} | Nível: {p.nivel}")
    voltar()

def menu_del():
    limpar_term()
    print("--- REMOVER POKEMON ---\n")
    if not dados.pokedex:
        print("Não há Pokémon cadastrado...")
    else:
        for p in dados.pokedex:
            print("\nID: " + str(p.id) + "\nNome: " + p.nome)

        try:
            id_del = int(input("\nQual Pokémon (ID) você deseja remover?\n"))
            encontrado = False

            for p in dados.pokedex:
                if id_del == p.id:
                    encontrado = True
                    dados.pokedex.remove(p)
                    save()
                    print(f"{p.nome} - {p.id}\nExcluído com sucesso!")
                    break
            if not encontrado:
                print("Pokemon não encontrado...")
        except ValueError:
            print("Digite um ID válido.")
    voltar()

