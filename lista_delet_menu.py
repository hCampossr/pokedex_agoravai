def menu_list():            #Lista os pokemon cadastrados
    limpar_term()
    print("--- LISTA DE POKEMON ---\n")
    if not pokedex:
        print("Não há Pokémon cadastrado...")
    else:
        for p in pokedex:
            print(f"ID: {p.id} | Nome: {p.nome} | Tipo: {p.tipo} | Nível: {p.nivel}")
    voltar()

def menu_del():
    limpar_term()
    print("--- REMOVER POKEMON ---\n")
    if not pokedex:
        print("Não há Pokémon cadastrado...")
    else:
        for p in pokedex:
            print("\nID: " + str(p.id) + "\nNome: " + p.nome)

        try:
            id_del = int(input("\nQual Pokémon (ID) você deseja remover?\n"))
            encontrado = False

            for p in pokedex:
                if id_del == p.id:
                    encontrado = True
                    pokedex.remove(p)
                    save()
                    print(f"{p.nome} - {p.id}\nExcluído com sucesso!")
                    break
            if not encontrado:
                print("Pokemon não encontrado...")
        except ValueError:
            print("Digite um ID válido.")
    voltar()

load()

while True:
    limpar_term()
    print("====== SEJA BEM VINDO À POKEDEX ======\n\nO que deseja fazer?\n")
    try:
        menu = int(input(
            "1 - Adicionar um Pokemon\n"
            "2 - Listar os Pokémon cadastrados\n"
            "3 - Atualizar as informações de um Pokémon\n"
            "4 - Remover Pokémon (ID)\n\n"
            "0 - Sair\n\n"))
        
        if menu == 1:
            menu_add()

        elif menu == 2:
           menu_list()

        elif menu == 3:
            menu_att()

        elif menu == 4:
            menu_del()

        elif menu == 0:
            print("\nENCERRANDO... Até breve!")
            break

        else:
            print("\nInválido, digite um número entre 0 e 4")
            voltar()
    except ValueError:
        print("\nErro: Por favor, digite apenas números para opções e IDs.")

