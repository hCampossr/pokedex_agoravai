from load import load
from add_funcao import menu_add
from att_funcao import menu_att
from lista_delet_menu import menu_list, menu_del
from telas import limpar_term, voltar

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
