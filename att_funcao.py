def menu_att():
    limpar_term()
    print("--- ATUALIZAR FICHA DE UM POKEMON ---\n")
    if not pokedex:
        print("Não há Pokémon cadastrado...")
    else:
        for p in pokedex:
            print("\nID: " + str(p.id) + "\nNome: " + p.nome)
        try:
            id_att = int(input("\nQual Pokémon (ID) você deseja atualizar?\n"))
            # a variável encontrado foi ideia da IA, evita problemas de localizar ids já excluídos
            encontrado = False


            for p in pokedex:
                if id_att == p.id:
                    encontrado = True
                    selec_att = input("O que você deseja atualizar?: \n"
                                     "1 - Nome \n"
                                     "2 - Tipo \n"
                                     "3 - Nivel\n"
                                     "(Digite qualquer outra tecla para sair)\n")
                    if selec_att == "1":
                        p.nome = input("\nNovo nome: ")
                    elif selec_att == "2":
                        p.tipo = input("\nNovo tipo: ")
                    elif selec_att == "3":
                        p.nivel = int(input("\nNovo nivel: "))
                    else:
                        print("Fim da atualização")

                    print("Pokemon atualizado na Pokedex!")
                    break
            if not encontrado:
                print("Pokémon inexistente...")

        except ValueError:
            print("Digite um ID válido.")
